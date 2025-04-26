from datetime import datetime
import pyfiglet
import socket
import sys

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

if(len(sys.argv)>1):
    target_address = sys.argv[1]

    try:
        target_ip = socket.gethostbyname(target_address)
        
        try:
            target_info = socket.gethostbyaddr(target_ip)
            target_name = target_info[0]
            print(f"Target hostname: {target_name}")
        
        except socket.herror:
            target_name = "Unkown"
    
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

else:
    print("Invalid number of arguments")
    sys.exit()


print("*" * 50)
print(f"Scanning target: {target_address}-{target_ip} ")
print(f"Starting time: {datetime.now()}")
print("*" * 50)

try:
    for port in range(1, 65_535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
                print(f"Port {port} is open - {service}")
            except:
                print(f"Port {port} is open")
    s.close()

except KeyboardInterrupt:
    print("\nScan terminated by user")
    sys.exit()

except socket.error:
    print("Error while connecting to server")
    sys.exit()

except Exception as e:
    print("Something went wrong: ", e)
    sys.exit()