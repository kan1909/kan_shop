from shop.celery import app
from django.core.mail import send_mail

@app.task()
def reset_password_message_sender(message_text: str, reset_password_token):
    send_mail(
        # title:
        "Password Reset for {title}".format(title="KAN"),
        # message:
        message_text,
        # from:
        "aaanaconda@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
    return "Send Reset Password"
