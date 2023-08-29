from swagger_server.models.db.streaming_device_model import Streaming_Device
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class AllStreaming_DevicesRepository:

    def __init__(self, mysql: db, log: logging) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)

    def get_all_streaming_devices(self, internal_transaction_id, external_transaction_id):
        try:
            streaming_devices = Streaming_Device.query.all()
            if streaming_devices:
                data = [p.to_json() for p in streaming_devices]
                return data
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id,
                          external_transaction_id, "get_all_streaming_devices", __name__, error)
            return ""
