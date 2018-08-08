# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Users, Category, Order, ServiceMaster


# Register your models here.


# def invited_user(obj):
#     return "\n".join([user.username for user in obj.invited.all()])
#
#
# class RoomAdmin(admin.ModelAdmin):
#     """Комнаты чата"""
#     list_display = ("date", "text")
#
#
# admin.site.register(User, RoomAdmin)


class UserAdmin(admin.ModelAdmin):
    model = Users
    readonly_fields = 'created_at updated_at'.split()
    list_display = ("name", "phone")

admin.site.register(Users, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    model = Category

admin.site.register(Category, CategoryAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = 'created_at updated_at'.split()
    list_display = ("display_user_name", "display_category")

    def display_user_name(self, obj):
        return obj.user.name

    def display_category(self, obj):
        return obj.category.category


admin.site.register(Order, OrderAdmin)


class ServiceAdmin(admin.ModelAdmin):
    model = ServiceMaster
    list_display = ("display_user_name", "display_category")

    def display_user_name(self, obj):
        return obj.user.name

    def display_category(self, obj):
        return obj.category.category


admin.site.register(ServiceMaster, ServiceAdmin)
