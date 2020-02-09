#! /usr/bin/env python3
import requests
import argparse
import os,sys

apikey = ''

def create_parse():
    parser = argparse.ArgumentParser(
        description='vultr control panel')
    parser.add_argument('command', help='action to perform')
    parser.add_argument('target', help='server(s)', nargs='*')
    return parser

def serverlist():
    url = 'https://api.vultr.com/v1/server/list'
    r = s.get(url)
    status = r.status_code
    if (status != 200):
        print(status)
        print(url,headers)
        r.raise_for_status()
    return r.json()

def printstatus(statuswanted):
    list = serverlist()
    for i in list.keys():
        if (statuswanted == 'ALL' or list[i]['status'] == statuswanted):
            print('ID: {}'.format(list[i]['SUBID']))
            print('Name: {}'.format(list[i]['label']))
            print('Start: {}'.format(list[i]['date_created']))
            print('Status: {}'.format(list[i]['status']))
            print('Datacenter: {} ({})'.format(list[i]['DCID'],list[i]['location']))
            print('OS: {}'.format(list[i]['os']))
            print('RAM: {}'.format(list[i]['ram']))
            print('Main IP: {}\n'.format(list[i]['main_ip']))

def planlist():
    url = 'https://api.vultr.com/v1/plans/list'
    r = s.get(url)
    status = r.status_code
    if (status != 200):
        print(status)
        print(url,headers)
        r.raise_for_status()
    return r.json()

def printallplans():
    list=planlist()
    for i in list:
        print('ID: {}'.format(list[i]['VPSPLANID']))
        print('Name: {}'.format(list[i]['name']))
        print('Price per month: {}'.format(list[i]['price_per_month']))
        print('Plan type: {}'.format(list[i]['plan_type']))
        print('Locations: ',end='')
        if (len(list[i]['available_locations']) == 0):
            print('NONE')
        else:
            regions=regionlist()
            for j in list[i]['available_locations']:
                dc=str(j)
                print('{}[{}] '.format(regions[dc]['name'],dc),end='')
            print()
        print()

def printplans():
    list=planlist()
    for i in list:
        if (len(list[i]['available_locations']) > 0):
            print('ID: {}'.format(list[i]['VPSPLANID']))
            print('Name: {}'.format(list[i]['name']))
            print('Price per month: {}'.format(list[i]['price_per_month']))
            print('Plan type: {}'.format(list[i]['plan_type']))
            print('Locations: ',end='')
            regions=regionlist()
            for j in list[i]['available_locations']:
                dc=str(j)
                print('{}[{}] '.format(regions[dc]['name'],dc),end='')
            print()
        print()

def regionlist():
    url = 'https://api.vultr.com/v1/regions/list'
    r = s.get(url)
    status = r.status_code
    if (status != 200):
        print(url)
        print(status)
        r.raise_for_status()
    return r.json()

def kill(target):
    list = serverlist()
    count = 0
    for i in target:
        try:
            x = list[i]['SUBID'] 
            url = 'https://api.vultr.com/v1/server/destroy'
            r = s.post(url, data={'SUBID':x})
            status=r.status_code
            if (status == 200):
                print('{} destroyed.'.format(i))
                count = count + 1
            else:
                print('Status returned: {}'.format(status))
                print(url,'SUBID:',x)
                r.raise_for_status()
        except KeyError:
            next
    print('{} server(s) destroyed.'.format(count))

def status(target):
    for i in target:
        url = 'https://api.vultr.com/v1/server/list'
        payload = ({'SUBID': i})
        r = s.get(url, params=payload)
        status = r.status_code
        if (status != 200):
            print(status)
            print(url,headers)
            r.raise_for_status()
        x = r.json()
        for j in x:
            print(j,': ',x[j])
        print()

def create(target):
    url = 'https://api.vultr.com/v1/server/create'
    datacenter = target[0]
    vpsplan = target[1]
    osid = target[2]
    pvtnet = target[3] == '1'
    sshkey = target[4]
    firewall = target[5]
    hostname = target[6]
    tags = target[7:]

    print('Requested:\nDatacenter: {}\nPlan: {}\nOS: {}'.format(datacenter,vpsplan,osid))
    print('PrivateNetworking: {}\nSSHkey: {}\nFirewall: {}'.format(pvtnet,sshkey,firewall))
    print('Hostname: {}\nTags: {}'.format(hostname,tags))
    return

def copy(target):
    for i in target:
        url = 'https://api.vultr.com/v1/server/list'
        payload = ({'SUBID': i})
        r = s.get(url, params=payload)
        status = r.status_code
        if (status != 200):
            print(status)
            print(url,headers)
            r.raise_for_status()
        existing = r.json()
        datacenter = existing['DCID']
        vpsplan = existing['VPSPLANID']
        osid = existing['OSID']
        pvtnet = 
        sshkey = 
        firewall = existing['FIREWALLGROUPID']
        tags = existing['tag']

def printoslist():
    return

def printfwlist():
    return

def printsshlist():
    return

def start():
    parser = create_parse()
    args = parser.parse_args()
    try:
        apikey = os.environ["VULTRAPI"]
    except KeyError:
        print('Must set VULTRAPI key enviroment variable.')
        sys.exit(1)
    command=args.command
#    print(command)
    if command == 'list':
        target=args.target[0]
#        print(target)
        if (target == 'server' or target == 'servers'):
            printstatus('ALL')
        if (target == 'plans'):
            printplans()
        if (target == 'allplans'):
            printallplans()
        if (target == 'active' or target == 'pending' or target == 'suspended' or target == 'closed'):
            printstatus(target)
        if (target == 'os'):
            printoslist()
        if (target == 'ssh'):
            printsshlist()
        if (target == 'fw'):
            printfwlist()
    elif (command == 'ls'):
        printstatus('ALL')
    elif (command == 'status'):
        status(args.target)
    elif (command == 'kill'):
        kill(args.target)
    elif (command == 'create'):
        create(args.target)
    elif (command == 'copy'):
        copy(args.target)
    else:
        print('Command {} not recognized.'.format(command))
        sys.exit(1)

try:
    apikey = os.environ["VULTRAPI"]
except KeyError:
    print('Must set VULTRAPI key enviroment variable.')
    sys.exit(1)

s = requests.Session()
s.headers.update({'API-Key': apikey})

if __name__ == '__main__':
    start()

