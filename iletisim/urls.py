from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.iletiListe,name="iletiListe"), #127.0.0.1:8000/iletisim/
    path('detay/<int:pk>/',views.iletiDetay,name="iletiDetay"),
    path('ileti/yeni/',views.yeni_ileti,name="yeni_ileti"),
    path('iletiduzenle/<int:pk>',views.iletiduzenle,name="iletiduzenle"),
]
