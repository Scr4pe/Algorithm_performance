import time
import random

# strings
confirmation_text = "\n\nDo you want to start this script:\n[y or Y] + Enter"
welcome = "\n\nWelcome to Algorithm performance.\n\n"
P_create = "Create Random list"
P_start_ = "Starting Algorithm"
P_finish_selection = ""
P_exit = "\n\nThank you for using this product."
P_name = ""
P_Algo_init = " Algo has started"
P_Algo_finished = " Algo is finished"

# float
bub_diff = 0.0
ins_diff = 0.0
mer_diff = 0.0
qui_diff = 0.0
hea_diff = 0.0
cou_diff = 0.0
rad_diff = 0.0
buc_diff = 0.0

# lists
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
# 4. print("This Algo X is done (1/8)")


# Create list and shuffle each other on the same way, so every algo has the same shuffled list 
for i in range(1,1000):
    random_list.append(i)
    sorted_list.append(i)
    shuffled_list.append(i)
shuffle_list = list(zip(random_list,shuffled_list))
random.shuffle(shuffle_list)
random_list,shuffled_list = zip(*shuffle_list)
shuffle_list = list(shuffle_list)
random_list = list(random_list)

# Selection Algo
""" Describtion of the Selection Algo
    This algo searches for the smallest value in the list and set it to position[0].
    And sorts the list in ascending order.
"""
def selection_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global sel_diff
    # set comparison in sorting as global
    global sel_com
    # set accesses in sorting as global
    global sel_acc
    # set variables to 0
    sel_diff = 0
    sel_com = 0
    sel_acc = 0
    P_name = "Selection"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    for i in range(len(random_list)):
        i_past = i
        for j in range(i+1, len(random_list)):
            if random_list[i_past] > random_list[j]:
                i_past = j
                sel_acc += 2
                sel_com += 1
            else:
                sel_acc += 2
                sel_com += 1
        # Swap minimum element with first element
        random_list[i], random_list[i_past] = random_list[i_past], random_list[i]
    # >>
    end = time.time()
    sel_diff = round(end - start,ndigits=4)
    print(P_name + P_Algo_finished)
    # check if the result is correct
    if sorted_list == random_list:
        print("Check was successful")
    else:
        print("Check was unsuccessful")
    print("reset random_list")
    # reset unshuffled list
    random_list = shuffled_list
    # create a border
    print(len(P_name + P_Algo_init) * "#")

# Bubble Algo
""" Describtion of the Bubble Algo

"""
def bubble_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global bub_diff
    # set comparison in sorting as global
    global bub_com
    # set accesses in sorting as global
    global bub_acc
    # set variables to 0
    bub_diff = 0
    bub_com = 0
    bub_acc = 0
    n = len(random_list)
    P_name = "Bubble"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    for i in range(n-1):
        for j in range(0, n-i-1):
            if random_list[j] > random_list[j + 1] :
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]

    # >>
    end = time.time()
    bub_diff = round(end - start,ndigits=4)
    print(P_name + P_Algo_finished)
    # check if the result is correct
    if sorted_list == random_list:
        print("Check was successful")
    else:
        print("Check was unsuccessful")
    print("reset random_list")
    # reset unshuffled list
    random_list = shuffled_list
    # create a border
    print(len(P_name + P_Algo_init) * "#")


# Insertion Algo
""" Describtion of the Insertion Algo

"""
# Insertion
def insertion_algo():
    # set difference in time later as float to global
    global bub_diff
    # set comparison in sorting as global
    global bub_com
    # set accesses in sorting as global
    global bub_acc
    # set variables to 0
    bub_diff = 0
    bub_com = 0
    bub_acc = 0
    n = len(random_list)
    P_name = "Bubble"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    
    # >>
    end = time.time()
    bub_diff = round(end - start,ndigits=4)
    print(P_name + P_Algo_finished)
    # check if the result is correct
    if sorted_list == random_list:
        print("Check was successful")
    else:
        print("Check was unsuccessful")
    print("reset random_list")
    # reset unshuffled list
    random_list = shuffled_list
    # create a border
    print(len(P_name + P_Algo_init) * "#")

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
    print(confirmation_text)
    confirmation = input()
    if confirmation == "y" or confirmation == "Y":
        print(welcome)
        print(P_create)
        selection_algo(random_list,sorted_list)
        print("---seconds %s---"%(sel_diff))
        print("---accesses %s---"%(sel_acc))
        print("---compairments %s---"%(sel_com))
        bubble_algo(random_list,sorted_list)
        print("---seconds %s---"%(bub_diff))
        print("---accesses %s---"%(bub_acc))
        print("---compairments %s---"%(bub_com))
        # Ranking all Algos
        # Name of Algo, 1. Time, 2. Comparisons, 3. Accesses

        # After all algos
        print(P_exit)
    else:
        print(P_exit)

if __name__ == "__main__":
    main()
