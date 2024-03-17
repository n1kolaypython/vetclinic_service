class AppointmentNotFound(Exception):
    """
    Appointment was not found
    """

class AppointmentCreateAbort(Exception):
    """
    Creating new appointment was aborted
    """

class AppointmentNotFoundOrUpdateAbort(Exception):
    """
    Appointment was not found or update of appointment was aborted
    """

class AppointmentNotFoundOrDeleteAbort(Exception):
    """
    Appointment was not found or update of appointment was aborted
    """