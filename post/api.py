from sqlite3 import IntegrityError

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from models import Users, Category, Order, ServiceMaster


class CategoryResources(ModelResource):
    class Meta:
        resource_name = 'category'
        queryset = Category.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'category': ALL_WITH_RELATIONS,
        }


class UserResource(ModelResource):
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


class ServicesResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    category = fields.ForeignKey(CategoryResources, 'category', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = ServiceMaster.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'service'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
        }


class OrderResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)
    category = fields.ForeignKey(CategoryResources, 'category', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Order.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'order'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
            'status': ALL,
        }
