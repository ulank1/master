# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


def image_upload_to(instance, filename):
    return "images/%s" % filename


class Users(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    phone = models.CharField(max_length=30, verbose_name="Тел. номер")
    name = models.CharField(max_length=30, verbose_name="ФИО")
    age = models.CharField(max_length=20, verbose_name="День рождения", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    category = models.CharField(max_length=200, verbose_name="Категория")

    def __unicode__(self):
        return self.category


class ServiceMaster(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    address = models.CharField(verbose_name="адрес", max_length=500, null=True, blank=True)
    description = models.TextField(verbose_name="описание", null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    experience = models.FloatField(verbose_name="Опыт", null=True, blank=True)
    lat = models.FloatField(max_length=20, null=True, blank=True)
    lng = models.FloatField(max_length=20, null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='категория')
    user = models.ForeignKey(Users, verbose_name='пользователь')

    def __unicode__(self):
        return self.address


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    category = models.ForeignKey(Category, verbose_name='категория')
    user = models.ForeignKey(Users, verbose_name='заказчик', null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    address = models.CharField(verbose_name="адрес", max_length=500, null=True, blank=True)
    lat = models.FloatField(max_length=20, null=True, blank=True)
    lng = models.FloatField(max_length=20, null=True, blank=True)
    description = models.TextField(verbose_name="описание", max_length=500, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.address