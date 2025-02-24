n = int(input("Enter number of members: "))

num = []
hash_table_linear = [-1] * 25
hash_table_chaining = [[] for _ in range(25)]  # Chaining

for i in range(n):
    while True:
        t = input(f"Enter telephone number of member number {i + 1}: ")
        if t.isdigit():
            num.append(int(t))
            break
        else:
            print("Invalid input. Please enter a valid telephone number.")

print(f"Telephone numbers: {num}")

# Hashing function
def get_hash(value):
    digit_sum = sum(int(d) for d in str(value))
    return digit_sum % 10  # Hash table size is 10

# Insertion using Linear Probing
for i in num:
    position = get_hash(i)
    while hash_table_linear[position] != -1:
        position = (position + 1) % 25  # Linear probing
    hash_table_linear[position] = i

# Insertion using Chaining
for i in num:
    position = get_hash(i)
    hash_table_chaining[position].append(i)

# Search function with comparison count
def search_linear(value):
    position = get_hash(value)
    comparisons = 0
    while hash_table_linear[position] != -1:
        comparisons += 1
        if hash_table_linear[position] == value:
            return comparisons
        position = (position + 1) % 25
    return comparisons

def search_chaining(value):
    position = get_hash(value)
    comparisons = len(hash_table_chaining[position])  # Checks all elements in the chain
    return comparisons

# Compare Searching
search_values = [25, 99, 31, 50]  # Testing for existing and non-existing numbers
print("\n🔹 Comparisons for Searching:")
for num in search_values:
    cmp_linear = search_linear(num)
    cmp_chaining = search_chaining(num)
    print(f"{num}: Linear Probing - {cmp_linear} comparisons, Chaining - {cmp_chaining} comparisons")

# Print Hash Tables
print("\n🔹 Hash Table using Linear Probing:", hash_table_linear)
print("\n🔹 Hash Table using Chaining:")
for i, chain in enumerate(hash_table_chaining):
    print(f"Index {i}: {chain}")