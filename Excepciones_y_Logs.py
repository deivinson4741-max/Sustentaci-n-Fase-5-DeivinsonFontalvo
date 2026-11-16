import datetime
import os

# --- Excepciones Personalizadas ---
class SoftwareFJError(Exception):
    "Clase base para todas las excepciones del sistema Software FJ."
    pass

class ClienteInvalidoError(SoftwareFJError):
    "Se lanza cuando los datos del cliente no cumplen con las validaciones."
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    "Se lanza cuando se intenta contratar un servicio inactivo o inválido."
    pass

class ReservaInvalidaError(SoftwareFJError):
    "Se lanza cuando una reserva falla por parámetros incorrectos o conflictos."
    pass


# --- Sistema de Logs ---
class LoggerSistema:
    "Clase encargada de registrar eventos y errores en un archivo de logs."
    
    def __init__(self, nombre_archivo="sistema_logs.txt"):
        self.nombre_archivo = nombre_archivo

    def registrar_evento(self, tipo, mensaje):
        "Registra eventos y errores aplicando bloques try/except/finally de forma segura."
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea_log = f"[{timestamp}] [{tipo.upper()}] {mensaje}\n"
        
        try:
            # Intenta abrir y escribir en el archivo de logs
            with open(self.nombre_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(linea_log)
        except IOError as e:
            # Manejo de error si falla la escritura en disco (encadenamiento de excepciones)
            raise RuntimeError(f"Fiebre crítica: No se pudo escribir en el archivo de logs.") from e
        else:
            # Se ejecuta si la escritura fue exitosa
            pass
        finally:
            # Bloque de cierre o cierre lógico garantizado
            pass