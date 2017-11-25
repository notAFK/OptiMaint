class Diagram(object):

    """
    id: int
    company: string (XC/WC)
    start_station: dictionary { station: Station, time: datetime }
    end_station: dictionary { station: Station, time: datetime }
    nr_cars: int
    mileage: double
    period: dictionary { start: datetime, end: datetime, type: string(SO/SX) }
    """

    def __init__(self, id, company, start_station, end_station,
                 nr_cars, mileage, period):
        self.id = id
        self.company = company
        self.start_station = start_station
        self.end_station = end_station
        self.nr_cars = nr_cars
        self.mileage = mileage
        self.period = period
