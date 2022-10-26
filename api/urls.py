from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken import views
from rest_framework_nested import routers
from api.view.comment_view import CommentViewSet

router = routers.DefaultRouter()

""" Comment """
router.register(r"comments", CommentViewSet)

# Basic router
urlpatterns = router.urls

urlpatterns += [path("authorizations/", views.obtain_auth_token)]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
