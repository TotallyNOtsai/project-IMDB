# Can get apikey at https://imdb-api.com

import requests

class Imdb:
    # Set apikey type to str
    def __init__(self, apikey: str):
        self.apikey = apikey

    def searchall(self,name: str):
        '''
        Return the search result in json
        '''

        response = requests.get(f"https://imdb-api.com/en/API/SearchAll/{self.apikey}/{name}")
        response.raise_for_status()

        data = response.json()

        return data

    def getinfo_id(self,id: str):
        '''
        Return the info of the id in json
        '''
        if id[0:2] == "tt":
            response = requests.get(f"https://imdb-api.com/en/API/Title/{self.apikey}/{id}")

        elif id[0:2]  == "nm":
            response = requests.get(f"https://imdb-api.com/en/API/Name/{self.apikey}/{id}")

        elif id[0:2] == "co":
            response = requests.get(f"https://imdb-api.com/en/API/Company/{self.apikey}/{id}")
        
        else:return False

        response.raise_for_status()

        data = response.json()
        if data['errorMessage'] == "" or data['errorMessage'] is None:
            return data

        else:return False
            
    def get_info(self,type: int):
        '''
        Return top250 Movies/Series/Coming Soon/In Theaters in json/Weekend Boxoffice/Boxoffice Alltime

        type(parameter)

        1 = top250movies,
        2 = top250series,
        3 = coming soon,
        4 = in theaters,
        5 = weekend boxoffice,
        6 = boxoffice all time,
        '''
        if type == 1:
            response = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{self.apikey}')

        elif type == 2:
            response = requests.get(f'https://imdb-api.com/en/API/Top250TVs/{self.apikey}')
        
        elif type == 3:
            response = requests.get(f'https://imdb-api.com/en/API/ComingSoon/{self.apikey}')

        elif type == 4:
            response = requests.get(f'https://imdb-api.com/en/API/InTheaters/{self.apikey}')

        elif type ==5:
            response = requests.get(f'https://imdb-api.com/en/API/BoxOffice/{self.apikey}')

        elif type == 6:
            response = requests.get(f'https://imdb-api.com/en/API/BoxOfficeAllTime/{self.apikey}')
        
        else:return False

        response.raise_for_status()
        data = response.json()

        return data