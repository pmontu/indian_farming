from django.conf.urls import url

from .views import UserViewSet

urlpatterns = [
    url(r'^$', UserViewSet.as_view({
    		"get": "list",
    		"post": "create"
    	})),
]
