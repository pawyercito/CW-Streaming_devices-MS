from swagger_server.models.response_delete_streaming_device import ResponseDeleteStreamingDevice
from swagger_server.repository.delete_streaming_device_repository import DeleteStreaming_DeviceRepository
from swagger_server.utils.logs.logging import log as logging


class DeleteStreaming_DeviceUseCase:

    def __init__(self, streaming_device_repository: DeleteStreaming_DeviceRepository, log: logging):
        self.log = log
        self.streaming_device_repository = streaming_device_repository
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def delete_streaming_device(self, id_streaming_device: int, internal_transaction_id: str):
        streaming_device_data = self.streaming_device_repository.delete_streaming_device(
            id_streaming_device, internal_transaction_id)

        if streaming_device_data:
            response = ResponseDeleteStreamingDevice(
                code="200",
                message="Regla eliminada exitosamente",
                data=streaming_device_data,
                internal_transaction_id=None,
                external_transaction_id=None
            )
            return response, 200
        else:
            response = ResponseDeleteStreamingDevice(
                code="404",
                message="El valor ingresado no existe",
                data=[],
                internal_transaction_id=None,
                external_transaction_id=None
            )

            return response, 400
