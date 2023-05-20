import pytest
from datetime import date


class Socie:
    def __init__(self, nombre: str, apellido: str, emprendimiento: str, dni: str, codigo_postal: str, domicilio: str,
                 telefono: str, email: str, activated: bool, tipo: str, cuotas: list = []):
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


@pytest.fixture
def new_socie():
    return Socie(
        nombre="Juan",
        apellido="Perez",
        emprendimiento="Cafeteria",
        dni="12345678",
        codigo_postal="1234",
        domicilio="Calle 123",
        telefono="12345678",
        email="mimail@mail.com",
        activated=True,
        tipo="pleno",)


def test_create_socie(new_socie):
    new_socie = new_socie
    assert isinstance(new_socie, Socie)


def test_socie_activatesd_is_false_when_last_cuota_more_that_3_month_of_today(new_socie):
    # Setup
    new_socie = new_socie
    socie_cuota_payed = [
        {"date": date(2022, 1, 1), "amount": 100},
        {"date": date(2022, 2, 1), "amount": 100},
        {"date": date(2022, 2, 1), "amount": 100}
    ]
    today = date(2022, 6, 1)

    # Exercise
    new_socie.cuotas = socie_cuota_payed

    # Verify
    assert new_socie.get_status(today) is False


def test_socie_activatesd_is_true_when_last_couta_is_less_than_3_month_today(new_socie):
    # Setup
    new_socie = new_socie
    socie_cuota_payed = [
        {"date": date(2022, 3, 1), "amount": 100},
        {"date": date(2022, 4, 1), "amount": 100},
        {"date": date(2022, 5, 1), "amount": 100}
    ]
    today = date(2022, 6, 1)

    # Exercise
    new_socie.cuotas = socie_cuota_payed

    # Verify
    assert new_socie.get_status(today) is True