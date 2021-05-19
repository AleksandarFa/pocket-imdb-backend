from django.test import TestCase
# from django.contrib.auth.hashers import check_password
from nose.tools import eq_
# from nose.tools import eq_, ok_
from ..serializers import CreateUserSerializer


class TestCreateUserSerializer(TestCase):
    def setUp(self):
        self.user_data = {'username': 'test', 'email': 'test', 'password': 'test'}

    def test_serializer_with_empty_data(self):
        serializer = CreateUserSerializer(data={})
        eq_(serializer.is_valid(), False)

    # TODO: Check test
    # def test_serializer_with_valid_data(self):
    #     serializer = CreateUserSerializer(data=self.user_data)
    #     ok_(serializer.is_valid())

    # TODO: Check test
    # def test_serializer_hashes_password(self):
    #     serializer = CreateUserSerializer(data=self.user_data)
    #     ok_(serializer.is_valid())

    #     user = serializer.save()
    #     ok_(check_password(self.user_data.get('password'), user.password))
