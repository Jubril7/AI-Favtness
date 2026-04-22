from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/\nDisallow: /accounts/\nAllow: /"
    return HttpResponse(content, content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # password reset
    path('', include('gym.urls')),
    path('robots.txt', robots_txt),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'gym.views.error_404'
handler500 = 'gym.views.error_500'
