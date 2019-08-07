"""recipie_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from recipie_box.views import index, recipie, author, addauthor, addrecipie, loginpage, logoutpage
from recipie_box.models import Author, Recipie


admin.site.register(Author)
admin.site.register(Recipie)
# admin.site.register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('recipies/<int:id>', recipie),
    path('author/<int:id>', author),
    path('addauthor/', addauthor),
    path('addrecipie/', addrecipie),
    path('login/', loginpage),
    path('logout/', logoutpage, name='logout')
]
