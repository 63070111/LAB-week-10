import re
from netmiko import ConnectHandler


def get_data_from_device(device_params):
    with ConnectHandler(**device_params) as ssh:
        result_shipinbr = ssh.send_command('sh ip int br')
        print(result_shipinbr)

        result_intf_desc = ssh.send_command('sh int description')
        print(result_intf_desc)

        result_mgmt_vrf_route = ssh.send_command(
            'sh ip route vrf management | include ^C')
        print(result_mgmt_vrf_route)

        result_ctrl_data_vrf_route = ssh.send_command(
            'sh ip route vrf control-data | include ^C')
        print(result_ctrl_data_vrf_route)


def get_ip(device_params, intf):
    with ConnectHandler(**device_params) as ssh:
        result_intf = ssh.send_command(f'show ip interface {intf}')
        match = re.search(r'Internet address is\s+([\d\.]+)', result_intf)
        if match:
            return match.group(1)


if __name__ == '__main__':
    device_ip = '172.31.112.4'
    username = 'admin'
    password = 'cisco'

    device_params = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': username,
        'password': password,
    }
    print(get_ip(device_params, 'G0/0'))
