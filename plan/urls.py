from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from plan import views

router = routers.DefaultRouter()
router.register(r'merchants', views.MerchantViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-list/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]