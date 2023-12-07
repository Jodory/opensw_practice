# Python3 샘플 코드 #


import requests

url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List'
params ={'serviceKey' : 'HyZOmaV0pdONOrIhqKtat2iK3fAUhv2XgBOkBMiSDKmKCuqOcxnqHxMSze9Fg%2Fkxw%2Bo189a3jqPMvoXj0J1JVA%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', 'type' : 'xml', 'encoding':'utf-8'}

response = requests.get(url, params=params)
print(response.content)

