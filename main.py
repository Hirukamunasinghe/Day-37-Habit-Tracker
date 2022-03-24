import requests
from datetime import datetime
#POST
USER_NAME ="hiruka7"
TOKEN = "frfrjfjvjijo3jfir5"
GRAPH_ID = "graph33"

pixela_endpoint =  "https://pixe.la/v1/users"
user_params ={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_params ={
    "id":GRAPH_ID,
    "name":"Code Tracking System",
    "unit":"Hrs",
    "type":"int",
    "color":"shibafu"
}

headers ={
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

post_pixela_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#print(today.strftime("%Y-%m-%d"))

post_pixela_params ={
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you code today? ")
}


response = requests.post(url=post_pixela_endpoint,json=post_pixela_params,headers=headers)
print(response.text)

#UPDATE PIXELA
update_pixela_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_pixela_params ={
    "quantity":"2"
}

# response = requests.put(url=update_pixela_endpoint,json=update_pixela_params,headers=headers)
# print(response.text)

#DELETE
delete_pixela_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixela_endpoint,headers=headers)
# print(response.text)