from shop_project.celery import app
from .sending_email import send_email


@app.task
def send_email_task(user_email, secret_code):
    try:
        send_email(user_email, secret_code)

    except Exception as _ex:
        return _ex