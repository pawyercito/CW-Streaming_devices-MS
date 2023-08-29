import connexion
from swagger_server.models.request_new_streaming_device import RequestNewStreamingDevice  # noqa: E501

from flask.views import MethodView
from timeit import default_timer
from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.new_streaming_device_uses_cases import NewStreaming_DeviceUseCase
from swagger_server.repository.new_streaming_device_repository import NewStreaming_DeviceRepository
from swagger_server.resources.db import db


class NewStreaming_DeviceView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        new_streaming_device_repository = NewStreaming_DeviceRepository(mysql, log)
        self.new_streaming_device_use_case = NewStreaming_DeviceUseCase(
            new_streaming_device_repository, log)

    def new_streaming_device(self):  # noqa: E501
        """Crear un nuevao Dispositivo de streaming.

        Crear uno nuevo Dispositivo de streaming. # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseNewStreaming_Device
        """

        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "new_streaming_device"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:

            body = RequestNewStreamingDevice.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.new_streaming_device_use_case.new_streaming_device(
                body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos",
                     internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response
