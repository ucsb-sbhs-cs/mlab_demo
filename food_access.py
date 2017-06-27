#!/usr/bin/env python
# Process CORGIS food_access.json using Python

# Phill Conrad (UCSB) / Sky Adams (SBHS)
# 06/26/2017

import json

def get_county_list(filename='food_access.json'):
   with open(filename) as f:
      return json.loads(f.read())

def get_states_list(county_list):

    states = set()
    for county in county_list:
       states.add(county["State"])

    states_list = list(states)
    states_list.sort()
    return states_list

def get_counties_for_state(county_list, state):

    counties = []
    for county in county_list:
       if county["State"]==state:
           counties.append(county)

    counties.sort()
    return counties

def get_county_names_for_state(county_list, state):

    county_names = []
    for county in county_list:
       if county["State"]==state:
           county_names.append(county["County"])

    county_names.sort()
    return county_names


 
def main():
    county_list = get_county_list()
    states = get_states_list(county_list)
    print("states",states,"len(states)",len(states))
   
    CA_counties = get_counties_for_state(county_list,"CA")
    print("len(CA_counties)",len(CA_counties))

    CA_county_names = get_county_names_for_state(county_list,"CA")
    print("len(CA_county_names)",len(CA_county_names))
    print("CA_county_names",CA_county_names)

    DE_counties = get_counties_for_state(county_list,"DE")
    print("len(DE_counties)",len(DE_counties))

    DE_county_names = get_county_names_for_state(county_list,"DE")
    print("len(DE_county_names)",len(DE_county_names))
    print("DE_county_names",DE_county_names)
    
if __name__=="__main__":
    main()
