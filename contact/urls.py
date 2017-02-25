from django.conf.urls import url

from .views import ContactUsViewSet

urlpatterns = [
    url(r'^$', ContactUsViewSet.as_view({
    		"post": "create",
    		"get": "list"
    	})),
]
