with open('file.txt') as fp:
    data1 = fp.read()

with open("activity3.txt") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("merging 2 files")
with open("mergefile.txt","w") as fp:
    fp.write(data1)