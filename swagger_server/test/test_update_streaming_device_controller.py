# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_update_streaming_device import RequestUpdateStreamingDevice  # noqa: E501
from swagger_server.models.response_update_streaming_device import ResponseUpdateStreamingDevice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUpdateStreamingDeviceController(BaseTestCase):
    """UpdateStreamingDeviceController integration test stubs"""

    def test_update_streaming_device(self):
        """Test case for update_streaming_device

        Actualizar Dispositivo de streaming.
        """
        body = RequestUpdateStreamingDevice()
        response = self.client.open(
            '/streaming_devices/{id_streaming_device}'.format(id_streaming_device=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
