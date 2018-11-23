# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Users, Category, Order, ServiceMaster, SubCategory, Forum, ForumSubCategory, ForumCategory, \
    Confirmation, ConfirmationOrder, SubCategoryService, CategoryService, Review, CommentUser


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


class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory


admin.site.register(SubCategory, SubCategoryAdmin)


class CategoryAdminService(admin.ModelAdmin):
    model = CategoryService


admin.site.register(CategoryService, CategoryAdminService)


class SubCategoryAdminService(admin.ModelAdmin):
    model = SubCategoryService


admin.site.register(SubCategoryService, SubCategoryAdminService)


class ForumCategoryAdmin(admin.ModelAdmin):
    model = ForumCategory


admin.site.register(ForumCategory, ForumCategoryAdmin)


class ForumSubCategoryAdmin(admin.ModelAdmin):
    model = ForumSubCategory


admin.site.register(ForumSubCategory, ForumSubCategoryAdmin)


class ForumAdmin(admin.ModelAdmin):
    model = Forum
    readonly_fields = 'created_at updated_at'.split()
    list_display = ("title", "display_user_name", "display_category")

    def display_user_name(self, obj):
        return obj.user.name

    def display_category(self, obj):
        return obj.sub_category.sub_category


admin.site.register(Forum, ForumAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = 'created_at updated_at'.split()
    list_display = ("display_user_name", "display_category")

    def display_user_name(self, obj):
        return obj.user.name

    def display_category(self, obj):
        return obj.sub_category.sub_category


admin.site.register(Order, OrderAdmin)


class ServiceAdmin(admin.ModelAdmin):
    model = ServiceMaster
    list_display = ("display_user_name", "display_category")

    def display_user_name(self, obj):
        return obj.user.name

    def display_category(self, obj):
        return obj.sub_category.sub_category


admin.site.register(ServiceMaster, ServiceAdmin)


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ("display_user_name", "status")

    def display_user_name(self, obj):
        return obj.user.name


admin.site.register(Review, ReviewAdmin)


class CommentUserAdmin(admin.ModelAdmin):
    model = CommentUser
    list_display = ("display_user_name", "comment")

    def display_user_name(self, obj):
        return obj.user.name


admin.site.register(CommentUser, CommentUserAdmin)
