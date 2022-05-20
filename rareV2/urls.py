from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rareV2Api.views.comments import CommentView
from rareV2Api.views import register_user, login_user, TagView
from rareV2Api.views import CategoryView
from rareV2Api.views.post import PostView
from rareV2Api.views import TagView
from rareV2Api.views.rareuser import RareUserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')
router.register(r'tags', TagView, 'tag')
router.register(r'posts', PostView, 'posts')
router.register(r'comments', CommentView, 'comments')
router.register(r'rare_users', RareUserView, 'rare_user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
