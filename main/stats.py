import time

import psutil

from main.models import ServerStats

# CPU
CPU_CORES = psutil.cpu_count()

# BOOT TIME
BOOT_TIME = psutil.boot_time()


# NETWORK
def get_network_usage():
    net_stats = psutil.net_io_counters(pernic=False, nowrap=True)
    net_in_1 = net_stats.bytes_recv
    net_out_1 = net_stats.bytes_sent
    time.sleep(1)
    net_stats_new = psutil.net_io_counters(pernic=False, nowrap=True)
    net_in_2 = net_stats_new.bytes_recv
    net_out_2 = net_stats_new.bytes_sent

    net_in = net_in_2 - net_in_1
    net_out = net_out_2 - net_out_1

    return net_in, net_out


def get_stats() -> ServerStats:
    memory_info = psutil.virtual_memory()
    net_in, net_out = get_network_usage()
    disc_info = psutil.disk_usage('/')

    return ServerStats(
        cpu_cores=CPU_CORES,
        cpu_current_usage=psutil.cpu_percent(interval=0.1), # Usage at the moment
        cpu_average_usage=[x / CPU_CORES * 100 for x in psutil.getloadavg()][1], # For the last 5 minutes
        memory_total=memory_info.total,
        memory_percent_usage=memory_info.percent,
        disc_total=disc_info.total,
        disc_percent_usage=disc_info.percent,
        network_download_speed=net_in,
        network_upload_speed=net_out,
        boot_time=BOOT_TIME,
    )
