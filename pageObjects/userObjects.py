from wsgiref import headers

import requests
from utilites.baseUrl import BaseUrl
from utilites.headers.headersUser import header
from utilites.jsonData.jsonDataUser import JsonData
from utilites.resources import ApiResources

url = BaseUrl._base + ApiResources._path_user


class UserObjects:

    def get_user(self):
        "Performing a GET operation on the server, the people have a user named Leanne Graham"
        response = requests.get(url, params={"name": "Leanne Graham", "email": "Sincere@april.biz"})
        return response

    def post_user(self):
        "Perform a POST operation on the server, add a user named bob."
        user_response = requests.post(url, json=JsonData.post_user, headers=header.header_post)
        return user_response

    def put_user(self):
        "Performing a PUT operation on the server, renaming user and email to user number 1."
        id_response = requests.put(url + ApiResources._id1_user, json=JsonData.put_user)
        return id_response

    def patch_user(self):
        "Performing a patch operation on the server, correcting the user name of user number one."
        id_response = requests.patch(url + ApiResources._id1_user, json=JsonData.patch_user)
        return id_response

    def delete_user(self):
        "Perform a delete operation on the server, delete user number 1."
        id_response = requests.delete(url + ApiResources._id1_user)
        return id_response
