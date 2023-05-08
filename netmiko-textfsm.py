import textfsm
from netmiko import ConnectHandler

def get_data_from_device(device_params):
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_command('show interfaces')
        template_file_here = "path/to/your/TextFSM_template_file"
        with open(template_file_here) as f:
            fsm = textfsm.TextFSM(f)
            result = fsm.ParseText(result)
            headers = fsm.header
        return [headers] + result

if __name__ == '__main__':
    device_ip = '172.31.112.4'
    username = 'admin'
    password = 'cisco'

    device_params = {'device_type': 'cisco_ios',
                     'ip': device_ip,
                     'username': username,
                     'password': password,
                     }

    data = get_data_from_device(device_params)
    for row in data:
        print(row)
