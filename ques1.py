with open("D:\Python\day10\sample.txt", "r") as f:
    data = f.read()
    content = data.replace("python","java")
    search = data.find("learning")
    print(search)
    
    print(content)
with open("D:\Python\day10\sample.txt", "w") as f:
    f.write(content)