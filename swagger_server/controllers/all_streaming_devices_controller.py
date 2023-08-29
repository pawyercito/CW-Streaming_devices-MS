import connexion

from swagger_server.models.request_all_streaming_devices import RequestAllStreamingDevices

from flask.views import MethodView
from timeit import default_timer
from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.all_streaming_devices_uses_cases import AllStreaming_DevicesUseCase
from swagger_server.repository.all_streaming_devices_repository import AllStreaming_DevicesRepository
from swagger_server.resources.db import db


class AllStreaming_DevicesView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        all_streaming_devices_repository = AllStreaming_DevicesRepository(mysql, log)
        self.all_streaming_devices_use_case = AllStreaming_DevicesUseCase(all_streaming_devices_repository, log)

    def all_streaming_devices(self):  # noqa: E501
        """Todos los Dispositivo de streaming.

        Todos los Dispositivo de streaming # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseAllStreaming_Devices
        """

        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "all_streaming_devices"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:

            body = RequestAllStreamingDevices.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.all_streaming_devices_use_case.get_all_streaming_devices(
                body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos",
                     internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response
