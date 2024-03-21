from django.shortcuts import render, redirect
from .forms import RestorePasswordForm, RestoreCodeForm, NewPasswordForm
from reg_log.models import CustomUser
from django.contrib import messages
from random import randint
from .tasks import send_email_task
from django.contrib.auth.hashers import make_password



def restore(request):
    if 'user_id' in request.session:
        return redirect('reg_log:dashboard')


    if request.method == 'GET':
        form_email = RestorePasswordForm()
        data = {'form_email': form_email, 'user': None}
        return render(request, 'restore_password/restore.html', data)

    if request.method == 'POST':
        user_email = request.POST['user_email']
        user = CustomUser.objects.filter(user_email=user_email).first()
        if user is not None:
            u_email = user.user_email
            secret_code = randint(10000, 99999)
            send_email_task.delay(user_email, secret_code)
            request.session['secret_code'] = secret_code
            request.session['u_email'] = u_email
            print(secret_code)
            messages.success(request, 'Код отправлен, укажите код в форме')
            return redirect('restore:restore_code')

        form_email = RestorePasswordForm()
        data = {'form_email': form_email, 'user': None}
        messages.error(request, 'Нет Email')
        return render(request, 'restore_password/restore.html', data)


def restore_code(request):
    if 'user_id' in request.session:
        return redirect('reg_log:dashboard')

    if request.method == 'GET':
        form = RestoreCodeForm()
        data = {'form_code': form, 'user': None}
        return render(request, 'restore_password/secret_code.html', data)
    user_code = request.POST['user_code']
    if int(user_code) != request.session['secret_code']:
        messages.error(request, 'не тот код')
        return redirect('restore:restore_password')
    return redirect('restore:new_password')


def new_password(request):
    if 'user_id' in request.session:
        return redirect('reg_log:dashboard')

    form = NewPasswordForm()
    data = {'form_new_password': form, 'user': None}
    if request.method == 'GET':
        return render(request, 'restore_password/new_password.html', data)

    if request.method == 'POST':
        password_one = request.POST['user_password']
        password_two = request.POST['user_password_repeat']
        if password_one != password_two:
            messages.error(request, 'ошибка пароль')
            return render(request, 'restore_password/new_password.html', data)

        u_email = request.session['u_email']
        user = CustomUser.objects.filter(user_email=u_email).first()
        CustomUser.objects.filter(pk=user.id).update(user_password=make_password(password_one))

        messages.success(request, 'успешный смена пароля')
        return redirect('reg_log:login')



