"""joca_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from joca_app2 import views as joca_app2
from joca_app1 import views as joca_app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view3/',joca_app2.lista),
    path('view4/',joca_app2.func),

    path('view1/', joca_app1.primer),
    path('view2/', joca_app1.HorayFecha)
]
