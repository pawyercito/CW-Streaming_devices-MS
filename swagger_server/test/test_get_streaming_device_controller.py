# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_get_streaming_device import RequestGetStreamingDevice  # noqa: E501
from swagger_server.models.response_get_streaming_device import ResponseGetStreamingDevice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetStreamingDeviceController(BaseTestCase):
    """GetStreamingDeviceController integration test stubs"""

    def test_get_streaming_device(self):
        """Test case for get_streaming_device

        Obtener una Dispositivo de streaming.
        """
        body = RequestGetStreamingDevice()
        response = self.client.open(
            '/streaming_devices/{id_streaming_device}'.format(id_streaming_device=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
