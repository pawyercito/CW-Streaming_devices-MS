from swagger_server.models.response_update_streaming_device import ResponseUpdateStreamingDevice
from swagger_server.repository.update_streaming_device_repository import UpdateStreaming_DeviceRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_update_streaming_device import RequestUpdateStreamingDevice


class UpdateStreaming_DeviceUseCase:

    def __init__(self, streaming_device_repository: UpdateStreaming_DeviceRepository, log: Logging):
        self.log = log
        self.streaming_device_repository = streaming_device_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def update_streaming_device(self, id_streaming_device, body: RequestUpdateStreamingDevice, internal_transaction_id: str):

        streaming_device_exist = self.streaming_device_repository.check_streaming_device(
            id_streaming_device, internal_transaction_id, body.external_transaction_id)

        if streaming_device_exist is None:
            response = ResponseUpdateStreamingDevice(
                code="404",
                message="No hay dato registrado",
                data=[],
                internal_transaction_id=None,
                external_transaction_id=None
            )
            return response, 404

        streaming_device_data = body.data.to_dict()
        data = self.streaming_device_repository.save_changes(
            streaming_device_exist, streaming_device_data, internal_transaction_id, body.external_transaction_id)

        if data:
            response = ResponseUpdateStreamingDevice(
                code="200",
                message="Data actualizada exitosamente",
                data=data,
                internal_transaction_id=None,
                external_transaction_id=None
            )
            return response
        else:
            return 400
