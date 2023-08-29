# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_new_streaming_device import RequestNewStreamingDevice  # noqa: E501
from swagger_server.models.response_new_streaming_device import ResponseNewStreamingDevice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNewStreamingDeviceController(BaseTestCase):
    """NewStreamingDeviceController integration test stubs"""

    def test_new_streaming_device(self):
        """Test case for new_streaming_device

        Crear una nueva Dispositivo de streaming.
        """
        body = RequestNewStreamingDevice()
        response = self.client.open(
            '/new-streaming_device',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
