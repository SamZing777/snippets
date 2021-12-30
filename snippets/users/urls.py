from django.urls import path

from .views import (
	UserList,
	UserDetail
	)

urlpatterns = [ 
	path('', UserList.as_view(), name='users'),
	path('<int:pk>/', UserDetail.as_view(), name='user_detail')
]

"""
	Henry
	snippetAdmin
"""
