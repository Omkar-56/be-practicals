import heapq

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq
    

def build_freq_map(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def build_tree(freq):
    pq = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(pq)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.freq+right.freq, left, right)
        heapq.heappush(pq, merged)

    return pq[0] if pq else None

def gen_codes(node, prefix = "", codebook=None):
    if codebook is None:
        codebook = {}

    if node is None:
        return codebook
    
    if node.left is None and node.right is None:
        codebook[node.char] = prefix
        return codebook
    
    gen_codes(node.left, prefix+"0", codebook)
    gen_codes(node.right, prefix+"1", codebook)

    return codebook

def encode_text(text, codebook):
    return "".join(codebook[ch] for ch in text)

def display_results(freq_map, codes, encoded_text):
    print("\nCharacter\tFrequency\tHuffman Code")
    for ch in sorted(codes.keys()):
        print(f"{ch}\t\t{freq_map[ch]}\t\t{codes[ch]}")
    print("\nEncoded Text:", encoded_text)


def main():
    print("=== Huffman Encoding ===")
    print("1. Automatic (from input text)")
    print("2. Manual (enter characters and frequencies)")
    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter the text: ")
        freq_map = build_freq_map(text)

    elif choice == "2":
        freq_map = {}
        text = ""
        n = int(input("Enter number of characters: "))
        for i in range(n):
            ch = input(f"Character {i + 1}: ")[0]
            f = int(input(f"Frequency of {ch}: "))
            freq_map[ch] = f
            text += ch * f

    else:
        print("Invalid choice!")
        return

    root = build_tree(freq_map)
    codes = gen_codes(root)
    encoded_text = encode_text(text, codes)
    display_results(freq_map, codes, encoded_text)


if __name__ == "__main__":
    main()