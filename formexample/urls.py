from django.conf.urls import url

from formexample import views

urlpatterns=[
    url(r'^form_data$',views.formExample),
]