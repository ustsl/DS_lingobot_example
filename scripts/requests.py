import requests

class Request_post:
    def __init__ (self, link, token):
        response = requests.post(link, headers = {'Authorization': token})
        self.result = response.json()