"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from test_app.views import simple, Simpleview, SimpleView2, SimpleGenerics, SimpleGenericsUpdate, SimpleViewset
from django.conf import settings

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("simple_viewset", SimpleViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("simple/", simple),
    path("simpleview/", Simpleview.as_view()),
    path("simpleview/<int:id>", Simpleview.as_view()),
    path("simpleview_modal/", SimpleView2.as_view()),
    path("simpleview_modal/<int:id>", SimpleView2.as_view()),
    path("simple_generics/", SimpleGenerics.as_view()),
    path("simple_generics/<int:id>", SimpleGenericsUpdate.as_view()),

    path("api/v1/", include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar 

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns