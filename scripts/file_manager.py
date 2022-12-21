from yaml import full_load
import json


class YAML_worker:
    def __init__(self, file_name):
        self.file_name = file_name

class YAML_read(YAML_worker):
    def get_config(self):
        with open(f'{self.file_name}.yaml', 'r') as f:
            return full_load(f)

class JSON_worker:
    def __init__(self, name):
        self.name = name

class JSON_open(JSON_worker):
    def open (self):
        with open(f'{self.name}.json') as f:
            return json.load(f)

class JSON_load(JSON_worker):
    def load(self, data):
        with open(f'{self.name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)