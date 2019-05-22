"""Farm_Website URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage', views.homepage, name='homepage'),
    url(r'^data/homepage', views.dataactionselect, name='datahomepage'),
    url(r'^data/rowselect/(?P<id>[ab-d])', views.rowselect, name='rowselect'),
    url(r'^data/lotselect', views.lotselect, name='lotselect'),
    url(r'^science/home', views.sciencehome, name='sciencehome'),
    url(r'^data/getrow/(?P<id>[ab-d])/', views.getrow, name="getrow"),
    url(r'^data/submitdata/(?P<lot_id>[ab-d])/(?P<row_id>[0-9][0-9])/', views.submitdata, name="submitdata"),
    url(r'^data/view/viewrow', views.viewrow, name='viewrow'),
    url(r'^data/view/rowdata', views.rowdata, name='rowdata'),
    url(r'^data/view/getplant/(?P<id>.{0,100})', views.getplant, name="getplant"),
    url(r'^data/edit/(?P<id>.{0,100})', views.editplant, name="editplant"),
    url(r'^data/updateplant/(?P<id>.{0,100})', views.updateplant, name="updateplant"),
    url(r'^data/delete/(?P<id>.{0,100})', views.deleteplant, name="deleteplant"),
    url(r'^data/view/viewall', views.viewall, name="viewall"),
    url(r'^data/deleterowdata/(?P<lot_id>[ab-d])/(?P<row_id>[0-9][0-9])', views.deleterowdata, name="deleterowdata"),
    url(r'^about', views.about, name="about"),
    url(r'^data/qr/(?P<lot_id>[ab-d])/(?P<row_id>[0-9][0-9])/', views.qrredirect, name="qrredirect"),
    url(r'^archive', views.archive, name='archive'),
    url(r'^science/post', views.sciencepost, name='sciencepost'),
    url(r'^', views.homepage, name='homepage')
]
