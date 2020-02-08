#! /usr/bin/env python3
import requests
import argparse
import os,sys
import pprint

def create_parse():
    parser = argparse.ArgumentParser(
        description='vultr control panel')
    parser.add_argument('command', help='command to execute')
    return parser

def serverlist(apikey):
    url = 'https://api.vultr.com/v1/server/list'
    headers = {'API-Key': apikey}
    print('{} {}'.format(url,headers))
    response = requests.get(url, headers=headers)
    pprint.pprint(response.json())

def start():
    parser = create_parse()
    args = parser.parse_args()
    command = args.command
    try:
        apikey = os.environ["VULTRAPI"]
        print(apikey)
    except KeyError:
        print('Must set VULTRAPI key enviroment variable.')
        sys.exit(1)
    if command == 'sl':
        print('got sl command')
        serverlist(apikey)

if __name__ == '__main__':
    start()

