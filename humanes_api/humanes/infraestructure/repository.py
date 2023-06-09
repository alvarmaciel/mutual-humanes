import abc
from humanes_api.humanes.domain.socies import AccountData


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, account_data: AccountData):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> AccountData:
        raise NotImplementedError


class AccountDataRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, account_data):
        self.session.add(account_data)

    def get(self, reference):
        return self.session.query(AccountData).filter_by(dni=reference).one()

    def list(self):
        return self.session.query(AccountData).all()