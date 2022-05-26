import urequests

HTTP_HEADERS = {'Content-Type': 'application/json'}
request = urequests.get('https://fakestoreapi.com/products/categories', headers = HTTP_HEADERS)
print(request.text)
if 'electronics' in request.text:
    print('connection is OK')