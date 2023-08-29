from swagger_server.models.db.streaming_device_model import Streaming_Device
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class UpdateStreaming_DeviceRepository:

    def __init__(self, mysql: db, log: logging) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)

    def save_changes(self, streaming_device_exist, streaming_device_data, internal_transaction_id, external_transaction_id):
        try:
            streaming_device_exist.id_streaming_device = streaming_device_data.get("id_streaming_device")
            streaming_device_exist.name_streaming_device = streaming_device_data.get("name_streaming_device")
            streaming_device_exist.state_streaming_device = streaming_device_data.get("state_streaming_device")
            streaming_device_exist.created_at = streaming_device_data.get("created_at")
            

            streaming_device_exist.save()
            return streaming_device_exist.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id,
                          external_transaction_id, "get_streaming_device", __name__, error)
            return ""

    def check_streaming_device(self, id_streaming_device, internal_transaction_id, external_transaction_id):
        try:
            streaming_device = Streaming_Device.query.get(id_streaming_device)
            return streaming_device
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id,
                          external_transaction_id, "get_streaming_device", __name__, error)
            return ""
