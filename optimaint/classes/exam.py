class Exam(object):

    """
    type: string (C1/C2...)
    mile_range: double
    day_range: int
    mile_tol: double
    day_tol: int
    """

    def __init__(self, type, mile_range, day_range, mile_tol, day_tol):
        self.type = type
        self.mile_range = mile_range
        self.day_range = day_range
        self.mile_tol = mile_tol
        self.day_tol = day_tol
