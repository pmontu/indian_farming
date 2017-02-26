from django.conf.urls import url

from .views import OrderViewSet

urlpatterns = [
	url(r'^$', OrderViewSet.as_view({
			"post": "create"
		}))
]