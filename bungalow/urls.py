from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls

TITLE = 'Homes API'
DESCRIPTION = 'A REST API for imported home data'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title=TITLE, description=DESCRIPTION)),
]