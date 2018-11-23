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
    device_id = models.CharField(max_length=20, verbose_name="device id", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория задач'
        verbose_name_plural = 'Категории задач'

    category = models.CharField(max_length=200, verbose_name="Категория")

    def __unicode__(self):
        return self.category


class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='категория')

    class Meta:
        verbose_name = 'Подкатегория задач'
        verbose_name_plural = 'Подкатегории задач'

    sub_category = models.CharField(max_length=200, verbose_name="Подкатегория")

    def __unicode__(self):
        return self.sub_category


class CategoryService(models.Model):
    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'

    category = models.CharField(max_length=200, verbose_name="Категория")

    def __unicode__(self):
        return self.category


class SubCategoryService(models.Model):
    category = models.ForeignKey(CategoryService, verbose_name='категория')

    class Meta:
        verbose_name = 'Подкатегория услуг'
        verbose_name_plural = 'Подкатегории услуг'

    sub_category = models.CharField(max_length=200, verbose_name="Подкатегория")

    def __unicode__(self):
        return self.sub_category


class ForumCategory(models.Model):
    class Meta:
        verbose_name = 'Категория Форума'
        verbose_name_plural = 'Категории Форума'

    category = models.CharField(max_length=200, verbose_name="Категория")

    def __unicode__(self):
        return self.category


class ForumSubCategory(models.Model):
    category = models.ForeignKey(ForumCategory, verbose_name='категория')

    class Meta:
        verbose_name = 'Подкатегория Форума'
        verbose_name_plural = 'Подкатегории Форума'

    sub_category = models.CharField(max_length=200, verbose_name="Подкатегория")

    def __unicode__(self):
        return self.sub_category


class Forum(models.Model):
    class Meta:
        verbose_name = 'Форум'
        verbose_name_plural = 'Форум'

    description = models.TextField(verbose_name="описание", null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    title = models.CharField(verbose_name='название', max_length=200, null=True, blank=True)
    count = models.IntegerField(verbose_name='количество', default=0, null=True, blank=True)
    sub_category = models.ForeignKey(ForumSubCategory, verbose_name='категория')
    user = models.ForeignKey(Users, verbose_name='пользователь')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    user = models.ForeignKey(Users, verbose_name='пользователь')
    forum = models.ForeignKey(Forum, verbose_name='форум')
    comment = models.CharField(verbose_name='Коментарий', max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title


class Confirmation(models.Model):
    user = models.ForeignKey(Users, verbose_name='пользователь')
    forum = models.ForeignKey(Forum, verbose_name='форум')
    confirmation = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ServiceMaster(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    image1 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка1', null=True, blank=True)
    image2 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка2', null=True, blank=True)
    image3 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка3', null=True, blank=True)
    image4 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка4', null=True, blank=True)
    image5 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка5', null=True, blank=True)

    address = models.CharField(verbose_name="адрес", max_length=500, null=True, blank=True)
    description = models.TextField(verbose_name="описание", null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    experience = models.FloatField(verbose_name="Опыт", null=True, blank=True)
    lat = models.FloatField(max_length=20, null=True, blank=True)
    lng = models.FloatField(max_length=20, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryService, verbose_name='категория', null=True, blank=True)
    user = models.ForeignKey(Users, verbose_name='пользователь', null=True, blank=True)

    def __unicode__(self):
        return self.address


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    image1 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка1', null=True, blank=True)
    image2 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка2', null=True, blank=True)
    image3 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка3', null=True, blank=True)
    image4 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка4', null=True, blank=True)
    image5 = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка5', null=True, blank=True)

    sub_category = models.ForeignKey(SubCategory, verbose_name='категория', null=True, blank=True)
    user = models.ForeignKey(Users, verbose_name='заказчик', null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка', null=True, blank=True)
    address = models.CharField(verbose_name="адрес", max_length=500, null=True, blank=True)
    lat = models.FloatField(max_length=20, null=True, blank=True)
    lng = models.FloatField(max_length=20, null=True, blank=True)
    description = models.TextField(verbose_name="описание", max_length=500, null=True, blank=True)
    status = models.IntegerField(default=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.address


class ConfirmationOrder(models.Model):
    user = models.ForeignKey(Users, verbose_name='пользователь')
    order = models.ForeignKey(Order, verbose_name='Заказ')
    status = models.IntegerField(default=1, null=True, blank=True)
    confirmation = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ConfirmationService(models.Model):
    user = models.ForeignKey(Users, verbose_name='пользователь')
    order = models.ForeignKey(ServiceMaster, verbose_name='Заказ')
    status = models.IntegerField(default=1, null=True, blank=True)
    confirmation = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(Users, verbose_name='пользователь')
    status = models.IntegerField(null=True, blank=True, verbose_name='оценка')


class CommentUser(models.Model):
    user = models.ForeignKey(Users, verbose_name='пользователь')
    comment = models.CharField(max_length=200, null=True, blank=True, verbose_name='коментарий')

    def __unicode__(self):
        return self.comment
