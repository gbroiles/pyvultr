#! /usr/bin/env python3
import requests
import argparse
import os,sys
import pprint

def create_parse():
    parser = argparse.ArgumentParser(
        description='vultr control panel')
    parser.add_argument('command', help='action to perform')
    parser.add_argument('target', help='server(s)', nargs='*')
    return parser

def serverlist(apikey):
    url = 'https://api.vultr.com/v1/server/list'
    headers = {'API-Key': apikey}
    r = requests.get(url, headers=headers)
    list = r.json()
    for i in list.keys():
        print('ID: {}'.format(list[i]['SUBID']))
        print('Name: {}'.format(list[i]['label']))
        print('Start: {}'.format(list[i]['date_created']))
        print('Datacenter: {} ({})'.format(list[i]['DCID'],list[i]['location']))
        print('OS: {}'.format(list[i]['os']))
        print('RAM: {}'.format(list[i]['ram']))
        print('Main IP: {}'.format(list[i]['main_ip']))
        print('\n')
    return list

def kill(apikey,target):
    list = serverlist(apikey)
    for i in target:
        if list[i]['SuBID'] == i:
            url = 'https://api.vultr.com/v1/server/destroy'
            headers = {'API-Key': apikey}
            r = requests.post(url, headers=headers, data={'SUBID':i})
            status=r.status_code
            if (status == 200):
                print('{} destroyed.'.format(i))
            else:
                print('Status returned: {}'.format(status))
        else:
            print('Server {} not found'.format(i))

def start():
    parser = create_parse()
    args = parser.parse_args()
    try:
        apikey = os.environ["VULTRAPI"]
    except KeyError:
        print('Must set VULTRAPI key enviroment variable.')
        sys.exit(1)
    command=args.command
    target=args.target
    if (command == 'sl' or command == 'serverlist'):
        serverlist(apikey)
    elif (command == 'kill'):
        kill(apikey,target)
    else:
        print('Command not recognized.')

if __name__ == '__main__':
    start()

