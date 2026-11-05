with open("D:\Python\day10\sample.txt", "r") as f:
    content = f.read()
    content = content.replace("python","java")
    print(content)
with open("D:\Python\day10\sample.txt", "w") as f:
    f.write(content)
