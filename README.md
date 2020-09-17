# Yaml_to_JSON_Converter

Overview:
This script will parse a YAML file and convert it into a structured JSON file. 

Parameters: 
  (yamlFile) : Please replace current param with the actual location of yaml file. 
  (jsonFile): Please replace current location of where the json file will be stored
 
State Overview:
  1. The YAML file will first be converted into a Python Nested Dictionary
  2. The function parse_through_dict() takes in the nested dictionary
    a) First For Loop --> Going to iterate through yaml_dict keys via Province Code (ie. AB, BC)
    b) Second For Loop --> Going to iterate through the City Code within the matched Province Code (Nested Dictionary) 
    c) Third For Loop --> Now that we are in the nested dict of Province --> City, want to iterate through building code nested in matched provCode-->cityCode
    d) If Condition --> Condition to check for CLLI that are over 8 chars
       Yes) Append to seperate declared list[]
       No) Continue Dictionary Iteration
    e) For Loop will iterate through the delete_clliList list and match nested key elements based on Province Code-->City Code-->Building Code
       Once there's a match, will delete element from dictionary
    f) Write to JSON
  


