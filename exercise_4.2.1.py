with open("/tmp/datafile.txt", "w") as fileObj:
    for i in range(1, 101):
        fileObj.write(str(i) + "\n")
