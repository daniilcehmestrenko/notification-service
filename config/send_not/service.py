import requests


class SendMessage:
    BASE_URL = "https://probe.fbrq.cloud/v1"
    HEADERS = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDE0MjIyMTYsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IktpbWNoaWRldmVsb3BlciJ9.R5mncjM_tjcfZmFmm9qnQpLocod9ANkbJ-UXHOkqLfM"
        }
    
    @classmethod
    def send_message(cls, text, phone, pk):
        message = {
                "id": pk,
                "phone": phone,
                "text": text,
            }
        response = requests.post(
                f'{cls.BASE_URL}/send/{pk}',
                json=message,
                headers=cls.HEADERS
            )
        data = response.json()
        if data["message"] == 'OK':
            return True

        return False
