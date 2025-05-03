from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, PatientViewSet, DoctorViewSet, MappingViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
router.register('doctors', DoctorViewSet, basename='doctors')
router.register('mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('mappings/<int:patient_id>/', MappingViewSet.as_view({'get': 'list'}), name='mapping-by-patient'),  # This is the fix
    path('', include(router.urls)),
]
