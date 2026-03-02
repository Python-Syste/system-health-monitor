import psutil
import time

def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        print(f"CPU: {cpu}% | Memory: {memory}%")
        time.sleep(5)

if __name__ == "__main__":
    monitor()
