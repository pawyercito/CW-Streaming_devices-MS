from swagger_server.models.response_get_streaming_device import ResponseGetStreamingDevice
from swagger_server.repository.get_streaming_device_repository import GetStreaming_DeviceRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_get_streaming_device import RequestGetStreamingDevice


class GetStreaming_DeviceUseCase:

    def __init__(self, streaming_device_repository: GetStreaming_DeviceRepository, log: Logging):
        self.log = log
        self.streaming_device_repository = streaming_device_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def get_streaming_device(self, id_streaming_device, body: RequestGetStreamingDevice, internal_transaction_id: str):
        data = self.streaming_device_repository.get_streaming_device(
            id_streaming_device, internal_transaction_id, body.external_transaction_id)
        response = {}
        if data:

            response = ResponseGetStreamingDevice(
                code="200",
                message="Datos obtenidos exitosamente",
                data=data,
                internal_transaction_id=None,
                external_transaction_id=None
            )

        else:

            response = ResponseGetStreamingDevice(
                code="404",
                message="No hay datos registrados",
                data=[],
                internal_transaction_id=None,
                external_transaction_id=None
            )

        return response
