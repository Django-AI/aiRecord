from django.contrib import admin
from django.urls.conf import include, path
from django.views.generic.base import RedirectView


urlpatterns = (
    # Home URL redirected to Admin
    path('', RedirectView.as_view(url='admin')),

    # Admin URLs
    path('admin/', admin.site.urls),

    # Query Profiling URLs
    path('silk/', include('silk.urls', namespace='silk')),

    # REST Framework URLs
    path('api/auth/', include('rest_framework.urls')),

    # H1st URLs
    path('h1st/', include('h1st.django.urls')),
)
