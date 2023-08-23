from nats import NATS

from app.core.interfaces.dao import BaseBroker
from .mailing import Mailing


class Broker(BaseBroker):
    def __init__(self, client: NATS) -> None:
        self.client = client
        self.mailing = Mailing(client)
