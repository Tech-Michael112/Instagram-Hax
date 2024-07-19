import os
import requests
import logging 

git = 'git pull'
def Execution():
    try:
        os.system(git)
        import gram1
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
        print("There's an exception!!!")
    except ImportError as e:
        print("Error importing gram1 module: dont edit repository document...", e)

Execution()
