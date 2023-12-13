from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name = 'index'), # path for index page (+ handles colab requests)
    path("handle_sms/", views.handle_sms), # this path hadnles webhooks for sms
    path('res/', views.testt_handler)
]