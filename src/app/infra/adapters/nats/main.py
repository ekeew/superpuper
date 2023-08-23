from nats import NATS

from app.core.interfaces.adapters import BaseBroker
from .mailing import Mailing


class NatsBroker(BaseBroker):
    def __init__(self, client: NATS) -> None:
        self.client = client
        self.mailing = Mailing(client)
