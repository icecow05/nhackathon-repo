import numpy as np
with open('./input.txt', 'r') as f:
  input = f.read()
lines = input.splitlines()
matrices = {}
current_matrix = None
operations = []
operation_count = 0

for line in lines:
  if line.strip():
    cleaned_line = line.split()
    if line.isalpha() and len(line) == 1:
      current_matrix = line
      matrices[current_matrix] = []
    elif cleaned_line[0].isnumeric():
      matrices[current_matrix].append(cleaned_line)
    elif "+" in cleaned_line or "-" in cleaned_line or "*" in cleaned_line or "/" in cleaned_line:
      operations.append(cleaned_line)

def perform_operations(op, vectors):
  result = np.array(vectors[op[0]], dtype = int)

  for i in range(1, len(op), 2):
    operator = op[i]
    operand = op[i+1]
    

    if operator == "+":
      result += np.array(vectors[operand], dtype = int) 
    elif operator == "-":
      result -= np.array(vectors[operand], dtype = int)
    elif operator == "*":
      result = np.dot(result, np.array(vectors[operand], dtype=int))
    elif operator == "/":
      result /= np.array(vectors[operand], dtype = int)

  return result.tolist()

results = {}
for i, op in enumerate(operations):
  result = perform_operations(op, matrices)
  results[f"{' '.join(operations[i])}"] = result
for key, value in results.items():
    print(f'{key}')
    for row in value:
        print(' '.join(map(str, row)))
    print()