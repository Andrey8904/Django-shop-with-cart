from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import RegisterUserForm, LoginUserForm, ActivateCodeForm, ActivateEmailForm
from django.contrib.auth import logout
from favorites.models import Favorites
from shop.models import Product
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from random import randint
from .tasks import send_email_task


class Register(View):

    def get(self, request):
        if 'user_id' in request.session:
            return redirect('reg_log:dashboard')

        form = RegisterUserForm()
        data = {'form': form, 'user': None}
        return render(request, 'reg_log/register.html', data)

    def post(self, request):
        clear_form = RegisterUserForm()
        data = {'form': clear_form}
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user_name = form_data['user_name']
            user_email = form_data['user_email']
            user_password = form_data['user_password']
            user_password_repeat = form_data['user_password_repeat']
            user_agree = form_data['user_agree']

            if user_password != user_password_repeat:
                messages.error(request, 'пароли не совпали')
                return render(request, 'reg_log/register.html', data)

            try:
                user = CustomUser.objects.filter(user_email=user_email)
                if not user:
                    user = CustomUser(
                        user_name=user_name,
                        user_email=user_email,
                        user_password=make_password(user_password),
                        user_agree=user_agree
                    )

                    user.save()
                    # генерирование кода
                    secret_code = randint(10000, 99999)
                    # отправка кода на почту
                    send_email_task.delay(user_email, secret_code)
                    request.session['u_email'] = user_email
                    # запись кода в сессию
                    request.session['secret_code'] = secret_code
                    messages.success(request, 'Вы успешно зарегестрировались. Подтвердите почту.')
                    return redirect('reg_log:activate')

                messages.error(request, 'user уже существует')
                return render(request, 'reg_log/register.html', data)

            except:
                return render(request, 'reg_log/register.html', data)

        return render(request, 'reg_log/login.html')


class Activate(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('reg_log:dashboard')

        form = ActivateCodeForm()
        data = {'form': form, 'user': None}
        return render(request, 'reg_log/activate.html', data)

    def post(self, request):
        activate_code = request.POST['activate_code']
        user_email = request.session['u_email']
        if int(activate_code) == request.session['secret_code']:
            CustomUser.objects.filter(user_email=user_email).update(user_activated=True)
            messages.success(request, 'вы активированы')
            return redirect('reg_log:login')

        return redirect('reg_log:activate')


class CantEnter(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('reg_log:dashboard')
        return render(request, 'reg_log/cant_enter.html', {'user': None})


class OtherActivate(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('reg_log:dashboard')
        form = ActivateEmailForm()
        data = {'user': None, 'form_email': form}
        return render(request, 'reg_log/other_activate.html', data)

    def post(self, request):
        user_email = request.POST['user_email']
        user = CustomUser.objects.filter(user_email=user_email).first()
        if user is not None and user.user_activated == 0:
            u_email = user.user_email
            secret_code = randint(10000, 99999)
            send_email_task.delay(user_email, secret_code)
            request.session['secret_code'] = secret_code
            request.session['u_email'] = u_email
            messages.success(request, 'Код отправлен, укажите код в форме')
            return redirect('reg_log:other_activate_code')
        messages.error(request, 'Нет Email или вы уже активированны')
        return redirect('reg_log:other_activate')


class OtherActivateCode(View):
    def get(self, request):
        if 'user_id' in request.session:
            return redirect('reg_log:dashboard')
        form = ActivateCodeForm()
        data = {'user': None, 'form': form}
        return render(request, 'reg_log/other_activate_code.html', data)

    def post(self, request):
        secret_code_form = request.POST['activate_code']
        session_code = request.session['secret_code']
        session_email = request.session['u_email']
        if int(secret_code_form) == session_code:
            CustomUser.objects.filter(user_email=session_email).update(user_activated=True)
            return redirect('reg_log:login')
        return redirect('reg_log:other_activate')


class Login(View):

    def get(self, request):
        if 'user_id' in request.session:
            return redirect('reg_log:dashboard')

        form = LoginUserForm()
        data = {'form': form, 'user': None}
        return render(request, 'reg_log/login.html', data)

    def post(self, request):
        form = LoginUserForm()
        data = {'form': form, 'user': None}
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user = CustomUser.objects.filter(user_email=user_email).first()
        if user is not None:
            stored_password = user.user_password
            bytes_user = user_password
            if check_password(bytes_user, stored_password) and user.user_activated == 1:
                request.session['user_id'] = user.id
                return redirect('reg_log:dashboard')

            messages.error(request, 'Не тот логин или пароль')
            return render(request, 'reg_log/login.html', data)
        return render(request, 'reg_log/login.html', data)


class Dashboard(View):
    def get(self, request):
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = CustomUser.objects.get(pk=user_id)

            favorites = Favorites.objects.filter(user_id=user_id)
            favorite_ids = [favorite.product_id for favorite in favorites]
            favorite_products = Product.objects.filter(id__in=favorite_ids)
            data = {'user': user, 'favorite_products': favorite_products}
            return render(request, 'reg_log/dashboard/dashboard.html', data)
        return redirect('reg_log:login')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('shop:index')
