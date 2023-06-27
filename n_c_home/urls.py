from django.urls import path
from n_c_home import views as v

app_name='app'

urlpatterns = [
    path("", v.index, name='index'),
    path("searchInfo/", v.searchInfo, name='searchInfo'),
    path("naverCrawling/", v.naverCafeInfo, name='naverCafeInfo'),
    path("naverSCrawling/", v.naverCafeSearch, name='naverCafeSearch'),
]