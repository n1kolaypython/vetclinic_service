class ClientPaymentNotFound(Exception):
    """
    Client payment was not found
    """

class ClientPaymentCreateAbort(Exception):
    """
    Creating new client was aborted
    """

class ClientPaymentNotFoundOrUpdateAbort(Exception):
    """
    Client payment was not found or update of client payment was aborted
    """

class ClientPaymentNotFoundOrDeleteAbort(Exception):
    """
    Client payment was not found or update of client payment was aborted
    """