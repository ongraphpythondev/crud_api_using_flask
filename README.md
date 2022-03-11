# Flask API with CRUD operations
This POC includes the CRUD API operations on Product models like GET, POST, PUT, PATCH, DELETE.
  

# Installation and Running

clone the repository
```
git clone https://github.com/ongraphpythondev/crud_api_using_flask.git
cd crud_api_using_flask
```
create a virtual environment
```
python3 -m venv env
env/bin/activate.bat
```
install required packages
```
pip install -r requirements.txt
```
running
```
python api.py
```
## Operations:


**Create a product**:-   For creating a product,
```
				127.0.0.1:8000/product
```

**Get an specific product**:-  For getting a particular product ,
```
				 127.0.0.1:8000/product/id
				at the _**id**_ you have to put the id of the product you want to see.
```			
		
**Get all products**:-  For getting all products, 
```				
				127.0.0.1:8000/product
```

**Update a particular product**:-  For this you have to give products's id in this url and use PUT method,
```				
  			127.0.0.1:8000/product/ _**id**_
     			     and give what field you want to update
```
**For partial Update a particular product**:-  For this you have to give products's id in this url and use PATCH method,
```				
  			127.0.0.1:8000/product/ _**id**_
     			     and give what field you want to update
```
**Delete a particular product**:- For this you have to give product's id in this url
```
				127.0.0.1:8000/product/ _**id**_
```
