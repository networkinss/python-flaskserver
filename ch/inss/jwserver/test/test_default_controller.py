# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from ch.inss.jwserver.models.error_model import ErrorModel  # noqa: E501
from ch.inss.jwserver.models.metadata import Metadata  # noqa: E501
from ch.inss.jwserver.models.resources import Resources  # noqa: E501
from ch.inss.jwserver.models.shell import Shell  # noqa: E501
from ch.inss.jwserver.models.task import Task  # noqa: E501
from ch.inss.jwserver.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_metadata(self):
        """Test case for add_metadata

        Creates new metadata
        """
        metadata = {
  "binaryfiles" : [ "file1", "file2", "file3" ],
  "appname" : "demoapp",
  "author" : "John",
  "domain" : "example.com",
  "dbtype" : "postgres",
  "username" : "johndoe"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/metadata',
            method='POST',
            headers=headers,
            data=json.dumps(metadata),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_add_resources(self):
        """Test case for add_resources

        Creates new resources
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(filestream='/path/to/file',
                    filename='filename_example')
        response = self.client.open(
            '/api/v1/resources',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_add_shell(self):
        """Test case for add_shell

        Creates new shell
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(filestream='/path/to/file',
                    filename='filename_example')
        response = self.client.open(
            '/api/v1/shell',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_task(self):
        """Test case for add_task

        Creates new task
        """
        task = {
  "args" : [ "<appname>" ],
  "precheckfile" : "/bin/binaryfile",
  "postcheckfile" : [ "openapi.yaml" ],
  "replacemustache" : ".go",
  "shell" : "shellscript.sh",
  "name" : "generatesomething",
  "inputmustache" : "anyfilepath.mustache",
  "enabled" : "true",
  "firstarg" : "any"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/task',
            method='POST',
            headers=headers,
            data=json.dumps(task),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_metadata(self):
        """Test case for delete_metadata

        Deletes metadata by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/metadata/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_resources(self):
        """Test case for delete_resources

        Deletes resources by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/resources/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_shell(self):
        """Test case for delete_shell

        Deletes shell by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/shell/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task(self):
        """Test case for delete_task

        Deletes task by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/task/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_metadata_byname(self):
        """Test case for find_metadata_byname

        Returns metadata by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/metadata/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_resources_byname(self):
        """Test case for find_resources_byname

        Returns resources by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/resources/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_shell_byname(self):
        """Test case for find_shell_byname

        Returns shell by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/shell/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_task_byname(self):
        """Test case for find_task_byname

        Returns task by name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/task/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_metadata_list(self):
        """Test case for get_metadata_list

        List of metadatas
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/metadatas',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_resources_list(self):
        """Test case for get_resources_list

        List of resourcess
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/resourcess',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_shell_list(self):
        """Test case for get_shell_list

        List of shells
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/shells',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_list(self):
        """Test case for get_task_list

        List of tasks
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tasks',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_metadata(self):
        """Test case for update_metadata

        Updates metadata by name
        """
        metadata = {
  "binaryfiles" : [ "file1", "file2", "file3" ],
  "appname" : "demoapp",
  "author" : "John",
  "domain" : "example.com",
  "dbtype" : "postgres",
  "username" : "johndoe"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/metadata/{name}'.format(name='name_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(metadata),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_resources(self):
        """Test case for update_resources

        Updates resources by name
        """
        resources = {
  "filename" : "example.mustache"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/resources/{name}'.format(name='name_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(resources),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_shell(self):
        """Test case for update_shell

        Updates shell by name
        """
        shell = {
  "filename" : "shellscript.sh"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/shell/{name}'.format(name='name_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(shell),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task(self):
        """Test case for update_task

        Updates task by name
        """
        task = {
  "args" : [ "<appname>" ],
  "precheckfile" : "/bin/binaryfile",
  "postcheckfile" : [ "openapi.yaml" ],
  "replacemustache" : ".go",
  "shell" : "shellscript.sh",
  "name" : "generatesomething",
  "inputmustache" : "anyfilepath.mustache",
  "enabled" : "true",
  "firstarg" : "any"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/task/{name}'.format(name='name_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(task),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
