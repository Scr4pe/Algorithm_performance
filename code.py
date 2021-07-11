import time
import random

confirmation_text = "Do you want to start this script:\n[y or Y] + Enter"
welcome = "\n\nWelcome to Algorithm performance."
P_create = "Create Random array"
P_start_ = "Starting Algorithm"
P_finish_selection = ""
P_exit = "\n\nThank you for using this product."
global counter
counter = 0
rank = []
random_list = []
sorted_list = []
shuffled_list = []
# Standard algo blueprint
# 1. print(started)
# 2. sort by algorithm
# 3. Check if the sorted list is correct
# 3.1 If everything is correct print("Everything is correct")
# 3.2 If its not correct print(Error in Algo X\n This algo doesnt work)
# 3.2.1 break up this Algo
# 4. print("This Algo X is done (1/8)")


# Create array
for i in range(1,5):
    random_list.append(i)
    sorted_list.append(i)
    shuffled_list.append(i)
shuffle_list = list(zip(random_list,shuffled_list))
random.shuffle(shuffle_list)
random_list,shuffled_list = zip(*shuffle_list)

# Selection
def selection_algo():
    print()
    # check if the algo worked
    if sorted_list == random_list:
        print("Algo worked")
    else:
        print("Algo didnt worked")
    # reset random_list
    random_list = shuffled_list

# Bubble
def bubble_algo():
    print()

# Insertion
def insertion_algo():
    print()

# Merge
def merge_algo():
    print()

# Quick
def quick_algo():
    print()

# Heap
def heap_algo():
    print()

# Counting
def counting_algo():
    print()

# Radix
def radix_algo():
    print()

# Bucket
def bucket_algo():
    print()

# Main function
def main():
    confirmation = input("\n\nDo you want to execute this script? \n[Y/y] ")
    if confirmation == "y" or confirmation == "Y":
        print(welcome)
        selection_algo()

        # Ranking all Algos
        # Name of Algo, 1. Time, 2. Comparisons, 3. Accesses

        # After all algos
        print(P_exit)

    else:
        print(P_exit)

if __name__ == "__main__":
    main()
