from datetime import date

class Socie:
    def __init__(self, nombre: str, apellido: str, emprendimiento: str, dni: str, codigo_postal: str, domicilio: str,
                 telefono: str, email: str, activated: bool, tipo: str, cuotas: list = [], recipies: list = []):
        self.nombre = nombre
        self.apellido = apellido
        self.emprendimiento = emprendimiento
        self.dni = dni
        self.codigo_postal = codigo_postal
        self.domicilio = domicilio
        self.telefono = telefono
        self.email = email
        self.activated = activated
        self.tipo = tipo
        self.cuotas = []
        self.invoices = []

    def get_status(self, today:date)->bool:
        if self._check_and_update_status(today):
            self.activated = True
        else:
            self.activated = False
        return self.activated

    def _check_and_update_status(self, today:date)->bool:
        last_cuota = self.cuotas[-1]
        last_cuota_date = last_cuota["date"]
        difference = today - last_cuota_date
        if difference.days >= 90:
            return False
        else:
            return True

