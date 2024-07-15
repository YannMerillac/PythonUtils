import psutil
import time
import sys
import subprocess

def monitor_process(command: str, time_interval=1):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    pid = process.pid
    
    cpu_history = []
    memory_history = []

    while True:
        p = psutil.Process(pid)
        cpu_percent = p.cpu_percent()
        memory_usage = p.memory_info()[1]
        
        for child in p.children():
            memory_usage += child.memory_info()[1]
            cpu_percent += child.cpu_percent()

        memory_usage_gb = round(memory_usage / 1024 ** 3, 2)
        print(f"**** cpu: {cpu_percent:.2f} %, memory: {memory_usage_gb}")

        if not p.is_running():
            break

        time.sleep(time_interval)
        print(p)
        print(p.is_running())

    print("Done")

if __name__ == "__main__":
    command = " ".join(sys.argv[1:])
    print(f"Starting monitoring of : {command}")
    monitor_process(command)

            
