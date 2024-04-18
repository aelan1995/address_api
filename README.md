# Address API 
Assignment API using FASTAPI


## Instruction Installation ##

* Make sure to check if Python is installed 
  * Open Terminal
  * Type python -v
  * If not installed visit https://www.python.org/ and for this I'm currently using Python 3.12

* Get the address_api repository
  * Open Terminal
  * and type "git clone https://github.com/aelan1995/address_api.git"
  * cd address_api


## Create a Virtual Environment and Activate ##
    * pip install virtualenv <name>
    * cd <name>/Script/bin/activate
    * pip install -r requirements.txt


## Run Uvicorn ##
    * inside address_api folder
    * type "uvicorn main:app" or if specific ip and port is block
    * type "uvicorn main:app --host 0.0.0.0 --port 80 --reload"

## Open Browser ##
    * Type on the address bar http://127.0.0.1/docs   