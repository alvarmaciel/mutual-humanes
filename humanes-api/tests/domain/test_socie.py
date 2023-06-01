import string
import random
from datetime import date
from humanes.domain.socies import Socie
from humanes.domain.cash_register import CashRegister, Cashier


def create_new_socie(tipo="adherente", activated=True):
    letters = string.ascii_letters
    numbers = string.digits
    length = 10
    socie = Socie(
        name=''.join(random.choice(letters) for _ in range(length)),
        last_name=''.join(random.choice(letters) for _ in range(length)),
        business=''.join(random.choice(letters) for _ in range(length)),
        dni=''.join(random.choice(numbers) for _ in range(length)),
        zip_code=''.join(random.choice(numbers) for _ in range(length)),
        address=''.join(random.choice(letters) for _ in range(length)),
        phone=''.join(random.choice(numbers) for _ in range(length)),
        email=''.join(random.choice(letters) for _ in range(length)),
        activated=activated,
        type=tipo, )
    return socie


def test_create_socie():
    new_socie = create_new_socie()
    assert isinstance(new_socie, Socie)


def test_socie_activatesd_is_false_when_last_fee_more_that_3_month_of_today():
    # Setup
    new_socie = create_new_socie()
    socie_fee_payed = [
        {"date": date(2022, 1, 1), "amount": 100},
        {"date": date(2022, 2, 1), "amount": 100},
        {"date": date(2022, 2, 1), "amount": 100}
    ]
    today = date(2022, 6, 1)

    # Exercise
    new_socie.fees = socie_fee_payed

    # Verify
    assert new_socie.get_status(today) is False


def test_socie_activatesd_is_true_when_last_couta_is_less_than_3_month_today():
    # Setup
    new_socie = create_new_socie()
    socie_fee_payed = [
        {"date": date(2022, 3, 1), "amount": 100},
        {"date": date(2022, 4, 1), "amount": 100},
        {"date": date(2022, 5, 1), "amount": 100}
    ]
    today = date(2022, 6, 1)

    # Exercise
    new_socie.fees = socie_fee_payed

    # Verify
    assert new_socie.get_status(today) is True


def test_cashier_can_register_a_payed_fee_in_cash_register():
    # Setup
    cash_register =  CashRegister()
    humane_socie = create_new_socie(tipo="humane", activated=True)
    cashier = Cashier(humane_socie)
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="adherente", activated=True)
    fee = {"date": date(2022, 1, 1), "amount": 100}

    # Exercise
    cashier.checkout(socie, today, fee, cash_register)

    # Verify
    assert cash_register.total == 100


def test_cashier_can_emit_a_recipie_and_save_it_in_cash_register():
    # Setup
    cashier = Cashier(create_new_socie(tipo="pleno", activated=True))
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    fee = {"date": date(2022, 1, 1), "amount": 100}
    cash_register =  CashRegister()
    # Exercise
    cashier.checkout(socie, today, fee, cash_register)

    # Verify
    assert cash_register.total == 100
    assert len(cash_register.invoices) == 1
    assert cash_register.invoices[0] == {"socie": socie, "date": today, "amount": 100}


def test_cashier_can_emit_a_recipie_and_save_it_in_socie():
    # Setup
    cashier = Cashier(create_new_socie(tipo="pleno", activated=True))
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    fee = {"date": date(2022, 1, 1), "amount": 100}
    cash_register =  CashRegister()
    # Exercise
    cashier.checkout(socie, today, fee, cash_register)

    # Verify
    assert cash_register.total == 100
    assert len(socie.invoices) == 1
    assert socie.invoices[0] == {"socie": socie, "date": today, "amount": 100}


def test_cashier_can_emit_a_recipie_and_save_it_in_cash_register_and_socie():
    # Setup
    cashier = Cashier(create_new_socie(tipo="pleno", activated=True))
    today = date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    fee = {"date": date(2022, 1, 1), "amount": 100}
    cash_register =  CashRegister()
    # Exercise
    cashier.checkout(socie, today, fee, cash_register)

    # Verify
    assert cash_register.total == 100
    assert len(socie.invoices) == 1
    assert socie.invoices[0] == {"socie": socie, "date": today, "amount": 100}
    assert len(cash_register.invoices) == 1
    assert cash_register.invoices[0] == {"socie": socie, "date": today, "amount": 100}
    assert socie.fees == [{"date": date(2022, 1, 1), "amount": 100}]


def test_cashier_can_get_all_invoices_by_socie():
    # Setup
    cash_register =  CashRegister()
    cashier = Cashier(create_new_socie(tipo="pleno", activated=True), cash_register)
    date(2022, 6, 1)
    socie = create_new_socie(tipo="General", activated=True)
    fee_1 = {"date": date(2022, 1, 1), "amount": 100}
    fee_2 = {"date": date(2022, 2, 1), "amount": 100}
    fee_3 = {"date": date(2022, 3, 1), "amount": 100}
    socie.fees = [fee_1, fee_2, fee_3]
    cash_register.invoices = [{"socie": socie, "date": fee_1["date"], "amount": fee_1["amount"]},
                     {"socie": socie, "date": fee_2["date"], "amount": fee_2["amount"]},
                     {"socie": socie, "date": fee_3["date"], "amount": fee_3["amount"]}]
    cash_register =  CashRegister()
    # Exercise
    socie_invoices = cashier.get_all_invoices_by_socie({"socie": socie})

    # Verify
    assert len(socie_invoices) == len(socie.invoices)
    assert socie_invoices == socie.invoices
