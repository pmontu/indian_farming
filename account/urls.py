from django.conf.urls import url

from .views import AccountViewSet

urlpatterns = [
	url(r'^$', AccountViewSet.as_view({
			"post": "create"
		}))
]