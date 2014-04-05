#!/usr/bin/env python3
from urllib2 import urlopen
from json import load, dumps

def get_data():
    url = 'https://personnel.mariposaltd.com/api/map/cities'

    response = urlopen(url)
    json_obj = load(response)
    return json_obj

def print_raw_data(data):
    f = open('adjuster-data.json', 'w')
    f.write(dumps(data, indent=4))
    f.close()

def main():

    raw_data = get_data()
    print_raw_data(raw_data)


if __name__ == '__main__':
    main()