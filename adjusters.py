#!/usr/bin/env python3
from urllib2 import urlopen
from json import load, dumps

# Get the Mariposa data in JSON format (city, state, and number of adjusters)
def get_data():
    url = 'https://personnel.mariposaltd.com/api/map/cities'

    response = urlopen(url)
    json_obj = load(response)
    return json_obj

# Write raw adjuster data to a file called adjuster-data.json
def print_raw_data(data):
    f = open('adjuster-data.json', 'w')
    f.write(dumps(data, indent=4))
    f.close()

# Convert JSON data to a list and sort by number of adjusters (high to low)
def convert_json_and_sort(data):
    city_list = []
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 
          'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
          'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
          'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    
    # Create the city list array and get the geodata
    for location in data:
        if location['state'] in states:
            city = location['city'].title().decode('string_escape')
            state = location['state']
            location = location['number']
            city_list.append([city, state, location])

            # Now that we have the city and state, go get latitude and longitude
            # This currently just prints xml to the console, but it's a good start
            get_geodata(city.replace(' ', '%20'), state)

        # Reverse sort the list by number of adjusters    
        city_list.sort(key=lambda x: x[2], reverse=True)

        f = open('cities.csv', 'w')
        f.write('city,state,num,lon,lat\n')
        for item in city_list:
            f.write(item[0] + ',' + item[1] + ',' + str(item[2]) + '\n')
        f.close()
        
# Get geodata and add to list
def get_geodata(city, state):
    url = 'http://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderWebServiceHttpNonParsed_V04_01.aspx?city=' + city + '&state=' + state + '&apikey=demo&format=XML&census=false&notStore=false&version=4.01'
    response = urlopen(url)
    output = response.read()
    print(output)
    # xml_data = open('xml_response.xml', 'w')
    # xml_data.write(output)
    # xml_data.close()

# The main function that makes it all happen
def main():
    raw_data = get_data()
    convert_json_and_sort(raw_data)
    print_raw_data(raw_data)

    # get_geodata()


if __name__ == '__main__':
    main()