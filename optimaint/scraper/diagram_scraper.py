import re
import os

from optimaint.scraper import config


OPERATORS_MAP = {
    "VW": "Virgin",
    "XC": "Cross Country"
}


def parse_diagram(diagram_str):
    parsing_stations = "OUT"
    lines = diagram_str.split("\n")
    for index, line in enumerate(lines):
        print(line)
        if "Diagram :" in line:
            # diagram info
            line = line.split(": ")[1].split()
            operator = OPERATORS_MAP[line[0]]
            no_carriages = int(line[1][0])
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
    print('PARSED {}'.format(diagram_id))


def main():
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
    for i, d in enumerate(diagrams):
        diagrams[i] = diagrams[i].strip("\t ")
        diagrams[i] = re.sub(r"[\n]+", "\n", diagrams[i])
        parse_diagram(diagrams[i])


if __name__ == "__main__":
    main()
