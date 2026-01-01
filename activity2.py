import os
print("cheaking the file exists or not")
if os.path.exists('my_file.txt'):
    print("file exists")
else:
    print("file does not exist")

my_file = open("my_file.txt", "w")
my_file.write("Hello, I am a penguin and I am 1 year old.")
my_file.close()

os.remove("my_file.txt")
os.rmdir("mydirectory")