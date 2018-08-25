import numpy as np
from PIL import Image
from random import shuffle

N = 50
img = Image.open(r"C:\Users\sridhar\Pictures\percolate\sheebuBW_50_new.bmp")
out = list(map(lambda x: map(lambda y: 1 if np.average(y) > 250 else 0, x), np.array(img)))
open_sites = [N]
for i in range(N):
    row = list(out[i])
    for j in range(N):
        if row[j] == 1:
            open_sites.append(str(i+1) + " " + str(j+1) + "\n")

shuffle(open_sites)
with open("sheebu" + str(N) + ".txt",'w',encoding = 'utf-8') as f:
    f.write(str(N) + "\n")
    f.writelines(map(str, open_sites))
