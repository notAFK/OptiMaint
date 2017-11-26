
from optimaint.librarian.db import SESSION

s = SESSION()

# USE INSErt INTO ... your table with right values
#SELECT arrivals.unit, departures.miles, 'XS' AS company, arrivals.date, departures.station_id, departures.finish_depot, departures.time, arrivals.arrival_time FROM arrivals JOIN departures ON departures.finish_depot = arrivals.station_id AND departures.date = arrivals.date AND departures.unit = arrivals.unit;