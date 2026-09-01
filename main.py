import platform


def system_information():
    print("\n--- System Information ---")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")


def network_diagnostics():
    import socket

    print("\n--- Network Diagnostics ---")

    hostname = socket.gethostname()
    print(f"Computer Name: {hostname}")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()

        print(f"Local IP Address: {local_ip}")
    except socket.error:
        print("Local IP Address: Unable to determine")

    print("\nTesting internet connection...")

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Internet Connection: Connected")
    except OSError:
        print("Internet Connection: Not Connected")

    try:
        dns_ip = socket.gethostbyname("google.com")
        print(f"DNS Resolution: Working ({dns_ip})")
    except socket.error:
        print("DNS Resolution: Failed")


def storage_information():
    import shutil

    print("\n--- Storage Information ---")

    total, used, free = shutil.disk_usage("/")

    gb = 1024 ** 3

    print(f"Total Storage: {total / gb:.2f} GB")
    print(f"Used Storage: {used / gb:.2f} GB")
    print(f"Free Storage: {free / gb:.2f} GB")

    usage_percent = (used / total) * 100
    print(f"Storage Usage: {usage_percent:.1f}%")

def memory_information():
    import os

    print("\n--- Memory Information ---")

    try:
        with open("/proc/meminfo", "r") as file:
            memory_data = file.readlines()

        mem_total = 0
        mem_available = 0

        for line in memory_data:
            if line.startswith("MemTotal:"):
                mem_total = int(line.split()[1])
            elif line.startswith("MemAvailable:"):
                mem_available = int(line.split()[1])

        mem_used = mem_total - mem_available

        total_gb = mem_total / 1024 / 1024
        used_gb = mem_used / 1024 / 1024
        available_gb = mem_available / 1024 / 1024

        usage_percent = (mem_used / mem_total) * 100

        print(f"Total Memory: {total_gb:.2f} GB")
        print(f"Used Memory: {used_gb:.2f} GB")
        print(f"Available Memory: {available_gb:.2f} GB")
        print(f"Memory Usage: {usage_percent:.1f}%")

    except Exception as error:
        print(f"Unable to read memory information: {error}")

def main():
    while True:
        print("\n================================")
        print("       IT SUPPORT TOOLKIT")
        print("================================")
        print("1. System Information")
        print("2. Network Diagnostics")
        print("3. Storage Information")
        print("4. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            system_information()
        elif choice == "2":
            network_diagnostics()
       elif choice == "3":
            storage_information()
       elif choice == "4":
            memory_information()
       elif choice == "5":
            print("\nExiting IT Support Toolkit...")
            break
        else:
            print("\nInvalid option. Please select 1-4.")


if __name__ == "__main__":
    main()
