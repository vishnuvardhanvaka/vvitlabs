from django.urls import path
from . import views
urlpatterns=[
path('',views.home),
path('ai/',views.ai),
path('ai/<str:expn>',views.ai),
path('os/',views.os),
path('dbms/',views.dbms),
path('r/',views.r),

]