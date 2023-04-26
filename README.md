# FastApi with NBP api


## Create and activate virtual env

```bash 
python3.11 -m venv venv
source venv/bin/activate 
pip install --upgrade pip
```   
   


## Install dependencies

`pip install -r requirements.tx`

## Run it

`uvicorn main:app --reload` 

## Check it
Open your browser at http://127.0.0.1:8888/items/5?q=somequery.

You will see the JSON response as:

`{"item_id": 5, "q": "somequery"}`

## Interactive API docs

Now go to http://127.0.0.1:8888/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):