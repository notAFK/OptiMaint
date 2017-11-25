class Train(object):

    """
    id: int
    company: string (XC/WC)
    nr_cars: int
    mile_since_serv: double
    day_since_serv: day
    """

    def __init__(self, id, company, nr_cars, mile_since_serv, day_since_serv):
        self.id = id
        self.company = company
        self.nr_cars = nr_cars
        self.mile_since_serv = mile_since_serv
        self.day_since_serv = day_since_serv
