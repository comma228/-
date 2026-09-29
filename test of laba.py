from os import getcwd, fsencode, listdir, walk, stat
from sys import platform
from psutil import virtual_memory
from platform import version, release
from json import dump

data = {}

data["platform"] = platform
data["version"] = version()
data["release"] = release()
data["virtual_memory"] = virtual_memory()._asdict()
data["current_directory"] = getcwd()

file_name = "test if laba.py"
file_bytes = fsencode(file_name)
data["file_bytes"] = (file_bytes)

data["listdir"] = listdir()

data["stat"] = str(stat("test of laba.py"))

with open("output.json", "w", encoding="utf-8") as file:
    dump(data, file, ensure_ascii=False, indent=4)
