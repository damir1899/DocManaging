from rest_framework import permissions, routers

from .views import DocumentViewSet


router = routers.DefaultRouter()
router.register('api/document', DocumentViewSet, basename='document')

