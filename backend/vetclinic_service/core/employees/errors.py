
class EmployeeNotFound(Exception):
    """
    Employee was not found
    """

class EmployeeCreateAbort(Exception):
    """
    Creating new employee was aborted
    """

class EmployeeNotFoundOrUpdateAbort(Exception):
    """
    Employee was not found or update of employee was aborted
    """

class EmployeeNotFoundOrDeleteAbort(Exception):
    """
    Employee was not found or update of employee was aborted
    """