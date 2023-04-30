import time
import paramiko

username = 'admin'
password = 'cisco'

devices_ip = ["172.31.112.4", "172.31.112.5", "172.31.112.6"]
for ip in devices_ip:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=username,
                   password=password, look_for_keys=False)
    print("Connecting to {} ...".format(ip))
    with client.invoke_shell() as ssh:
        print("Connected to {} ...".format(ip))

        ssh.send("terminal lenght 0\n")
        time.sleep(1)
        result = ssh.recv(1000).decode('ascii')
        print(result)
        if ip == 0:
            ssh.send("conf\n")
            ssh.send("router ospf 1\n")
            ssh.send("network 172.31.112.0 0.0.0.0 area 0\n")
            ssh.send("network 172.31.112.16 0.0.0.0 area 0\n")
            ssh.send("network 172.31.112.32 0.0.0.0 area 0\n")
        elif ip == 1:
            ssh.send("conf\n")
            ssh.send("router ospf 1\n")
            ssh.send("network 172.31.112.0 0.0.0.0 area 0\n")
            ssh.send("network 172.31.112.32 0.0.0.0 area 0\n")
            ssh.send("network 172.31.112.48 0.0.0.0 area 0\n")
        elif ip == 2:
            ssh.send("conf\n")
            ssh.send("int g0/2\n")
            ssh.send("ip address 192.168.122.28 255.255.255.0\n")
            ssh.send("no sh\n")
            ssh.send("exit\n")
            ssh.send("router ospf 1\n")
            ssh.send("network 172.31.112.0 0.0.0.0 area 0\n")
            ssh.send("network 172.31.112.48 0.0.0.0 area 0\n")
            ssh.send("network 172.31.122.0 0.0.0.0 area 0\n")
            ssh.send("exit\n")
            ssh.send("ip route 0.0.0.0 0.0.0.0 172.31.112.1\n")
            ssh.send("access-list 99 permit 172.31.112.4 0.0.0.0\n")
            ssh.send("access-list 99 permit 172.31.112.5 0.0.0.0\n")
            ssh.send("access-list 99 permit 172.31.112.6 0.0.0.0\n")
            ssh.send("access-list 99 deny any\n")
            ssh.send("ip nat pool all 172.31.122.28 172.31.122.28 255.255.255.0\n")
            ssh.send("int g0/0\n")
            ssh.send("ip nat inside\n")
            ssh.send("int g0/1\n")
            ssh.send("ip nat inside\n")
            ssh.send("ip nat inside source list 99 pool all overload\n")
            ssh.send("exit\n")
            ssh.send("int g0/2\n")
            ssh.send("ip nat outside\n")
            ssh.send("exit\n")
        time.sleep(2)
        result = ssh.recv(1000).decode('ascii')
        print(result)
        
