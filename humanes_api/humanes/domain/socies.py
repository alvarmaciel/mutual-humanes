from dataclasses import dataclass, field
from datetime import date


@dataclass
class Socie:
    name: str
    last_name: str
    business: str
    dni: str
    zip_code: str
    address: str
    phone: str
    email: str
    type: str
    fees: list[dict] = field(default_factory=list)
    invoices: list[dict] = field(default_factory=list)
    activated: bool = field(default=True)

    def get_status(self, today: date) -> bool:
        if self._check_and_update_status(today):
            self.activated = True
        else:
            self.activated = False
        return self.activated

    def _check_and_update_status(self, today: date) -> bool:
        last_cuota = self.fees[-1]
        last_cuota_date = last_cuota["date"]
        difference = today - last_cuota_date
        if difference.days >= 90:
            return False
        else:
            return True
