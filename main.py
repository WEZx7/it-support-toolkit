def system_information():
    print("\n--- System Information ---")
    print("System information module coming soon...")


def network_diagnostics():
    print("\n--- Network Diagnostics ---")
    print("Network diagnostics module coming soon...")


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
