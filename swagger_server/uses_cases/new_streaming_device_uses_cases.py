from swagger_server.models.response_new_streaming_device import ResponseNewStreamingDevice
from swagger_server.repository.new_streaming_device_repository import NewStreaming_DeviceRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_new_streaming_device import RequestNewStreamingDevice


class NewStreaming_DeviceUseCase:

    def __init__(self, streaming_device_repository: NewStreaming_DeviceRepository, log: Logging):
        self.log = log
        self.streaming_device_repository = streaming_device_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def new_streaming_device(self, body: RequestNewStreamingDevice, internal_transaction_id: str):
        streaming_device = body.data.to_dict()
        data = self.streaming_device_repository.create_streaming_device(
            streaming_device, internal_transaction_id, body.external_transaction_id)
        if data:
            response = ResponseNewStreamingDevice(
                code="200",
                message="Dato creado exitosamente",
                data=data,
                internal_transaction_id=None,
                external_transaction_id=None
            )
            return response
        else:
            response = ResponseNewStreamingDevice(
                code="404",
                message="No hay dispositivo de streaming registrado",
                data=[],
                internal_transaction_id=None,
                external_transaction_id=None
            )
            return response, 404
