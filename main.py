import platform


def system_information():
    print("\n--- System Information ---")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")


def network_diagnostics():
    import socket
    import subprocess

    print("\n--- Network Diagnostics ---")

    hostname = socket.gethostname()
    print(f"Computer Name: {hostname}")

    try:
        local_ip = socket.gethostbyname(hostname)
        print(f"Local IP Address: {local_ip}")
    except socket.error:
        print("Local IP Address: Unable to determine")

    print("\nTesting internet connection...")

    try:
        result = subprocess.run(
            ["ping", "-c", "1", "8.8.8.8"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("Internet Connection: Connected")
        else:
            print("Internet Connection: Not Connected")

    except Exception as error:
        print(f"Ping test failed: {error}")


def storage_information():
    print("\n--- Storage Information ---")
    print("Storage information module coming soon...")


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
            print("\nExiting IT Support Toolkit...")
            break
        else:
            print("\nInvalid option. Please select 1-4.")


if __name__ == "__main__":
    main()
