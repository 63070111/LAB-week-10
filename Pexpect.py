import pexpect

PROMPT = '#'
USERNAME = 'admin'
PASSWORD = 'cisco'
COMMAND = "conf"
COMMAND1 = 'int loopback 0'
device_ip = ["172.31.112.4", "172.31.112.5", "172.31.112.6"]

for i in device_ip:
    num = 1
    child = pexpect.spawn('telnet' + device_ip)
    child.expect('Username')
    child.sendline(USERNAME)
    child.expect('Password')
    child.sendline(PASSWORD)
    child.expect(PROMPT)
    child.sendline(COMMAND1)
    child.expect(PROMPT)
    child.sendline(COMMAND)
    child.expect(PROMPT)
    child.sendline("ip add" + num.num.num.num + "255.255.255.255")
    result = child.insertBefore
    print(result)
    num += 1
    print()
    print(result.decode('UTF-8'))
    child.sendline('exit')
    
