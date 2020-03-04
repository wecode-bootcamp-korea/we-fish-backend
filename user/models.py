from django.db import models

class User(models.Model):
    kakao_id         = models.CharField(max_length = 50, null = True)
    email            = models.CharField(max_length = 100)
    password         = models.CharField(max_length = 500, null = True)
    name             = models.CharField(max_length = 50, null = True)
    postcode         = models.CharField(max_length = 30)
    address          = models.CharField(max_length = 300)
    detailed_address = models.CharField(max_length = 300, null = True)
    mobile           = models.CharField(max_length = 50, null = True)
    agreement        = models.BooleanField(null = True)
    created_at       = models.DateTimeField(auto_now_add = True)
    updated_at       = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'

class Verification(models.Model):
    mobile  = models.CharField(max_length = 50, null = True)
    code    = models.CharField(max_length = 20, null = True)
    count   = models.CharField(max_length = 20, null = True)

    class Meta:
        db_table = 'verifications'

class Ask(models.Model):
    title   = models.CharField(max_length = 100, null = True)
    author  = models.CharField(max_length = 50, null = True)
    email   = models.CharField(max_length = 100, null = True)
    content = models.TextField(max_length = 2000, null = True)

    class Meat:
        db_table = 'asks'
