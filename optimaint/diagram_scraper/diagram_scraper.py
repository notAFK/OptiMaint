import re

from optimaint.diagram_scraper import config


def main():
    ltp = ""
    with open(config.DATA_FOLDER + "/test_ltp.txt", "r") as f:
        ltp = f.read()

    pattern = re.compile(r"(Diagram :.*(.*\n)*.*)(Diagram)", flags=re.M|re.S)

    for match in re.finditer(pattern, ltp):
        print(match.group(1))





if __name__=="__main__":
    main()