import os
import requests
import logging 

error_color=f'\33[1;91m'
success_color=f'\033[1;32m'
cod=54
line=f'{cod}*"_"'

git = 'git pull'
def Execution():
    try:
        os.system(git)
        import gram1
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as error:
        print(f"There's an exception!!! error {error}")
    except ImportError as e:
        
        print(f"{error_color} dont edit the module documentation.... or author has not uploaded update yet \n{line}")
Execution()
