from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "University"
        verbose_plural_name = "Universities"

    def __unicode__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Student"
        verbose_plural_name = "Students"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
