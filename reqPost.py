import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'eduardo', 'curso':'python', 'nivel':'intermedio'}
    headers = { 'Content-Type':'application/json', 'access-token':'12345' }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    #json post se encarga de serializarlos
    #data entonces nosotros de serializarlos

    #print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers #Dic
        server = headers_response['Server']
        print(server)
