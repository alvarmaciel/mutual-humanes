import pytest
import string
import random
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
        self.recipies = []

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

class Caja:
    def __init__(self):
        self.total = 0
        self.recipies = []

class Cashier:
    def __init__(self, cashier: Socie):
        self.cashier = cashier

    def checkout(self, socie, today, cuota, caja):
        caja.total += cuota["amount"]
        caja.recipies.append({"socie": socie, "date": today, "amount": cuota["amount"]})
        socie.cuotas.append(cuota)
        socie.recipies.append({"socie": socie, "date": today, "amount": cuota["amount"]})

def create_new_socie(tipo="pleno", activated=True):
    letters = string.ascii_letters
    numbers = string.digits
    length = 10
    socie = Socie(
        nombre=''.join(random.choice(letters) for _ in range(length)),
        apellido=''.join(random.choice(letters) for _ in range(length)),
        emprendimiento=''.join(random.choice(letters) for _ in range(length)),
        dni=''.join(random.choice(numbers) for _ in range(length)),
        codigo_postal=''.join(random.choice(numbers) for _ in range(length)),
        domicilio=''.join(random.choice(letters) for _ in range(length)),
        telefono=''.join(random.choice(numbers) for _ in range(length)),
        email=''.join(random.choice(letters) for _ in range(length)),
        activated=activated,
        tipo=tipo,)
    return socie


def test_create_socie():
    new_socie = create_new_socie()
    assert isinstance(new_socie, Socie)


def test_socie_activatesd_is_false_when_last_cuota_more_that_3_month_of_today():
    # Setup
    new_socie = create_new_socie()
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


def test_socie_activatesd_is_true_when_last_couta_is_less_than_3_month_today():
    # Setup
    new_socie = create_new_socie()
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


def test_cashier_can_register_a_payed_cuota_in_caja():
    # Setup
    caja = Caja()
    socio_cajero = create_new_socie(tipo="pleno", activated=True)
    cashier = Cashier(socio_cajero)
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    cuota = {"date": date(2022, 1, 1), "amount": 100}

    # Exercise
    cashier.checkout(socie, today, cuota, caja)

    # Verify
    assert caja.total == 100

def test_cashier_can_emit_a_recipie_and_save_it_in_caja():
    # Setup
    cashier = Cashier(create_new_socie(tipo="pleno", activated=True))
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    cuota = {"date": date(2022, 1, 1), "amount": 100}
    caja = Caja()
    # Exercise
    cashier.checkout(socie, today, cuota, caja)

    # Verify
    assert caja.total == 100
    assert len(caja.recipies) == 1
    assert caja.recipies[0] == {"socie": socie, "date": today, "amount": 100}

def test_cashier_can_emit_a_recipie_and_save_it_in_socie():
    # Setup
    cashier = Cashier(create_new_socie(tipo="pleno", activated=True))
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    cuota = {"date": date(2022, 1, 1), "amount": 100}
    caja = Caja()
    # Exercise
    cashier.checkout(socie, today, cuota, caja)

    # Verify
    assert caja.total == 100
    assert len(socie.recipies) == 1
    assert socie.recipies[0] == {"socie": socie, "date": today, "amount": 100}
