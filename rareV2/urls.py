from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rareV2Api.views import CategoryView
from rareV2Api.views import register_user, login_user
from rareV2Api.views.post import PostView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')


router.register(r'posts', PostView, 'posts')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
