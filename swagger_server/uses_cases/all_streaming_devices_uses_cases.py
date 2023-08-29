from swagger_server.models.response_all_streaming_devices import ResponseAllStreamingDevices
from swagger_server.repository.all_streaming_devices_repository import AllStreaming_DevicesRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_all_streaming_devices import RequestAllStreamingDevices


class AllStreaming_DevicesUseCase:

    def __init__(self, streaming_device_repository: AllStreaming_DevicesRepository, log: Logging):
        self.log = log
        self.streaming_device_repository = streaming_device_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def get_all_streaming_devices(self, body: RequestAllStreamingDevices, internal_transaction_id: str):

        streaming_devices_data = self.streaming_device_repository.get_all_streaming_devices(
            body.external_transaction_id, internal_transaction_id)

        if streaming_devices_data:
            response = ResponseAllStreamingDevices(
                code="200",
                message="Datos obtenidos exitosamente",
                data=streaming_devices_data,
                internal_transaction_id=None,
                external_transaction_id=None
            )
        else:
            response = ResponseAllStreamingDevices(
                code="404",
                message="No hay dispositivos de streaming registrados",
                data=[],
                internal_transaction_id=None,
                external_transaction_id=None
            )

        return response
