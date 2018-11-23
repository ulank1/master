from sqlite3 import IntegrityError

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from models import Users, Category, Order, ServiceMaster, SubCategory, Forum, ForumSubCategory, ForumCategory, Comment, \
    Confirmation, ConfirmationOrder, CategoryService, SubCategoryService, ConfirmationService, Review, CommentUser


class MultipartResource(object):
    def deserialize(self, request, data, format=None):

        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart/form-data'):
            multipart_data = request.POST.copy()
            multipart_data.update(request.FILES)
            return multipart_data

        return super(MultipartResource, self).deserialize(request, data, format)

    def put_detail(self, request, **kwargs):
        if request.META.get('CONTENT_TYPE', '').startswith('multipart/form-data') and not hasattr(request, '_body'):
            request._body = ''
        return super(MultipartResource, self).put_detail(request, **kwargs)

    def patch_detail(self, request, **kwargs):
        if request.META.get('CONTENT_TYPE', '').startswith('multipart/form-data') and not hasattr(request, '_body'):
            request._body = ''
        return super(MultipartResource, self).patch_detail(request, **kwargs)


class CategoryResources(MultipartResource, ModelResource):
    class Meta:
        resource_name = 'category'
        queryset = Category.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'category': ALL_WITH_RELATIONS,
        }


class SubCategoryResources(MultipartResource, ModelResource):
    category = fields.ForeignKey(CategoryResources, 'category', full=True)

    class Meta:
        resource_name = 'subcategory'
        queryset = SubCategory.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'sub_category': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
        }


class CategoryResourcesService(MultipartResource, ModelResource):
    class Meta:
        resource_name = 'category_service'
        queryset = CategoryService.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'category': ALL_WITH_RELATIONS,
        }


class SubCategoryResourcesService(MultipartResource, ModelResource):
    category = fields.ForeignKey(CategoryResourcesService, 'category', full=True)

    class Meta:
        resource_name = 'subcategory_service'
        queryset = SubCategoryService.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'sub_category': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
        }


class UserResource(MultipartResource, ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Users.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'users'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'phone': ALL_WITH_RELATIONS,
            'name': ALL_WITH_RELATIONS,
        }


class ForumCategoryResources(MultipartResource, ModelResource):
    class Meta:
        resource_name = 'forumcategory'
        queryset = ForumCategory.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'category': ALL_WITH_RELATIONS,
        }


class ForumSubCategoryResources(MultipartResource, ModelResource):
    category = fields.ForeignKey(ForumCategoryResources, 'category', full=True)

    class Meta:
        resource_name = 'forumsubcategory'
        queryset = ForumSubCategory.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'sub_category': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
        }


class ForumResource(MultipartResource, ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    sub_category = fields.ForeignKey(ForumSubCategoryResources, 'sub_category', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Forum.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'forum1'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
            'sub_category': ALL_WITH_RELATIONS,
            'title': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'description': ALL_WITH_RELATIONS,
        }


class CommentResource(MultipartResource, ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    forum = fields.ForeignKey(ForumResource, 'forum', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Comment.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'comment'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'comment': ALL_WITH_RELATIONS,
            'forum': ALL_WITH_RELATIONS,
        }


class ConfirmationResource(MultipartResource, ModelResource):
    forum = fields.ForeignKey(ForumResource, 'forum', null=True, full=True)
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Confirmation.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'confirmation'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
            'forum': ALL_WITH_RELATIONS,
        }


class ServicesResource(MultipartResource, ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    sub_category = fields.ForeignKey(SubCategoryResourcesService, 'sub_category', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = ServiceMaster.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'service'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'sub_category': ALL_WITH_RELATIONS,
        }


class OrderResource(MultipartResource, ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    sub_category = fields.ForeignKey(SubCategoryResources, 'sub_category', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Order.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'order'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'sub_category': ALL_WITH_RELATIONS,
            'status': ALL,
        }


class ConfirmationOrderResource(MultipartResource, ModelResource):
    order = fields.ForeignKey(OrderResource, 'order', null=True, full=True)
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = ConfirmationOrder.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'confirm'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'status': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
            'order': ALL_WITH_RELATIONS,
        }


class ConfirmationServiceResource(MultipartResource, ModelResource):
    order = fields.ForeignKey(ServicesResource, 'order', null=True, full=True)
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = ConfirmationService.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'confirm_service'
        filtering = {
            'id': ALL_WITH_RELATIONS,
            'status': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
            'order': ALL_WITH_RELATIONS,
        }


class ReviewResource(MultipartResource, ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Review.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'review'
        filtering = {
            'status': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
        }


class CommentUserResource(MultipartResource, ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = CommentUser.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'comment_user'
        filtering = {
            'comment': ALL_WITH_RELATIONS,
            'user': ALL_WITH_RELATIONS,
        }
