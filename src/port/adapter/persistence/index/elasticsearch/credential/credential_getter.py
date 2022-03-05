import abc


class CredentialGetter(abc.ABC):

    @abc.abstractmethod
    def get_host(self) -> str:
        pass

    @abc.abstractmethod
    def get_username(self) -> str:
        pass

    @abc.abstractmethod
    def get_password(self) -> str:
        pass
