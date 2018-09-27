import os.path
import fileinput

path = 'e://python/untitled'
dirs = os.listdir(path)
for file in dirs:
    if os.path.splitext(file)[1].find(".html") > -1:

        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open(file, "w", encoding="utf-8") as f_w:
            for line in lines:
                if "/ty7697/" in line:
                    # 替换
                    line = line.replace("/ty7697/", "/string2/")
                f_w.write(line)