def find_longest_word(filename):
    longest_word = ""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words, remove punctuation
                words = [word.strip('.,!?;:"()[]{}<>') for word in line.split()]
                for word in words:
                    if len(word) > len(longest_word):
                        longest_word = word
        return longest_word
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python find_longest_word.py <filename>")
    else:
        result = find_longest_word(sys.argv[1])
        if result:
            print(f"The longest word is: {result}")
