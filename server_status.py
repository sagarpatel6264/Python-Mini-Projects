import requests
def check_server(url):
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print("Server is ONLINE")
        else:
            print("Server ERROR")
    except:
        print("Server OFFLINE")
      
