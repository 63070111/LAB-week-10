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

        ssh.send("conf\n")
        ssh.send("no ip ssh server authentication user password\n")
        ssh.send("no ip ssh server authentication user keyboard\n")
        time.sleep(2)
        result = ssh.recv(1000).decode('ascii')
        print(result)
