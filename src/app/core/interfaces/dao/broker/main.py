from abc import ABC
from .mailing import BaseMailing


class BaseBroker(ABC):
    mailing: BaseMailing
