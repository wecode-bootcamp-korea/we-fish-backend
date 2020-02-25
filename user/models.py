from django.db import models

class User(models.Model):
    email            = models.CharField(max_length = 300)
    password         = models.CharField(max_length = 500)
    name             = models.CharField(max_length = 50)
    date_of_birth    = models.CharField(max_length = 50)
    postcode         = models.CharField(max_length = 50)
    address          = models.CharField(max_length = 300)
    detailed_address = models.CharField(max_length = 300)
    mobile           = models.CharField(max_length = 100)
    created_at       = models.DateTimeField(auto_now_add = True)
    updated_at       = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
