
from django.urls import path
from app import views
from app.common import API
from django.conf.urls import url


app_name = 'assets'

urlpatterns = [
    path('report/',views.report,name='report'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('index/',views.index,name='index'),
    path('detail/<int:asset_id>/',views.detail,name="detail"),
    path('',views.dashboard),
    path('exccmd/',views.exccmd,name='exccmd'),
    path('CheckAndRelease/',views.CheckAndRelease,name='CheckAndRelease'),
    path('proposal/',views.proposal,name="proposal"),
    path('Inspection/',views.Inspection,name="Inspection"),
    path('upgrade/',views.upgrade,name="upgrade"),
    path('selectcase/',views.selectcase,name="selectcase"),
    path('apschedulerpage/',API.apschedulerpage,name="apschedulerpage"),
]