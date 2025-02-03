import psutil
import logging

# Set thresholds
CPU_THRESHOLD = 80  # 80%
MEMORY_THRESHOLD = 80  # 80%
DISK_THRESHOLD = 80  # 80%

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.WARNING, format='%(asctime)s - %(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage: {cpu_usage}%")

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High disk usage: {disk_usage}%")

def check_running_processes():
    processes = len(psutil.pids())
    logging.info(f"Number of running processes: {processes}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()