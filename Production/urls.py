from django.urls import url

from .views import ProduceViewSet

urlpatterns = [
	url(r'^$', ProduceViewSet.as_view({
			"post": "create"
		}))
]