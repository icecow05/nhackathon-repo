import numpy as np
with open('matrix_operations/input.txt', 'r') as f:
  input_data = f.read()
lines = input_data.splitlines()
matrices = {}
current_matrix = None
operations = []
operation_count = 0
matrix_indicators = []
for line in lines:
  if line.strip():
    cleaned_line = line.split()
    if line.isalpha() and len(line) == 1:
      current_matrix = line
      matrix_indicators.append(current_matrix)
      matrices[current_matrix] = []
    elif cleaned_line[0].isnumeric():
      matrices[current_matrix].append(cleaned_line)
    elif "+" in cleaned_line or "-" in cleaned_line or "*" in cleaned_line or "/" in cleaned_line:
      operations.append(cleaned_line)


#print(matrices["A"])
a = np.array(matrices['A'], dtype=int)
b = np.array(matrices['B'], dtype=int)
c = np.array(matrices['C'], dtype=int)
d = np.array(matrices['D'], dtype=int)
e = np.array(matrices['E'], dtype=int)
f = np.array(matrices['F'], dtype=int)
g = np.array(matrices['G'], dtype=int)
h = np.array(matrices['H'], dtype=int)
i = np.array(matrices['I'], dtype=int)
j = np.array(matrices['J'], dtype=int)


"""
result1 = str((a+b).tolist())
print("A + B")
print(result1)
print(str((b+b+a).tolist()))
print(str((c+d+d+c).tolist()))
print(str(np.add(np.dot(e,f), np.dot(i,j)).tolist()))
"""
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

print("A + B")
print_matrix(a+b)
print("\nB + B + A")
print_matrix(b+b+a)
print("\nC + D + D + C")
print_matrix(c+d+d+c)
print("\nE * F + I * J")
print_matrix(np.add(np.dot(e,f), np.dot(i,j)))