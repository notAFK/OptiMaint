
from optimaint.librarian.db import SESSION

s = SESSION()

# USE INSErt INTO ... your table with right values
s.execute('INSERT INTO ann_route SELECT arrivals.diagram, departures.miles, arrivals.exam FROM arrivals JOIN departures ON departures.finish_depot = arrivals.station_id AND departures.date = arrivals.date AND departures.unit = arrivals.unit;')
