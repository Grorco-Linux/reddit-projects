import subprocess
import pprint


def notify(x):
    subprocess.call(['notify-send', x])


def device_scan(devices={}, firstrun=True, iteration=1):


    bashCommand = "sudo ./lclnmap.sh"
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    maclist = list(devices.keys())

    for line in output.splitlines():
        line = str(line).lstrip("b'").rstrip("'")
        if line.startswith('MAC'):
            macaddress = line.split()[2]
            name = ''.join(line.split()[3:])
            try:
                while True:
                    maclist.remove(macaddress)
            except ValueError:
                pass

            if macaddress not in devices.keys():
                if not firstrun:
                    notify('A new Mac Address: {} Named: {} has connected at IP addresss: {}'.format(macaddress,
                                                                                                 name, ipadd))
                devices.update({macaddress: {'Name': name, 'IP': [ipadd]}})
            else:
                if ipadd not in devices[macaddress]['IP']:
                    devices[macaddress]['IP'].append(ipadd)
        if line.startswith('Nmap scan'):
            ipadd = line.split()[-1]

        if line.startswith('Nmap done:'):
            finished = line



    for mac in maclist:
        notify('{} has left the network'.format(mac))
        devices.pop(mac)
    subprocess.call(['clear'])
    pprint.pprint(devices, width=120)
    print(line)
    print(iteration)
    device_scan(devices, firstrun=False, iteration=iteration+1)


if __name__ == "__main__":

    device_scan()

