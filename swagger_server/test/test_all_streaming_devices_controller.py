# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_all_streaming_devices import RequestAllStreamingDevices  # noqa: E501
from swagger_server.models.response_all_streaming_devices import ResponseAllStreamingDevices  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAllStreamingDevicesController(BaseTestCase):
    """AllStreamingDevicesController integration test stubs"""

    def test_all_streaming_devices(self):
        """Test case for all_streaming_devices

        Todas las Dispositivos de streaming.
        """
        body = RequestAllStreamingDevices()
        response = self.client.open(
            '/streaming_devices',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
