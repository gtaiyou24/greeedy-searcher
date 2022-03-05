import os

from port.adapter.persistence.index.elasticsearch.credential import CredentialGetter


class LocalCredentialGetter(CredentialGetter):

    def get_host(self) -> str:
        return os.environ.get("ELASTICSEARCH_HOSTNAME")

    def get_username(self) -> str:
        return os.environ.get("ELASTICSEARCH_USERNAME")

    def get_password(self) -> str:
        return os.environ.get("ELASTICSEARCH_PASSWORD")
