from django.urls import path

from .views import HomePageView, CPUUsageView, MemoryUsageView, DiskUsageView

urlpatterns = [
   path('cpu/', CPUUsageView.as_view(), name='cpu'),
   path('disk/', DiskUsageView.as_view(), name='disk'),
   path('memory/', MemoryUsageView.as_view(), name='memory'),
   path('', HomePageView.as_view(), name='home'),
]
