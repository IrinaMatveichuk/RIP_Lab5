from django.conf.urls import url, include
from django.contrib import admin
from my_lab5 import views
from my_lab5.views import FiguresView, FigureView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^figures/$', FiguresView.as_view()),
    url(r'^figures/(?P<id>\d+)$', FigureView.as_view(), name='figure_url')
]
