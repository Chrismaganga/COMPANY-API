from blog.views import CompanyProfileViewSet, UserProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CompanyProfileViewSet, basename='company_profile'),
router.register('user-profile', UserProfileViewSet, basename='user_profile')
urlpatterns = router.urls