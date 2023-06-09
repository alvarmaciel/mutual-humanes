from sqlalchemy import text

from humanes_api.humanes.domain.socies import Account, AccountData, AccountType
from humanes_api.humanes.infraestructure import repository


def test_repository_can_save_an_account_data(session):
    # Setup
    account_data = AccountData("a name", "a last name", "", "123456", "1245", "an address", "+5468", "an email")
    # Exercise
    repo = repository.AccountDataRepository(session)
    repo.add(account_data)
    session.commit()

    # Verify
    query = text("SELECT name, last_name, venture, dni FROM 'accounts_data'")
    results = session.execute(query).fetchall()
    assert results == [("a name", "a last name", "", "123456")]

def test_repository_can_get_saved_account_data(session):
    raise NotImplementedError

def test_repository_can_list_saved_account_data(session):
    raise NotImplementedError

