#! /usr/bin/env python3
import requests
import argparse
import os,sys
import pprint

def create_parse():
    parser = argparse.ArgumentParser(
        description='vultr control panel')
    parser.add_argument('list', help='list servers')
    parser.add_argument('kill', help='destroy server(s)' nargs='+')
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

def kill(apikey,target):
    url = 'https://api.vultr.com/v1/server/destroy'
    headers = {'API-Key': apikey}
    r = requests.post(url, headers=headers, data={'SUBID':target})
    print(r.status_code)

def start():
    parser = create_parse()
    args = parser.parse_args()
    try:
        apikey = os.environ["VULTRAPI"]
    except KeyError:
        print('Must set VULTRAPI key enviroment variable.')
        sys.exit(1)
    if (
    if (command == 'sl' or command == 'serverlist'):
        serverlist(apikey)
    elif (command == 'kill'):
        kill(apikey,target)

    else:
        print('Command not recognized.')

if __name__ == '__main__':
    start()

