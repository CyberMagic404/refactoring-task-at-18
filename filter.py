from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 11:
    j = 0
    while j < a1 - 11:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                newVar = arr[n][n1][0] // 3
                n2 = arr[n][n1][1] // 3
                n3 = arr[n][n1][2] // 3
                M = int(newVar) + int(n2) + int(n3)
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 11
    i = i + 11
res = Image.fromarray(arr)
res.save('res.jpg')
