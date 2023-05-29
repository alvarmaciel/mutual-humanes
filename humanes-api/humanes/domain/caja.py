from humanes.domain.socies import Socie

class Caja:
    def __init__(self):
        self.total = 0
        self.invoices = []

class Cashier:
    def __init__(self, cashier: Socie):
        self.cashier = cashier

    def checkout(self, socie, today, cuota, caja):
        caja.total += cuota["amount"]
        caja.invoices.append({"socie": socie, "date": today, "amount": cuota["amount"]})
        socie.cuotas.append(cuota)
        socie.invoices.append({"socie": socie, "date": today, "amount": cuota["amount"]})