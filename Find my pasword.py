import os
import subprocess

def get_connected_wifi():
    try:
        result = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True)
        for line in result.splitlines():
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except Exception as e:
        print(f"Error retrieving Wi-Fi: {e}")
    return None

def get_wifi_password(ssid):
    try:
        result = subprocess.check_output(f"netsh wlan show profile name=\"{ssid}\" key=clear", shell=True, text=True)
        for line in result.splitlines():
            if "Key Content" in line:
                return line.split(":")[1].strip()
    except Exception as e:
        print(f"Error retrieving password: {e}")
    return None

def get_available_networks():
    try:
        result = subprocess.check_output("netsh wlan show networks", shell=True, text=True)
        return result
    except Exception as e:
        print(f"Error retrieving available networks: {e}")
    return None

def get_connected_devices():
    try:
        result = subprocess.check_output("arp -a", shell=True, text=True)
        return result
    except Exception as e:
        print(f"Error retrieving connected devices: {e}")
    return None

def main():
    while True:
        print("\n1. Show current WiFi")
        print("2. Show the password")
        print("3. Show connected devices")
        print("4. Finish")
        choice = input ( "Choose an option(1/2/3/4): ")

        if choice == "1":
            ssid = get_connected_wifi()
            if ssid:
                print(f"Connected to WiFi: {ssid}")
            else:
                print("No WiFi connected.")
        elif choice == "2":
            ssid = get_connected_wifi()
            if ssid:
                password = get_wifi_password(ssid)
                if password:
                    print(f"Password for {ssid}: {password}")
                else:
                    print("Password could not be retrieved.")
            else:
                print("No WiFi connected.")
        elif choice == "3":
            devices = get_connected_devices()
            if devices:
                print("Connected devices:")
                print(devices)
            else:
                print("No devices found.")
        elif choice == "4":
            print("Program is ended.")
            break
        else:
            print("Invalid selection. Please select 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()