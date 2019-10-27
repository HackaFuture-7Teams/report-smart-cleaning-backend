from django.urls import path

from smart_report.views import InputCreateView

urlpatterns = [
    path('create/product/', InputCreateView.as_view()),
]
