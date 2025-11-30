def tire():
    print("=" * 40)

def fs(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

def fb(bytes_value):
    units = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while bytes_value >= 1024 and i < len(units) - 1:
        bytes_value /= 1024.0
        i += 1
    return f"{bytes_value:.1f} {units[i]}"

import shutil
import psutil
import datetime

disk = shutil.disk_usage("/")
d_total = disk.total
d_used = disk.used
d_free = disk.free

d_total_gb = d_total / (1024 ** 3)
d_used_gb = d_used / (1024 ** 3)
d_free_gb = (d_total - d_used) / (1024**3)
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
ram_use = psutil.virtual_memory()
print(f"RAM: Total = {ram_use.total / (1024**3):.2f}GB, Used = {ram_use.used / (1024**3):.2f}GB, Free = {ram_use.free / (1024**3):.2f}GB, Usage = {ram_use.percent}%")
tire()

cpu_time = psutil.cpu_times()
print("CPU worktime: ")
print(f" - User: {fs(cpu_time.user)}")
print(f" - System: {fs(cpu_time.system)}")
print(f" - IDLE: {fs(cpu_time.idle)}")
tire()

print("Network counters: ")
net_stats = psutil.net_io_counters()

print(f" - Bytes sent: {fb(net_stats.bytes_sent)}")
print(f" - Bytes recv: {fb(net_stats.bytes_recv)}")
print(f" - Packet sent: {fb(net_stats.packets_sent)}")
print(f" - Packet recv: {fb(net_stats.packets_recv)}")
print(f" - Droping packet: {net_stats.dropin}")
tire()

processes = psutil.process_iter(["name", "cpu_percent", "memory_percent"])
print(f"5 active processes: ")
sorted_processes = sorted(
    processes,
    key=lambda p: p.info["cpu_percent"],
)
for p in sorted_processes[:5]:
    try:
        proc_name = p.info.get("name", "N/A")
        cpu = p.info.get("cpu_percent", 0.0)
        mem = p.info.get("memory_percent", 0.0)

        print(f" - {proc_name[:20]:<20} | CPU: {cpu:.1f}% | RAM: {mem:.1f}%")
    except (psutil.noSuchProcess, psutil.AcessDenied):

        continue

tire()

boot_time = psutil.boot_time()
boot_time_u = datetime.datetime.fromtimestamp(boot_time).strftime("%d.%m.%Y %H:%M:%S")
print(f"Boot time: {boot_time_u}")
tire()

unique_users = set()
print(f"Active users:")
for user in psutil.users():
    if user.name in unique_users:
        continue
    try:
        session_start = datetime.datetime.fromtimestamp(user.started).strftime("%d.%m.%Y %H:%M:%S")

        print(f" - user: {user.name:<10}")
        print(f" - terminal/host: {user.terminal} @ {user.host}")
        print(f" - session start: {session_start}")
        print(f" - user PID: {user.pid}")

        unique_users.add(user.name)

    except ValueError:
        print(f" - User: {user.name} (Time error)")

tire()

temps = psutil.sensors_temperatures()
print(f"Temperatures: {psutil.sensors_temperatures()}")
if not temps:
    print("Can`t display temperatures data")
tire()