from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.delete_streaming_device_uses_cases import DeleteStreaming_DeviceUseCase
from swagger_server.repository.delete_streaming_device_repository import DeleteStreaming_DeviceRepository
from swagger_server.resources.db import db


class DeleteStreaming_DeviceView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        delete_streaming_device_repository = DeleteStreaming_DeviceRepository(mysql, log)
        self.delete_streaming_device_use_case = DeleteStreaming_DeviceUseCase(
            delete_streaming_device_repository, log)

    def delete_streaming_device(self, id_streaming_device: int):
        """Eliminar Dispositivo de streaming.

        Elimina un Dispositivo de streaming existente. # noqa: E501

        :param id_streaming_device: 
        :type id_streaming_device: int

        :rtype: ResponseDeleteStreaming_Device
        """

        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "delete_streaming_devices"
        package_name = __name__
        log = self.log
        start_time = default_timer()

        message = f"start request: {function_name}"
        log.info(
            self.msg_log,
            internal_transaction_id, function_name, package_name, message)

        response = self.delete_streaming_device_use_case.delete_streaming_device(
            id_streaming_device, internal_transaction_id)

        end_time = default_timer()
        log.info("ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos",
                 internal_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))

        return response
