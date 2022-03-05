from credentials import TOKEN, USERNAME
import requests
from datetime import datetime


# creating the user
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    'x-USER-TOKEN': TOKEN
}

# create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': 'programming',
    'name': 'Programming Graph',
    'unit': 'h',
    'type': 'float',
    'color': 'kuro'
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#post
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/programming"
pixel_config = {
    'date': datetime.today().strftime('%Y%m%d'),
    'quantity': str(input('How many hours were you programming today?')),
}
response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
print(response.text)

#update
# date_to_be_updated = datetime.today().strftime('%Y%m%d')
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/programming/{date_to_be_updated}"
# pixel_update_config = {
#     'quantity': '3.2',
# }
# print(pixel_update_config)
# response = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_update_config)
# print(response.text)

#delete
# date_to_be_deleted = 20200304
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/programming/{date_to_be_deleted}"
# pixel_update_config = {
#
# }
# print(pixel_update_config)
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)