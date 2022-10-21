from django.db import models


# Класс новости
class News(models.Model):
    name = models.CharField(
        max_length=50,
        default="Good news, everyone!"
    )
    text = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)

