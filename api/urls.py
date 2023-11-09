from django.urls import include, path
from rest_framework import routers
from .views import CandidatoViewSet, EmpresaViewSet, ExcelExportAPIView
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()

router.register(r'candidato', CandidatoViewSet)
router.register(r'empresa', EmpresaViewSet)

urlpatterns = [
    # path('', RedirectView.as_view(url='api/')),
    path('', include(router.urls)),
    path('export/', ExcelExportAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]