from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
from utils.utils import EmailUtils

STATUS_CHOICES = [     
    ('fruit',"Fruit"),
    ('vegetable',"Vegetable"),
    ('grain',"Grain"),
    ('protein',"Protein"),
    ('dairy',"Dairy"),
    ('unknown',"Unknown"),
]

class Kid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent_phone_number = models.CharField(max_length=100)
    parent_email_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=100)
    food_group = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def image_tag(self):
        print(dir(self.image_url))
        return mark_safe('<img src="{}" width="250" height="250" />'.format(self.image_url))

    def save(self, *args, **kwargs):
        if self.food_group == 'unknown':
            # send email to admin
            subject = 'Food Group Unknown'
            body = 'Food Group Unknown for {}'.format(self.kid.name)
            recipient = [self.kid.parent_email_address]
            mail_message = EmailUtils(subject, body, recipient)
            mail_message.send_email()
            self.is_approved = False
        else:
            self.is_approved = True
        super(Image, self).save(*args, **kwargs)

