import requests


class SendMail:
    BASE_URL = "https://probe.fbrq.cloud/v1"
    HEADERS = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDE0MjIyMTYsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IktpbWNoaWRldmVsb3BlciJ9.R5mncjM_tjcfZmFmm9qnQpLocod9ANkbJ-UXHOkqLfM"
        }
    
    def send_mail(self, text, phone, pk):
        message = {
                "id": pk,
                "phone": phone,
                "text": text,
            }
        response = requests.post(
                f'{self.BASE_URL}/send/{pk}',
                json=message,
                headers=self.HEADERS
            )
        data = response.json()
        if data["message"] == 'OK':
            return True

        return False
