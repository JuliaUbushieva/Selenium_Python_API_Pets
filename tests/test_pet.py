from api import Pets
import allure

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


@allure.feature('Pet Management')
@allure.story('Create New Pet')
@allure.severity('high')
def test_post_pet():
    with allure.step("Post a new pet and verify the response"):
        pet_id, status = pt.post_pet()
    with allure.step(f"Assert that the status code is 200"):
        assert status == 200
    with allure.step(f"Assert that pet ID is returned"):
        assert pet_id


def test_get_pet_photo():
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


def test_get_pet():
    status = pt.get_pet()
    assert status == 200


def test_edit_pet_name():
    status = pt.edit_pet_name()[1]
    pet_id = pt.edit_pet_name()[0]
    assert status == 200
    assert pet_id


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


def test_put_pet_like():
    status = pt.put_pet_like()
    assert status == 200


def test_put_pet_comment():
    status, comment = pt.put_pet_comment()
    assert status == 200
    assert comment


def test_reg_and_del_user():
    delete_status = pt.reg_and_del_user()
    assert delete_status == 200
