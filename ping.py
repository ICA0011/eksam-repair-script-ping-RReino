import requests


def check_server_status():
    a = requests.get("http://itcollege.ee")
    if a.status_code == 200:
        return True
    else:
        return False
