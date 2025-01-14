import os
import time
import platform

def clear_screen():
    system = platform.system().lower()
    if system == 'windows':
        os.system('cls')  # Untuk Windows
    else:
        os.system('clear')  # Untuk Linux/macOS

def print_ky_logo():
    logo = """ 
     ⠀⠀⠀⢀⣠⡄⠀⠀⣴⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⡿⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⠁⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⠏⠀⠀⠾⠿⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⡏⠀⠀⣤⣤⠀⠀⢸⣿⡿⠀⠀⢠⣤⡄⠀⠀⣿⣷⠀
⢠⣿⣿⣿⣿⡿⠁⠀⢰⣿⠏⠀⢀⣾⣿⠃⠀⢀⣿⡿⠁⠀⣰⣿⣿⡄
⢸⣿⣿⣿⣿⠃⠀⢀⣿⡿⠀⠀⣸⣿⠇⠀⠀⣾⣿⠃⠀⢰⣿⣿⣿⡇
⠘⣿⣿⣿⠇⠀⠀⣾⣿⠁⠀⢰⣿⡟⠀⠀⣰⣿⠇⠀⢀⣾⣿⣿⣿⠃
⠀⢿⣿⡟⠀⠀⣸⣿⠃⠀⢠⣿⡿⠁⠀⠀⠛⠛⠀⠀⣼⣿⣿⣿⡿⠀
⠀⠈⢿⣶⣶⣶⣿⣿⣶⣶⣾⣿⠇⠀⢠⣶⣶⣶⣶⣾⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⡿⠀⠀⣸⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠁⠀⠰⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀
       author devil 
================================
"""
    print(logo)

def run_command(command):
    try:
        result = os.popen(command).read()
        return result.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def get_memory_info():
    system = platform.system().lower()
    
    if system == 'windows':
        # Menggunakan perintah Windows untuk mendapatkan informasi memori
        command = "wmic memorychip get capacity"
        result = run_command(command)
        if result:
            # Mengambil nilai pertama (total memori dalam byte) dan mengonversinya ke MB
            mem_total = int(result.splitlines()[1]) // (1024 * 1024)  # Convert byte to MB
            return mem_total, mem_total  # Pada Windows, kita hanya akan memperkirakan memori yang tersedia
        else:
            return 0, 0  # Tidak dapat mendapatkan informasi memori
    else:
        # Menggunakan perintah Linux untuk mendapatkan informasi memori
        mem_total = int(run_command("grep MemTotal /proc/meminfo | awk '{print $2}'"))
        mem_available = int(run_command("grep MemAvailable /proc/meminfo | awk '{print $2}'"))
        return mem_total // 1024, mem_available // 1024  # Mengonversi dari KB ke MB

def main():
    clear_screen()
    print_ky_logo()
    
    print("Konfigurasi jaringan:")
    print(run_command("ifconfig"))
    time.sleep(2)  # Memberikan jeda 2 detik
    print("\nMerek HP Anda:")
    brand = run_command("getprop ro.product.brand")
    model = run_command("getprop ro.product.model")
    print(f"Brand: {brand}")
    print(f"Model: {model}")
    
    # Mendapatkan informasi RAM
    mem_total_mb, mem_available_mb = get_memory_info()
    
    print(f"\nTotal Memori: {mem_total_mb} MB")
    print(f"Memori Tersedia: {mem_available_mb} MB")

if __name__ == "__main__":
    main()
