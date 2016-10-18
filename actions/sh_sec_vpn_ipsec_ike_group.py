import requests
import warnings
import time
import json

from st2actions.runners.pythonrunner import Action

class shSecVpnIpsecIkeGroup(Action):
    def run(self, deviceIP, login, password, ikeGroup):
        
        headers = {
            "accept": "application/json",
            "content-length": "0"
        }

        ikeGroup = str(ikeGroup)
        #print(cmd_path)
        url = "https://" + deviceIP + "/show/security/vpn/ipsec/ike-group/" + ikeGroup
        print(url)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmd_response = requests.post(url, auth=(login, password), headers=headers, verify=False)

        #print(cmd_response.status_code) 
        if cmd_response.status_code == 201:
            cmd_path = cmd_response.headers["Location"]
            print(cmd_path)