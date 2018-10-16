"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from post.api import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(CategoryResources())
v1_api.register(SubCategoryResources())
v1_api.register(CategoryResourcesService())
v1_api.register(SubCategoryResourcesService())
v1_api.register(UserResource())
v1_api.register(OrderResource())
v1_api.register(ServicesResource())
v1_api.register(ForumCategoryResources())
v1_api.register(ForumSubCategoryResources())
v1_api.register(ForumResource())
v1_api.register(CommentResource())
v1_api.register(ConfirmationResource())
v1_api.register(ConfirmationOrderResource())

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]
