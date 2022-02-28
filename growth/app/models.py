from django.db import models

class Kid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent_phone_number = models.CharField(max_length=100)
    parent_email_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_url = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=100)
    food_group = models.CharField(max_length=100)

    def image_tag(self):
        return u'<img src="%s" width="150" height="150" />' % self.image_url

    def __str__(self):
        return self.kid.name

