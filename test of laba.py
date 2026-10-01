from os import getcwd, fsencode, listdir, walk, stat
from sys import platform
from psutil import virtual_memory
from platform import version, release
from json import dump
from stat import filemode
from datetime import datetime

data = {}
data["platform"] = platform
data["version"] = version()
data["release"] = release()
data["virtual_memory"] = virtual_memory()._asdict()
data["current_directory"] = getcwd()

file_name = "test of laba.py"
file_bytes = fsencode(file_name)
data["file_bytes"] = str(file_bytes)

data["listdir"] = listdir()

mode = stat("test of laba.py").st_mode
nlink = stat("test of laba.py").st_nlink
time = stat("test of laba.py").st_mtime
read_time = datetime.fromtimestamp(time)

data["stat"] = {
    "mode": filemode(mode),
    "nlink": nlink,
    "time": str(read_time),
    "size": stat("test of laba.py").st_size
    }

with open("output.json", "w", encoding="utf-8") as file:
    dump(data, file, ensure_ascii=False, indent=4)
