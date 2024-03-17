class ClientNotFound(Exception):
    """
    Client was not found
    """

class ClientCreateAbort(Exception):
    """
    Creating new client was aborted
    """

class ClientNotFoundOrUpdateAbort(Exception):
    """
    Client was not found or update of client was aborted
    """

class ClientNotFoundOrDeleteAbort(Exception):
    """
    Client was not found or update of client was aborted
    """