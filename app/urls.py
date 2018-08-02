from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import SignInViewSet, UserBaseViewSet, RoleBaseViewSet

router = DefaultRouter()
router.register(r'adm/user', UserBaseViewSet, base_name='user')
router.register(r'adm/role', RoleBaseViewSet, base_name='role')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth-jwt/', SignInViewSet.as_view())
]
