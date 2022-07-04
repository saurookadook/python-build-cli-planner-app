from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

"""NOTE:
1) As of Python3.4, can also inherit from ABC instead of specifying `metaclass=ABCMeta`

2) Both DeadlinedMetaReminder and DeadlinedReminder have the
    two abstract methods we need: __iter__() comes from Iterable,
    while is_due() was defined by us. Any class that extends any of
    them will have to implement both methods in order to be concrete.
"""


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder, ABC):

    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        # date formatted to ISO8601
        formatted_date = self.date.isoformat()
        return iter([self.text, formatted_date])
