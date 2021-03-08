from django.db import models

from accounts.models import CustomUser

import random

# Create your models here.


class Codes(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Codes'

    def __str__(self):
        return str(self.number)


    def save(self, *args, **kwargs):
        number_list = [num for num in range(10)]
        code_items = []
        
        for i in range(5):
            number = random.choice(number_list)
            code_items.append(number)
        code_string = "".join(str(item) for item in code_items)
        self.number = code_string

        super().save(*args, **kwargs)

