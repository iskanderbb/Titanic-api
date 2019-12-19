# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO


from swagger_server.models.people import People  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.person_data import PersonData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_people_add(self):
        """Test case for people_add

        Add a person to the database
        """
        person = PersonData()
        response = self.client.open(
            '/people',
            method='POST',
            data=json.dumps(person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_people_list(self):
        """Test case for people_list

        Get a list of all people
        """
        response = self.client.open(
            '/people',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_delete(self):
        """Test case for person_delete

        Delete this person
        """
        response = self.client.open(
            '/people/{uuid}'.format(uuid='uuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_get(self):
        """Test case for person_get

        Get information about one person
        """
        response = self.client.open(
            '/people/{uuid}'.format(uuid='uuid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_person_update(self):
        """Test case for person_update

        Update information about one person
        """
        person = PersonData()
        response = self.client.open(
            '/people/{uuid}'.format(uuid='uuid_example'),
            method='PUT',
            data=json.dumps(person),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
