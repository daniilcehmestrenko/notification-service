from config.celery import app

from .service import SendMessage


@app.task
def send_message(pk, phone, text):
    SendMessage.send_message(
            pk=pk,
            phone=phone,
            text=text
        )
