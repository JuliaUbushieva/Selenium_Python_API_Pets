import os.path

import pytest
import requests

from api import Pets
from settings import VALID_EMAIL, VALID_PASSWORD

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo():
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


def test_edit_pet_name():
    status = pt.edit_pet_name()[1]
    pet_id = pt.edit_pet_name()[0]
    assert status == 200
    assert pet_id


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


# @pytest.mark.xfail   // Request to the Swagger to put like for a pet. When rerun a test expected to return code 403: ""You already liked it", but actually still return code 200.
# def test_put_pet_like():
#     status = pt.put_pet_like()
#     assert status == 200
#
#
# def test_put_pet_comment():
#     status, response = pt.put_pet_comment()
#     expected_message = 'You are the best pet ever!'
#     assert status == 200
#     assert response.get('message') == expected_message


# def test_get_registered():
#     status = pt.get_registered()[0]
#     my_temporary_id = pt.get_registered()[1]
#     assert status == 200
#     assert my_temporary_id
