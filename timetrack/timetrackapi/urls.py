from django.urls import include, path, re_path
from rest_framework import routers
from . import views

from django.conf.urls import include, url


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'worklogs', views.WorkLogViewSet)
#router.register(r'upload', views.WorkLogView, basename='worklogs')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^upload', views.FileUploadView.as_view()),
    path('<str:username>', include(router.urls)),
]

urlpatterns += router.urls