import numpy as np
from PIL import Image
from random import shuffle

N = 50
filename = input("Filename: ")
extension = input("Extension: ")
img = Image.open("C:\\Users\\sridhar\\Pictures\\percolate\\" + filename + '.' + extension)
im_ar = np.array(img)
##out = list(map(lambda x: map(lambda y: 1 if np.average(y) > 150 else 0, x), im_ar))

open_sites = []
for i in range(N):
    for j in range(N):
        if np.average(im_ar[i][j]) > 150:
            open_sites.append(str(i + 1) + " " + str(j + 1) + "\n")

##for i in range(N):
##    row = list(out[i])
##    for j in range(N):
##        if row[j] == 1:
##            open_sites.append(str(i + 1) + " " + str(j + 1) + "\n")

shuffle(open_sites)
with open(filename + "_" + str(N) + ".txt",'w',encoding = 'utf-8') as f:
    f.write(str(N) + "\n")
    f.writelines(map(str, open_sites))
