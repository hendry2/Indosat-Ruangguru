#ServerInfo.py

class Info:

    def __init__(self, get):
        self.get = get

    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'simpleserver'
        if self.get.lower() == 'mode':
            return 'Percobaan By Sahrul Ramadhani'
        if self.get.lower() == 'about':
            return 'linux version'
        if self.get.lower() == 'ver':
            return '1.0.0b'
        if self.get.lower() == 'edited':
            return 'Config Opindo'
        if self.get.lower() == 'date':
            return '07-09-2014'
        if self.get.lower() == 'by':
            return 'inunxlabs'
        if self.get.lower() == 'mail':
            return 'ramadhanisahrul38@gmail.com'
        if self.get.lower() == 'remode':
            return 'Sahrul Ramadhani'