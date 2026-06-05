from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True, db_column='id')
    admission_no = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'participants_participant'
        managed = False


class MasterTrainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'trainers'
        managed = False


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=50)
    client_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'clients'
        managed = False


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'courses'
        managed = False


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'rooms'
        managed = False


class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'certificates'
        managed = False


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'notifications'
        managed = False


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)

    client = models.ForeignKey(
        Client,
        db_column='client_id',
        on_delete=models.DO_NOTHING
    )

    program_name = models.CharField(max_length=255)

    category = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    duration_days = models.IntegerField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'programs'
        managed = False