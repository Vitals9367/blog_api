"""blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def healthz(*args, **kwargs):
    """Returns status code 200 if the server is alive."""
    return HttpResponse(status=200)


def readiness(*args, **kwargs):
    """
    Returns status code 200 if the server is ready to perform its duties.
    This goes through each database connection and perform a standard SQL
    query without requiring any particular tables to exist.
    """
    from django.db import connections

    for name in connections:
        cursor = connections[name].cursor()
        cursor.execute("SELECT 1;")
        cursor.fetchone()

    return HttpResponse(status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('healthz/', healthz),
    path('readiness/', readiness),
]
