from django.urls import path

from .views import store_cpu_usages, store_disk_usages, store_memory_usages

urlpatterns = [
    path('cpu-usages/', store_cpu_usages, name='cpu-usages'),
    path('memory-usages/', store_memory_usages, name='memory-usages'),
    path('disk-usages/', store_disk_usages, name='disk=usages'),
]
