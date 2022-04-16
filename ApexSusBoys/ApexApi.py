import requests
import sys
import logging

#set logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class ApexApi:
    def __init__(self, api_key, platform, player, uid):
        self.api_key = "auth="+api_key
        self.games_endpoint = "https://api.mozambiquehe.re/games?"
        self.bridge_endpoint = 'https://api.mozambiquehe.re/bridge?'
        self.platform = "platform="+platform
        self.player = "player="+player
        self.uid = "uid="+uid

    def get_player_stats(self):
        # Example: https://api.mozambiquehe.re/bridge?version=5&platform=PC&player=HeyImLifeline&auth=YOURAPIKEY
        response = self.api_request(self.bridge_endpoint, self.platform, self.player, self.api_key)
        return response

    def track_player(self):
        # Example: https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&uid=PLAYER_UID&platform=PLATFORM&history=1&action=ACTION
        response = self.api_request(self.games_endpoint, self.api_key, self.uid)
        return response

    def query_player_by_uid(self):
        # Example: https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&name=PLAYER_UID&platform=PLATFORM
        response = self.api_request(self.bridge_endpoint, self.api_key, self.uid, self.platform)
        return response

    def form_request_string(self, api_endpoint, *args):
        request_string = api_endpoint+'&'.join(list(args))
        logger.info(request_string)
        return request_string

    def api_request(self, *args):
        response = requests.get(self.form_request_string(*args))
        logger.info(response.status_code)
        return response.content