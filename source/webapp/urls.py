from django.urls import path

from webapp.views import calc_view, result_view

urlpatterns = [
    path('', calc_view),
    path('result/', result_view)
]