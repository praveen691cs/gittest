from django.conf.urls import url

from company import views
from testApp import views as testview
urlpatterns=[
    url(r'^company_hello$',views.helloDjango,name='company_hello'),
    url(r'company_hello1$',testview.helloDjango,name='company_hello1')
]