from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('snippet_app.urls')),
	path('users/', include('users.urls')),
	path('hyper/', include('hyperlinks.urls')),
	path('api-auth/', include('rest_framework.urls')),
	path('viewsets/', include('viewsets.urls')),
    path('admin/', admin.site.urls),
]


"""
	Username:  Admin
	Password:  snippetAdmin
"""
