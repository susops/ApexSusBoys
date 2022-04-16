import json
import pandas as pd
import logging

class ApexData:
    def __init__(self, user_data, file_name):
        self.pretty_data = self.format_data(user_data)
        self.file_name = file_name
        
    def format_data(self, user_data):
        loaded_data = json.loads(user_data)
        pretty_data = json.dumps(loaded_data, indent=2)
        return pretty_data
    
    def write_to_file(self):
        json_file_name = self.file_name+'.json'
        json_file = open(json_file_name, 'w')
        json_file.write(self.pretty_data)