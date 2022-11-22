from netmiko import ConnectHandler
 
#First create the device object using a dictionary
with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
 
# Next establish the SSH connection
        net_connect = ConnectHandler(**Router)
        print('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()

