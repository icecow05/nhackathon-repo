with open('./input.txt', 'r') as f:
  # Read the entire content of the file into the variable 'input'
  input_text = f.read()

# Split the content of the file into lines and store them in a list
lines = input_text.splitlines()

# Iterate through each line in the list of lines
for line in lines: 
  cleaned_line = ''.join(char for char in line if char.isalnum()) # Remove non-alphanumeric characters from the line and convert to lowercase
  lowercase_cleaned_line = cleaned_line.lower()

  # Initialize an empty set to store unique characters
  unique_chars = set()
  # Iterate through each character in the cleaned and lowercase line
  for char in lowercase_cleaned_line:
    if char.isalnum(): # Check if the character is alphanumeric
      # Add the character to the set of unique characters
      unique_chars.add(char)
    elif not char.isalnum():
      char.remove(char)

  # Check if the cleaned and lowercase line is a palindrome
  logic = lowercase_cleaned_line == lowercase_cleaned_line[::-1]

  # Check the result of the palindrome check
  if logic == True:
    print(f"YES, {len(unique_chars)}")
  else:
    print("NO,", -1)
