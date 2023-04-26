import os
path = os.chdir("I:\\New folder")

i = ["pizza", "map", "night", "biggan"]
j = 0
for file in os.listdir(path):
    new_file_name = "{}.jpg".format(i[j])
    
    os.rename(file, new_file_name)
    
    j = j + 1
