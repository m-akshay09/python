import socket
from IPy import IP


def scan(target,port_num):
    convert_ip=check_ip(target)
    print('\n'+'[-_0] Scanning target: '+str(target))
    for port in range(1,port_num):
        scan_port(convert_ip,port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
    
def scan_port(ipaddr,port):
    try:
        sock=socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddr,port)) 
        
        try:
            banner = sock.recv(1024)
            print('[+] port '+str(port)+' is open')
            print('[*] Banner Info: '+str(banner.decode().strip('\n').strip('\r')))
        except:
             print('[+] port '+str(port)+' is open')
    except:
        pass
        
targets=input('[+] Enter Target/s  To Scan(split multiple targets with ,): ')
port_num=int(input("[+] Enter Number Of Ports You Want To Scan: "))
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '),port_num) 
else:
    scan(targets,port_num)
 

 