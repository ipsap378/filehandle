outputfile = open("Upadtedfile.txt","w")
inputfiile = open('activity3.txt','r')
lines_seen_so_far = set()
print("eliminating duplicate lines...")
for line in inputfiile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)
inputfiile.close()
outputfile.close()