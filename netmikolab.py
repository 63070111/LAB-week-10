from netmiko import ConnectHandler


def get_data_from_device(device_params):
    with ConnectHandler(**device_params) as ssh:
        result_shipinbr = ssh.send_command('sh ip int br')
        print(result_shipinbr)
        result_shipinbr = ssh.send_command('sh int description')
        print(result_shipinbr)
        result_shipinbr = ssh.send_command(
            'sh ip route vrf management | include ^C')
        print(result_shipinbr)
        result_shipinbr = ssh.send_command(
            'sh ip route vrf control-data | include ^C')
        print(result_shipinbr)


def get_ip(device_params, intf):
    data = get_data_from_device(device_params)
    result = data.strip().split('\n')
    for line in result[1:]:
        words = line.split()
        if words[0][0] == intf[0] and words[0][-3:] == intf[1:]:
            return words[1]


if __name__ == '__main__':
    device_ip = '172.31.112.4'
    username = 'admin'
    password = 'cisco'

    device_params = {'device_type': 'cisco_ios',
                     'ip': device_ip,
                     'uername': username,
                     'password': password,
                     }
    print(get_ip(device_params, 'G0/0'))
