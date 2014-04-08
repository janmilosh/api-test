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

# def convert_json_to_list(json_obj):
#     for location in json_obj:
#         print location.city

def get_geodata():
    url = 'http://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderWebServiceHttpNonParsed_V04_01.aspx?streetAddress=9355%20Burton%20Way&city=Beverly%20Hills&state=ca&zip=90210&apikey=demo&format=XML&census=false&notStore=false&version=4.01'
    response = urlopen(url)
    output = response.read()
    xml_data = open('xml_response.xml', 'w')
    xml_data.write(output)
    xml_data.close()

def create_csv_file(data):
    f = open('cities.csv', 'w')
    f.write('city,state,num,lon,lat')
    for location in data:
        print location['city'] + ',' + location['state'] + ',' + str(location['number'])
    f.close()

def main():
    raw_data = get_data()
    print_raw_data(raw_data)
    create_csv_file(raw_data)
    get_geodata()


if __name__ == '__main__':
    main()