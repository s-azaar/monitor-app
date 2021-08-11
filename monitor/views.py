from django.views.generic import TemplateView, ListView

from collector.models import CPU, Memory, Disk


class HomePageView(TemplateView):
    template_name = 'home.html'


class CPUUsageView(ListView):
    model = CPU
    template_name = 'cpu.html'


class MemoryUsageView(ListView):
    model = Memory
    template_name = 'memory.html'


class DiskUsageView(ListView):
    model = Disk
    template_name = 'disk.html'

