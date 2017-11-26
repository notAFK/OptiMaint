import re
import os
import hashlib

from optimaint.db.database import Diagram
from optimaint.scraper import config


OPERATORS_MAP = {
    "VW": "Virgin",
    "XC": "Cross Country"
}


def parse_diagram(diagram_str):
    parsing_stations = "OUT"
    lines = diagram_str.split("\n")
    for index, line in enumerate(lines):
        if "Diagram :" in line:
            # diagram info
            line = line.split(": ")[1].split()
            company = line[0]
            no_cars = int(line[1][0])
            diagram_id = line[1]
            day_info = line[2]
            period_start = line[3]
            period_end = line[4]
        elif "OFF" in line:
            # It it means next line is first stn
            parsing_stations = "FIRST"
        elif parsing_stations == "IN":
            next_line = lines[index+1].split()
            if len(next_line) != 2 or ":" in next_line:
                # It means this last station
                line = line.split()
                end_station = line[0]
                end_time = line[1]
                parsing_stations = "OUT"
        elif "MILES" in line:
            miles = line.split(":(LD) ")[1].split()[4]
        elif parsing_stations == "FIRST" and line.strip():
            # First stn
            line = line.split()
            start_station = line[0]
            start_time = line[1]
            parsing_stations = "IN"

    diagram_id = int(diagram_id)
    miles = float(miles)
    # uuid=hashlib.sha256(str(diagram_id).encode('utf-8') + start_time.encode('utf-8') + end_time.encode('utf-8') + day_info.encode('utf-8')).hexdigest()
    return Diagram(id=diagram_id, total_mileage=miles, company=company,
                   no_cars=no_cars, schedule_uuid=0)


def parse_all_diagrams():
    ltp = "test_ltp.txt"
    f = open(os.path.join(config.DATA_FOLDER, ltp), "r")

    diagrams = [""]

    for line in f.readlines():
        line = line.replace("\t", " ")
        if "Diagram :" in line:
            diagrams.append(line.strip("\t "))
        else:
            diagrams[-1] += line.strip("\t ")

    diagrams = diagrams[1:]
    parsed_diagrams = []
    for i, d in enumerate(diagrams):
        diagrams[i] = diagrams[i].strip("\t ")
        diagrams[i] = re.sub(r"[\n]+", "\n", diagrams[i])
        parsed_diagrams.append(parse_diagram(diagrams[i]))

    return parsed_diagrams
