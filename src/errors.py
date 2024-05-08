class NotEnoughMoney(Exception):
    """Exception raised when funds on account are not sufficient"""

    pass


class UnknownEvent(Exception):
    """Raised when an Event kind is not known"""

    pass


class DepositTooHigh(Exception):

    pass
