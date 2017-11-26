from optimaint.scraper.diagram_scraper import parse_all_diagrams
from optimaint.db.config import SESSION

s = SESSION()
print(len(parse_all_diagrams()))
for i, diag in enumerate(parse_all_diagrams()):
    print(i)
    s.add(diag)
    s.commit()
