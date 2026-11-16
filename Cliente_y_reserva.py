from Excepciones_y_Logs import ClienteInvalidoError, ReservaInvalidaError, LoggerSistema
logger = LoggerSistema()

class Cliente:
    "Clase que representa a un cliente con validaciones estrictas y encapsulación."
    
    def __init__(self, nombre: str, documento: str, correo: str, telefono: str):
        self.nombre = nombre       # Utiliza el setter validado
        self.documento = documento # Utiliza el setter validado
        self.correo = correo       # Utiliza el setter validado
        self.telefono = telefono   # Utiliza el setter validado

    # --- ENCAPSULACIÓN Y VALIDACIONES (GETTERS Y SETTERS) ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            error_msg = f"Nombre de cliente inválido: '{valor}'. Debe tener al menos 3 caracteres."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__nombre = valor.strip()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        val_str = str(valor).strip()
        if not val_str.isdigit() or len(val_str) < 6:
            error_msg = f"Documento inválido: '{valor}'. Debe contener solo números (mínimo 6 dígitos)."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__documento = val_str

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            error_msg = f"Correo electrónico inválido: '{valor}'."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        val_str = str(valor).strip()
        if not val_str.isdigit() or len(val_str) < 7:
            error_msg = f"Teléfono inválido: '{valor}'."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__telefono = val_str

    def __str__(self):
        return f"Cliente: {self.__nombre} (Doc: {self.__documento})"


class Reserva:
    "Clase que integra cliente, servicio, duración y estado con manejo de excepciones."
    
    def __init__(self, cliente: Cliente, servicio, duracion_horas: int):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente" # Estados: Pendiente, Confirmada, Cancelada y Fallida

    @property
    def duracion_horas(self):
        return self.__duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, valor):
        try:
            val = int(valor)
            if val <= 0:
                raise ValueError("La duración debe ser mayor a 0 horas.")
            self.__duracion_horas = val
        except (ValueError, TypeError) as e:logger = LoggerSistema()

class Cliente:
    """Clase que representa a un cliente con validaciones estrictas y encapsulación."""
    
    def __init__(self, nombre: str, documento: str, correo: str, telefono: str):
        self.nombre = nombre       # Utiliza el setter validado
        self.documento = documento # Utiliza el setter validado
        self.correo = correo       # Utiliza el setter validado
        self.telefono = telefono   # Utiliza el setter validado

    # --- ENCAPSULACIÓN Y VALIDACIONES (GETTERS Y SETTERS) ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            error_msg = f"Nombre de cliente inválido: '{valor}'. Debe tener al menos 3 caracteres."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__nombre = valor.strip()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        val_str = str(valor).strip()
        if not val_str.isdigit() or len(val_str) < 6:
            error_msg = f"Documento inválido: '{valor}'. Debe contener solo números (mínimo 6 dígitos)."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__documento = val_str

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            error_msg = f"Correo electrónico inválido: '{valor}'."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        val_str = str(valor).strip()
        if not val_str.isdigit() or len(val_str) < 7:
            error_msg = f"Teléfono inválido: '{valor}'."
            logger.registrar_evento("ERROR", error_msg)
            raise ClienteInvalidoError(error_msg)
        self.__telefono = val_str

    def __str__(self):
        return f"Cliente: {self.__nombre} (Doc: {self.__documento})"


class Reserva:
    """Clase que integra cliente, servicio, duración y estado con manejo de excepciones."""
    
    def __init__(self, cliente: Cliente, servicio, duracion_horas: int):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente" # Estados: Pendiente, Confirmada, Cancelada, Fallida

    @property
    def duracion_horas(self):
        return self.__duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, valor):
        try:
            val = int(valor)
            if val <= 0:
                raise ValueError("La duración debe ser mayor a 0 horas.")
            self.__duracion_horas = val
        except (ValueError, TypeError) as e:
            error_msg = f"Duración de reserva inválida ({valor}): {e}"
        """Intenta procesar y confirmar la reserva controlando excepciones."""
        try:
            # Validamos si el servicio está disponible
            if hasattr(self.servicio, 'activo') and not self.servicio.activo:
                raise ReservaInvalidaError("No se puede confirmar la reserva: El servicio no está disponible.")
            
            # Cálculo del costo usando el método polimórfico del servicio
            costo_total = self.servicio.calcular_costo(self.duracion_horas)
        except Exception as e:
            self.estado = "Fallida"
            logger.registrar_evento("ERROR", f"Fallo al procesar reserva para {self.cliente.nombre}: {e}")
            raise ReservaInvalidaError(f"Error crítico en procesamiento de reserva") from e
        else:
            # Se ejecuta si todo sale bien
            self.estado = "Confirmada"
            logger.registrar_evento("EVENTO", f"Reserva confirmada exitosamente para {self.cliente.nombre}. Costo: ${costo_total}")
            return costo_total
        finally:
            # Bloque que siempre se ejecuta al intentar procesar una reserva
            print(f"[LOG INTERNO] Intento de reserva procesado con estado final: {self.estado}")

    def cancelar_reserva(self):
        self.estado = "Cancelada"
        logger.registrar_evento("EVENTO", f"Reserva cancelada para el cliente {self.cliente.nombre}.")
        error_msg = f"Duración de reserva inválida ({valor}): {e}"
        logger.registrar_evento("ERROR", error_msg)
        raise ReservaInvalidaError(error_msg) from e

    def confirmar_reserva(self):
        "Intenta procesar y confirmar la reserva controlando excepciones."
        try:
            # Validamos si el servicio está disponible
            if hasattr(self.servicio, 'activo') and not self.servicio.activo:
                raise ReservaInvalidaError("No se puede confirmar la reserva: El servicio no está disponible.")
            
            # Cálculo del costo usando el método polimórfico del servicio
            costo_total = self.servicio.calcular_costo(self.duracion_horas)
        except Exception as e:
            self.estado = "Fallida"
            logger.registrar_evento("ERROR", f"Fallo al procesar reserva para {self.cliente.nombre}: {e}")
            raise ReservaInvalidaError(f"Error crítico en procesamiento de reserva") from e
        else:
            # Se ejecuta si todo sale bien
            self.estado = "Confirmada"
            logger.registrar_evento("EVENTO", f"Reserva confirmada exitosamente para {self.cliente.nombre}. Costo: ${costo_total}")
            return costo_total
        finally:
            # Bloque que siempre se ejecuta al intentar procesar una reserva
            print(f"[LOG INTERNO] Intento de reserva procesado con estado final: {self.estado}")

    def cancelar_reserva(self):
        self.estado = "Cancelada"
        logger.registrar_evento("EVENTO", f"Reserva cancelada para el cliente {self.cliente.nombre}.")