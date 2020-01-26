import json
from pathlib import Path
# movies = [
#     {"id": 1, "title": "Venom", "year": 2019},
#     {"id": 2, "title": "dictator", "year": 2012},
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movie = json.loads(data)
print(movie)
