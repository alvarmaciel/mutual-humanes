from humanes.domain.socies import Socie

class Caja:
    def __init__(self):
        self.total = 0
        self.invoices = []

class Cashier:
    def __init__(self, cashier: Socie, caja: Caja=None):
        self.cashier = cashier
        self.caja = caja

    def checkout(self, socie, today, cuota, caja):
        caja.total += cuota["amount"]
        caja.invoices.append({"socie": socie, "date": today, "amount": cuota["amount"]})
        socie.cuotas.append(cuota)
        socie.invoices.append({"socie": socie, "date": today, "amount": cuota["amount"]})
    def get_all_invoices_by_socie(self, socie:Socie)->list:
        result = []
        for invoice in self.caja.invoices:
            if invoice["socie"] == socie:
                result.append(invoice)
        return result
