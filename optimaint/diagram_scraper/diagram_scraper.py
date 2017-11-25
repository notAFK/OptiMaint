import re

from optimaint.diagram_scraper import config


OPERATORS_MAP = {
    "VW": "Virgin",
    "XC": "Cross Country"
}


def parse_diagram(diagram_str):
    for line in diagram_str.split("\n"):
        if "Diagram :" in line:
            # diagram info
            line = line.split(": ").split()
            operator = OPERATORS_MAP[line[0]]
            no_carriages = int(line[1][0])
            



def main():
    ltp = ""
    f = open(config.DATA_FOLDER + "\\test_ltp.txt", "r")

    diagrams = [""]

    for line in f.readlines():
        line = line.replace("\t", " ")
        if "Diagram :" in line:
            diagrams.append(line.strip("\t "))
        else:
            diagrams[-1] += line.strip("\t ")

    for i, d in enumerate(diagrams):
        diagrams[i] = diagrams[i].strip("\t ")
        diagrams[i] = re.sub(r"[\n]+", "\n", diagrams[i])
        print(diagrams[i])
    print(diagrams)

if __name__=="__main__":
    main()