import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        '''Returns the raw response body as bytes.'''
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        '''Converts the response body to JSON.'''
        response_body = self.get_response_body()
        return json.loads(response_body)
