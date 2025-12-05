from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),
    path('api/specialists/', include('specialists.urls')),
    path('api/reviews/', include('reviews.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('specialists-page/', TemplateView.as_view(template_name='specialists.html')),
    path('specialist/', TemplateView.as_view(template_name='specialist_detail.html')),
    path('specialist-register/', TemplateView.as_view(template_name='specialist_register.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)