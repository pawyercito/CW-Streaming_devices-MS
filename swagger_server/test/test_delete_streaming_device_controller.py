# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.response_delete_streaming_device import ResponseDeleteStreamingDevice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeleteStreamingDeviceController(BaseTestCase):
    """DeleteStreamingDeviceController integration test stubs"""

    def test_delete_streaming_device(self):
        """Test case for delete_streaming_device

        Eliminar Dispositivo de streaming.
        """
        response = self.client.open(
            '/streaming_devices/{id_streaming_device}'.format(id_streaming_device=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
