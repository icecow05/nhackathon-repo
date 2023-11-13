import numpy as np

# Function to format a matrix as a string
def format_matrix(matrix):
    return '\n'.join([' '.join(map(str, row)) for row in matrix])

# Read input data from a file
with open('./input.txt', 'r') as f:
    input_data = f.read()

# Split input data into sections for matrices and operations
sections = input_data.split('operations\n')

# Parse matrices from the first section
matrices_data = sections[0].strip().split('matrices\n')[1].strip()
matrix_lines = matrices_data.split('\n')

# Dictionary to store matrices with their labels
matrices = {}
current_matrix = None

# Iterate through lines and parse matrices
for line in matrix_lines:
    if line.strip():
        cleaned_line = line.split()
        if cleaned_line[0].isalpha() and len(cleaned_line[0]) == 1:
            # Start a new matrix
            current_matrix = cleaned_line[0]
            matrices[current_matrix] = []
        elif cleaned_line[0].isnumeric():
            # Add row to the current matrix
            matrices[current_matrix].append(list(map(int, cleaned_line)))

# Perform matrix operations from the second section
operations_data = sections[1].strip()
operation_lines = operations_data.split('\n')

# Define the order of operations
precedence = {'*': 2, '/': 2, '+': 1, '-': 1}

# Iterate through each operation line
for operation_line in operation_lines:
    operation = operation_line.split()
    stack = []
    postfix = []

    # Convert the operation to postfix notation
    for token in operation:
        if token.isalpha():
            postfix.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    result_stack = []

    # Evaluate the postfix expression
    for token in postfix:
        if token.isalpha():
            result_stack.append(matrices[token])
        else:
            operand2 = result_stack.pop()
            operand1 = result_stack.pop()
            if token == '+':
                result_stack.append(np.add(operand1, operand2))
            elif token == '-':
                result_stack.append(np.subtract(operand1, operand2))
            elif token == '*':
                result_stack.append(np.dot(operand1, operand2))
            elif token == '/':
                # Note for later: Division is not a standard matrix operation, so handle it accordingly
                result_stack.append(np.divide(operand1, operand2))

    # Display the result of the operation with formatted output
    result_matrix = result_stack[0]
    print(' '.join(operation))
    print(format_matrix(result_matrix))
    print()