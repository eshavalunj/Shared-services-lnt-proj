from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'clients'
        managed = False