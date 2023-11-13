from random import shuffle

# Function to read input from a file
def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            symbols = [line.strip() for line in file.readlines()]
            valid_symbols = []

            # Iterate through each symbol read from the file
            for symbol in symbols:
                try:
                    n = int(symbol)
                    if n <= 0:
                        print(symbol)
                        print("invalid")
                    else:
                        valid_symbols.append(symbol)
                # If the conversion to an integer fails, print the symbol and mark it as invalid
                except ValueError:
                    print(symbol)
                    print("invalid")

            return valid_symbols
        
    except FileNotFoundError:
        print("Input file not found.")
        return None
    
    except Exception as e:
        print(f"There was an error during import: {str(e)}")
        return None

# File path for input symbols
input_file_path = "./input.txt"
symbol_numbers = read_input(input_file_path)


# Function to generate a Dobble deck
def generate_dobble_deck(numberOfSymbolsOnCard, shuffleSymbolsOnCard=False):
    cards = []

    n = numberOfSymbolsOnCard - 1

    # Populate the cards list
    for i in range(n+1): 
        cards.append([1])
        for j in range(n):
            cards[i].append((j+1)+(i*n)+1)

    for i in range(0, n):
        for j in range(0, n):
            cards.append([i+2])
            for k in range(0, n):
                val = (n+1 + n*k + (i*k+j)%n)+1
                cards[len(cards)-1].append(val)

    # Shuffle symbols on cards if specified
    if shuffleSymbolsOnCard:
        for card in cards:
            shuffle(card)

    # Print each card with its index
    for i, card in enumerate(cards, 1):
        line = f"{i} - {card}"
        print(line)

# Iterate through symbol numbers and generate Dobble decks
for symbol_number in symbol_numbers:
    print(symbol_number)
    generate_dobble_deck(int(symbol_number), shuffleSymbolsOnCard=False)
    print()