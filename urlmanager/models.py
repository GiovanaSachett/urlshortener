from django.db import models

MAX_URL_SIZE = 500
HASH_SIZE = 10

class URL(models.Model):
    original_url = models.CharField(max_length=MAX_URL_SIZE)
    hash = models.CharField(max_length=HASH_SIZE, db_index=True, primary_key=True)
    enabled = models.BooleanField()
