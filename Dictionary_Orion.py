#!/usr/bin/python3
'''
    Author: Khang Tran
    Date: September 4, 2020

    Parameters: 
    yamlFile: Please replace current param with the actual location of yaml file
    jsonFile: Please replace current location of where the json file is stored

    What I want to do is create a for loop that iterates through yaml file and checks key length (8 Characters CLLI)
    if yes --> streamline to JSON dump
    if no --> disregard
'''

import yaml
import json
import sys

yamlFile = "C:/Users/T944589/Documents/TNI/TNI-Website/YAML_Python_Dictionary/clli_out.yaml"
jsonFile = "C:/Users/T944589/Documents/TNI/TNI-Website/YAML_Python_Dictionary/sample_json.json"
delete_clliList = []


'''
    Function: parse_through_dict()
    Purpose: This function will recursively iterate and parse through the nested dictionary to get key "CLLI"
             - Once I iterate through list --> Remove from buildings CLLI that are longer than 8 chars
'''
def parse_through_dict(yaml_dict):
    # First going to iterate through yaml_dict keys via Province Code (ie. AB, BC)
    for provCode in yaml_dict.keys():
        # Then going to iterate through the City Code within the matched Province Code (Nested Dictionary)
        for cityCode in yaml_dict[provCode].keys():
            # Now that we are in the nested dict of Province --> City, want to iterate through building code nested in matched provCode-->cityCode
            for buildingCode in yaml_dict[provCode][cityCode].keys():
                # Condition to check for CLLI that are over 8 chars
                if (len(buildingCode) > 8):
                    # will append matched keys within nested dictionary Province --> City --> Building to temp list
                    delete_clliList.append({'provCode' : provCode, 'cityCode' : cityCode, 'buildingCode' : buildingCode})
    
    # This will iterate through the delete_clliList list and match nested key elements based on Province Code-->City Code-->Building Code
    for item in delete_clliList:
        if type(yaml_dict[item["provCode"]][item["cityCode"]][item["buildingCode"]]) is dict:
            del yaml_dict[item["provCode"]][item["cityCode"]][item["buildingCode"]]
    
    # Going to write the new yaml_dict in json file
    with open(jsonFile,"w", newline='\n') as json_file:
        
        # json.dump() streamlines dict object and writes it into json file 
        # indent=2 allows you to add new lines (Adds each dictionary entry onto a new line)
        json.dump(yaml_dict, json_file, indent=2)

    '''
    *********** DO NOT DELETE -- RECURSION ***********
    for key, value in yaml_dict.items():
        with open(jsonFile,"w", newline='\n') as json_file:
            # this is where recursion happens --> get's called repetitively if value of each item in directory is dict directory itself
            if (type(value) is dict):
                # here we are printing out all the keys in the current nested dictionary
                if (len(key) <= 8):
                    print ("Key: " + key)
                    parse_through_dict(value)
            else:
                #print(key + ":" + value)
                output = key + ":" + value
                print(output)
            #json.dump(new_dict, json_file, indent=2)
    *********** DO NOT DELETE -- RECURSION ***********
    '''


'''
    Function: convert()
    Purpose: Main Function that will read in CLLI YAML file and call on parse_through_dict()
'''
def convert():
    with open(yamlFile, 'r') as yaml_file:
        try:
            print("******* Operation Beginning *******") 

            yaml_data = yaml.safe_load(yaml_file) # yaml_data parses the yaml file as a stream and outputs into python dict
            parse_through_dict(yaml_data)

            print("******* Operation Completed *******") 
        except yaml.YAMLError as error:
            print(error)

convert()