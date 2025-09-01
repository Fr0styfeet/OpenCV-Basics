import numpy as np

matrix = np.random.randint(0, 100, (5, 5))
print("Matrix:\n", matrix)

row = np.random.randint(0, 4)
col = np.random.randint(0, 4)

print(f"\nSelected Pixel : [{row}, {col}] ")

four = []
if row-1 >= 0: four.append(int(matrix[row-1, col]))
if row+1 < 5: four.append(int(matrix[row+1, col]))
if col-1 >= 0: four.append(int(matrix[row, col-1]))
if col+1 < 5: four.append(int(matrix[row, col+1]))  

diag = []
if row-1 >= 0 and col-1 >= 0: diag.append(int(matrix[row-1, col-1]))
if row-1 >= 0 and col+1 < 5: diag.append(int(matrix[row-1, col+1]))
if row+1 < 5 and col-1 >= 0: diag.append(int(matrix[row+1, col-1]))
if row+1 < 5 and col+1 < 5: diag.append(int(matrix[row+1, col+1]))

eight = four + diag  

print("4-Neighbors:", four  )
print("Diagonal Neighbors:", diag  )
print("8-Neighbors:", eight  )
