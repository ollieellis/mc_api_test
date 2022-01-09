### Specification
The MAIN api, is a RESTful api that allows users to connect via HTTP to interact with our database of accounts. Using RESTful named functions users can; get info, create and remove accounts from our database. However due to the sensitivity of the data; we do not allow a user to update/modify any existing account. Additionaly there is a get_health function to confirm the service is active.

### Documentation
Following will be examples on how to envoke the 4 functions in python3. For this demo I shall use the requests and json, python libraies (pip install requests json) and local host for my adress (http://127.0.0.1:8000/).

healthz
```python
r = requests.get('http://127.0.0.1:8000/healthz')
```

get
```python
r = requests.get('http://127.0.0.1:8000/accounts/500')
```

delete
```python
r = requests.delete('http://127.0.0.1:8000/accounts/500')
```

post
```python
pload = {'name':'Olivia','description':'Olivias account','balance':100.0,'active':True}
r = requests.post("http://127.0.0.1:8000/accounts/500", json=pload)
```
To display the message in string format you can use:
```python
print("code ", r, ", text: ", r.text)
```
