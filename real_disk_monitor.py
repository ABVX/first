def tire():
    print("=" * 40)

import shutil
import psutil

disk = shutil.disk_usage("/")
d_total = disk.total
d_used = disk.used
d_free = disk.free

d_total_gb = d_total / (1024 ** 3)
d_used_gb = d_used / (1024 ** 3)
d_free_gb = d_free / (1024 ** 3)
d_percent = d_used / d_total * 100

tire()
print("DISK MONITOR")
tire()
print(f"Total: {d_total_gb:.2f} GB")
tire()
print(f"Used: {d_used_gb:.2f} GB")
tire()
print(f"Free: {d_free_gb:.2f} GB")
tire()

if d_percent >= 90:
    d_status = "Critical low!!!"
elif d_percent >= 60:
    d_status = "Medium"
else:
    d_status = "Normal"

print(f"Usage: {d_percent:.1f}% - {d_status} space")

tire()
ram = psutil.virtual_memory()
print(f"RAM configuration: {ram}")
tire()

cpu_use = psutil.cpu_percent()
print(f"CPU usage: {cpu_use}")
tire()
cpu_count = psutil.cpu_count()
print(f"Number of CPU cores: {cpu_count}")
tire()
cpu_time = psutil.cpu_times()
print(f"CPU work time: :{cpu_time}")
tire()

net_counters = psutil.net_io_counters()
print(f"Connections counters: {psutil.net_io_counters}")
net_count = psutil.net_connections()
print(f"Connections count: {psutil.net_connections}")
tire()

processes = psutil.process_iter()
print(f"All proceses: {psutil.process_iter}")
tire()

boot_time = psutil.boot_time()
print(f"Boot time: {psutil.boot_time}")
tire()

users = psutil.users()
print(f"Users: {psutil.users}")
tire()

temps = psutil.sensors_temperatures()
print(f"Temperatures: {psutil.sensors_temperatures}")
tire()