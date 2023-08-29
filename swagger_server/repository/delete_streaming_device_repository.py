from swagger_server.models.db.streaming_device_model import Streaming_Device
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class DeleteStreaming_DeviceRepository:

    def __init__(self, mysql: db, log: logging) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)

    def delete_streaming_device(self, id_streaming_device, internal_transaction_id):
        try:
            streaming_device = Streaming_Device.query.get(id_streaming_device)
            if streaming_device:
                streaming_device.destroy()
                return streaming_device.to_json()
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id,
                          "delete_streaming_device", __name__, error)
            return ""
