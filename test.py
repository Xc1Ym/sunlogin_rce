a = {'nmap': {'command_line': 'nmap -oX - -p 40000-65535 -sV 192.168.151.130',
              'scaninfo': {'tcp': {'method': 'syn', 'services': '40000-65535'}},
              'scanstats': {'timestr': 'Thu Feb 17 10:45:19 2022', 'elapsed': '204.42', 'uphosts': '1',
                            'downhosts': '0', 'totalhosts': '1'}}, 'scan': {
    '192.168.151.130': {'hostnames': [{'name': '', 'type': ''}],
                        'addresses': {'ipv4': '192.168.151.130', 'mac': '00:0C:29:4D:32:D5'},
                        'vendor': {'00:0C:29:4D:32:D5': 'VMware'}, 'status': {'state': 'up', 'reason': 'arp-response'},
                        'tcp': {61561: {'state': 'open', 'reason': 'syn-ack', 'name': 'unknown', 'product': '',
                                        'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}}}

print(type(a))
b = list(a['scan']['192.168.151.130']['tcp'].keys())
print(type(b))
print('%s\t' % b[0])
# c = b['scan']
# print(type(c))
测试
