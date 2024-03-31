
class PetNotFound(Exception):
    """
    Pet was not found
    """

class PetCreateAbort(Exception):
    """
    Creating new pet was aborted
    """

class PetNotFoundOrUpdateAbort(Exception):
    """
    Pet was not found or update of pet was aborted
    """

class PetNotFoundOrDeleteAbort(Exception):
    """
    Pet was not found or update of pet was aborted
    """