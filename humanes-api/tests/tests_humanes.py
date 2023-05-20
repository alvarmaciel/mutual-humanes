import unittest
from dataclasses import dataclass


@dataclass
class Socie:
    nombre: str
    apellido: str
    emprendimiento: str
    dni: str
    codigo_postal: str
    domicilio: str
    telefono: str
    email: str
    activo: bool
    tipo: str


class TestSocieModel(unittest.TestCase):
    def test_something_A(self):
        # Setup
        nomnbre = "Juan"
        apellido = "Perez"
        emprendimiento = "Cafeteria"
        dni = "12345678"
        codigo_postal = "1234"
        domicilio = "Calle 123"
        telefono = "12345678"
        email = "miemail@email.com"
        activo = True
        tipo = "pleno"
        # Exercise
        new_socie = Socie(
            nombre=nomnbre,
            apellido=apellido,
            emprendimiento=emprendimiento,
            dni=dni,
            codigo_postal=codigo_postal,
            domicilio=domicilio,
            telefono=telefono,
            email=email,
            activo=activo,
            tipo=tipo,
        )
        # Verify
        self.assertIsInstance(new_socie, Socie)

    def test_something_B(self):
        # Setup
        nomnbre = "Juan"
        apellido = "Perez"
        emprendimiento = "Cafeteria"
        dni = "12345678"
        codigo_postal = "1234"
        domicilio = "Calle 123"
        telefono = "12345678"
        email = "miemail@email.com"
        activo = True
        tipo = "pleno"
        # Exercise
        new_socie = Socie(
            nombre=nomnbre,
            apellido=apellido,
            emprendimiento=emprendimiento,
            dni=dni,
            codigo_postal=codigo_postal,
            domicilio=domicilio,
            telefono=telefono,
            email=email,
            activo=activo,
            tipo=tipo,
        )
        new_socie.activo = False
        # Verify
        self.assertIsInstance(new_socie, Socie)
        self.assertFalse(new_socie.activo)

if __name__ == '__main__':
    unittest.main()
