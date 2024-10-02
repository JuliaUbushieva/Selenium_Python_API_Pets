import json
import requests
from settings import VALID_EMAIL, VALID_PASSWORD, TEMPORARY_EMAIL, TEMPORARY_PASSWORD


class Pets:
    """API library to the site http://34.141.58.52:8080/#/"""

    def __init__(self):
        # self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Request to the Swagger to obtain a unique user token for the specified email and password"""
        data = {"email": VALID_EMAIL,
                "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self):
        """Request to the Swagger to obtain a list of users"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json

        return status, amount

    def post_pet(self):
        """Request to the Swagger to create a new pet"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Kura', "type": 'parrot', "age": 4, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_pet_photo(self):
        """Request to the Swagger to upload a picture for a new pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('parrot.png', open('C:/Users/julia/PycharmProjects/PyTests/tests/photo/parrot.png', 'rb'),
                         'image/png')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def edit_pet_name(self):
        """Request to the Swagger to change a pet's name"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id, "name": 'Kitty', "type": 'dragon', "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def delete_pet(self):
        """Request to the Swagger to delete a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    # def put_pet_like(self):
    #     """Request to the Swagger to put like for a pet"""
    #     my_token = Pets().get_token()[0]
    #     pet_id = Pets().post_pet()[0]
    #     headers = {'Authorization': f'Bearer {my_token}'}
    #     url = f'{self.base_url}pet/{pet_id}/like'
    #     res = requests.put(url, headers=headers)
    #     status = res.status_code
    #     return status

    # def put_pet_comment(self):
    #     """Request to the Swagger to write a comment for a specific pet"""
    #     my_token = Pets().get_token()[0]
    #     my_id = Pets().get_token()[2]
    #     pet_id = Pets().post_pet()[0]
    #     headers = {'Authorization': f'Bearer {my_token}', 'Content-Type': 'application/json'}
    #     url = f'{self.base_url}pet/{pet_id}/comment'
    #     data = {"id": my_id, "message": 'You are the best pet ever!', "user_id": my_id}
    #     res = requests.put(url, json=data, headers=headers)
    #     status = res.status_code
    #     comment = res.json()
    #     return status, comment

    # def get_registered(self) -> json:
    #     data = {"email": TEMPORARY_EMAIL,
    #             "password": TEMPORARY_PASSWORD, "confirm_password": TEMPORARY_PASSWORD}
    #     res = requests.post(self.base_url + 'register', data=json.dumps(data))
    #     my_temporary_id = res.json()
    #     my_temporary_id = my_temporary_id.get('id')
    #     status = res.status_code
    #     print(my_temporary_id)
    #     return status, my_temporary_id

    # def delete_user(self):


Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().get_pet_photo()
Pets().edit_pet_name()
Pets().delete_pet()
# Pets().put_pet_like()
# Pets().put_pet_comment()
# Pets().get_registered()
