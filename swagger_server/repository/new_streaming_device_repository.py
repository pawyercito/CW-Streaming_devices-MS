from swagger_server.models.db.streaming_device_model import Streaming_Device
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class NewStreaming_DeviceRepository:

    def __init__(self, mysql: db, log: logging) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)

    def create_streaming_device(self, streaming_device, internal_transaction_id: str, external_transaction_id: str):
        try:
            new_streaming_device = Streaming_Device(streaming_device)
            new_streaming_device.save()
            return new_streaming_device.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id,
                          external_transaction_id, "new_streaming_device", __name__, error)
            return ""
