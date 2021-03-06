from django.db import models
from django.contrib.auth.models import User

#product model
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    url = models.URLField()
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:140]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
