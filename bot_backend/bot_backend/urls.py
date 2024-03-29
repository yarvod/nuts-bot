from django.contrib import admin
from django.urls import path, include
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request):
    return Response(status=status.HTTP_200_OK)


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('healthcheck/', health_check),
]
