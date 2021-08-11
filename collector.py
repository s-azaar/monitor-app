import requests
import json
import subprocess

base_url = 'http://127.0.0.1:8000/collect/'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
cpu_body = {'cpu_utilization': None, 'timestamp': None}
disk_body = {'free': None, 'used': None, 'timestamp': None}
memory_body = {'free': None, 'used': None, 'timestamp': None}
sub_urls = ['cpu-usages/', 'memory-usages/', 'disk-usages/']
data = None

for url in sub_urls:
    if url.startswith('cpu'):
        cpu_usages = subprocess.getoutput("cpu=$(mpstat  | tail -1 | awk '{print $4}') && echo $cpu")
        timestamp = subprocess.getoutput("date")
        cpu_body['cpu_utilization'] = cpu_usages+'%'
        cpu_body['timestamp'] = timestamp
        data = json.dumps(cpu_body)
    elif url.startswith('mem'):
        free_mem = subprocess.getoutput("free_mem=$(free | sed -n '2'p | awk '{print $4}') && echo $free_mem")
        used_mem = subprocess.getoutput("used_mem=$(free | sed -n '2'p | awk '{print $3}') && echo $used_mem")
        timestamp = subprocess.getoutput("date")
        memory_body['free'] = free_mem+' MB'
        memory_body['used'] = used_mem+' MB'
        memory_body['timestamp'] = timestamp
        data = json.dumps(memory_body)
    elif url.startswith('disk'):
        free_disk = subprocess.getoutput("disk_used=$(df --total | tail -1 | awk '{print $3}') && echo $disk_used")
        used_disk = subprocess.getoutput("disk_free=$(df --total | tail -1 | awk '{print $4}') && echo $disk_free")
        timestamp = subprocess.getoutput("date")
        disk_body['free'] = free_disk+' MB'
        disk_body['used'] = used_disk+' MB'
        disk_body['timestamp'] = timestamp
        data = json.dumps(disk_body)
    requests.post(base_url+url, data=data, headers=headers)

