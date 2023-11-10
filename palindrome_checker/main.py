with open('.input.txt', 'r') as f:
  input = f.read()
lines = input.splitlines()

for line in lines: 
  cleaned_line = ''.join(char for char in line if char.isalnum())
  unique_chars = set()
  for char in cleaned_line:
    if char.isalnum():
      unique_chars.add(char)
    elif not char.isalnum():
      char.remove(char)
  logic = cleaned_line == cleaned_line[::-1]
  if logic == True:
    print(f"YES, {len(unique_chars)}")
  else:
    print("NO,", -1)
