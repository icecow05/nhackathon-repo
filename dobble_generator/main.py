from random import shuffle

def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            symbols = [line.strip() for line in file.readlines()]
            return symbols
    except FileNotFoundError:
        print("A fájl nem található.")
        return None
    except Exception as e:
        print(f"Hiba történt a beolvasás közben: {str(e)}")
        return None

def is_valid_input(symbols):
    for symbol in symbols:
        try:
            n = int(symbol)
            if n <= 0:
                print("A szimbólumok számának pozitívnak kell lennie.")
                return False
        except ValueError:
            print("A bemenet nem érvényes, csak pozitív egész számokat fogad el.")
            return False
    return True

input_file_path = "./input.txt"
symbol_numbers = read_input(input_file_path)
#print(symbol_numbers)
"""if symbol_numbers is not None and is_valid_input(symbol_numbers):
    print("Az input érvényes.")
else:
    print("Az input érvénytelen.")"""

def generate_dobble_deck(numberOfSymbolsOnCard, shuffleSymbolsOnCard=False):
    cards = []


    n = numberOfSymbolsOnCard - 1


    numberOfCards = n**2 + n + 1


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

    if shuffleSymbolsOnCard:
        for card in cards:
            shuffle(card)

    for i, card in enumerate(cards, 1):
        line = f"{i} - {card}"
        print(line)

for symbol_number in symbol_numbers:
    print(symbol_number)
    generate_dobble_deck(int(symbol_number), shuffleSymbolsOnCard=False)
    print()

#generate_dobble_deck(30, shuffleSymbolsOnCard=False)
