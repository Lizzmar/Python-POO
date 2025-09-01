class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        # Método base que debe ser implementado por las subclases
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        # Implementación específica para notificar por email
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        # Implementación específica para notificar por SMS
        print(f"Enviando SMS a {self.usuario.sms}")


# (OCP) una clase o módulo debe estar abierto para que se le puedan añadir nuevas funcionalidades, 
# pero cerrado para que no se modifique el código ya existente.
# cuando se  agregar nuevas características, estas deben hacerse sin cambiar el código original que ya funciona.
# Así se evita romper la aplicación.