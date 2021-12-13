from django.core.mail import send_mail
from apps.newsletters.models import GetEmail
from django.contrib.auth import get_user_model
from django.conf import settings
from shop.celery import app

User = get_user_model()
MAIN_URL = 'http://89.223.65.30/{}'

@app.task
def send_newsletter(text: str):
    for user in User.objects.all():
        send_mail(
            "Добро пожаловать в KUTURAMO!",
            text, settings.EMAIL_HOST_USER,
            [user.email], fail_silently=False,
        )
    for data in GetEmail.objects.all():
        send_mail(
            "Добро пожаловать в KUTURAMO!",
            text, settings.EMAIL_HOST_USER,
            [data.email], fail_silently=False,
        )
    return 'Send All'


@app.task()
def send_verification_email(email: str):
    message = f"""Добро пожаловать в KAN
    Вы получили это письмо, потому что пользователь {email} указал ваш e-mail для подключения 
    к своему аккаунту.


    Чтобы подтвердить, перейдите по ссылке {MAIN_URL.format('api/v1/email-verify/') + email +'/'}"""
    send_mail(
        "Пожалуйста подтвердите ваш e-mail адрес",
        message, settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
    return 'Send email verification'


@app.task()
def send_order(email: str, order_id: str, data_product, total_price):
    message = f'Ваш заказ #{order_id} получен и обрабатывается администратором, ждите обратной связи)) \n'
    if len(data_product) == 1:
        for i in data_product:
            message = f"""
                    Продукт: {i['title']}
                    Количестко: {i['amount']}
                    Цена: {i['price']}
                    
                    -------------------------------
                    Итоговая цена: {total_price}
                """
    else:
        for i in data_product:
            message += f"""
                    Продукт: {i['title']}
                    Количестко: {i['amount']}
                    Цена: {i['price']}

            """
        message += f"""
                -------------------------------
                Итоговая цена: {total_price}
            """
    send_mail(
        "Информационная служба KUTURAMO",
        message, settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
    return 'Send email send order'
