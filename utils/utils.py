from django.core.mail import send_mail
import os
from growth.settings import EMAIL_ADDR_FORMATED

class EmailUtils:
    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.from_email = EMAIL_ADDR_FORMATED
        self.recipient_list = recipient_list

    def send_email(self):
        send_mail(
            self.subject, 
            self.message, 
            self.from_email, 
            self.recipient_list
        )
            
