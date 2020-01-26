from pathlib import Path

path = Path("ecommerce")

# is exists
# path.exists()
# to create a directory
# path.mkdir()
# to remove a directory
# path.rmdir()
# to remane a directory
# path.rename("ecommerce2")

# iterdir return the directories path and folders butit has two limitations
# we can not search by a pattern and another one is it doesn't search recursive
# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

# to search all files we can use
paths = [p for p in path.glob("*.py")]
print(paths)

# to search all files recursively

paths = [p for p in path.rglob("*.py")]
print(paths)
