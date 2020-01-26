from pathlib import Path
from time import ctime

path = Path("ecommerce/app.py")

# path.exists()
# rename
# path.rename()
# delete
# path.unlink()

# information about this file
print(ctime(path.stat().st_ctime))
print(path.read_text())
