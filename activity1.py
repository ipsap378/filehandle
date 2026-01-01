with open('file.txt','w') as file:
    file.write("Hi i am a penguin and I am 1 year old")
file.close()

with open('file.txt','w') as file:
    data = file.readlines()
    print("the words in this file are...")
    for line in data:
      word = line.split()
      print(word)
file.close()