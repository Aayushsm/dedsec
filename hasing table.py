
def print_hash_table(lst, n):
    print("-"*17)
    print("| Index\t| Value\t|")
    print("-"*17)
    for i in range(10):
        print("| ",i,"\t| ",lst[i],"\t|")
    print("-"*17)


def hash_table_func():
    n = int(input("Enter no of keys: "))

    hash_table = [0 for i in range(10)]

    for i in range(n):
        value = int(input("Enter a value: "))
        hash_key = value % 10

        hash_table[hash_key] = value
    
        print("Value: ", value, "| Hash key: ", hash_key)

    print_hash_table(hash_table,n)

hash_table_func()