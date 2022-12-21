from yaml import load
import requests
import os

class GetIntervalsConfig:
    
    #Класс получает данные, 
    #которые необходимы для форсмирования реквест-запроса к системе INTERVALS
    
    def __init__ (self):
        
        self.token = None 
        self.api_link = None
        print ('Данные АПИ получены')
        
    def get_token(self, file):
        
        f = open(f'{file}.yaml' , 'r')
        config = load(f)
        email = config['intervals_email']
        password = config['intervals_password']
        data = {'email': email, 'password': password}
        response = requests.post('https://intervals.ru/auth/token/login', data=data)
        self.token = 'Token ' + response.json()['auth_token']


class IntervalsUpload:
    #Загрузчик
    def __init__ (self, token, api_link, list_data):
        self.token = token
        self.api_link = api_link
        self.list_data = list_data
        self.str_data = ''
        self.get_str_data()
        self.upload_data()
        
    def get_str_data (self):
        for list_elem in self.list_data:
            line = ';'.join(str(v) for v in list_elem)
            self.str_data+=line+'\n'
            
    def upload_data (self):   
        response = requests.put(self.api_link,
        headers = {'Authorization': self.token},                     
        data={"data":self.str_data})
        print ('Данные успешно загружены в контейнер')
        print (response)
        