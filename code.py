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

# lists
rank = []
random_list = []
sorted_list = []
shuffled_list = []

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
""" Description of the Selection Algo
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
""" Description of the Bubble Algo
    This algo starts at the beginning of the list. And if next element on the list is larger swap [0] with [+1]. If next element is lower jump to next element[+1].
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
""" Description of the Insertion Algo
    This algo works with an Sorted and Un-Sorted list. Sorted list is list [0] and Un_sorted list is the rest.
    Next element after Sorted list is key and will be compaired from right to left (in Sorted list) to paste the variable in the right order (ascending).
"""
# Insertion
def insertion_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global ins_diff
    # set comparison in sorting as global
    global ins_com
    # set accesses in sorting as global
    global ins_acc
    # set variables to 0
    ins_diff = 0
    ins_com = 0
    ins_acc = 0
    n = range(1,len(random_list))
    P_name = "Insertion"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    for i in n:
        key = random_list[i]
        j = i - 1
        # actual swap
        while j >= 0 and key < random_list[j]:
            random_list[j + 1] = arr[j]
            j -= 1
        # no swap
        else:
            ins_acc += 2
            ins_com += 1
        random_list[j+1] = key
    # >>
    end = time.time()
    ins_diff = round(end - start,ndigits=4)
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
""" Description of the Merge Algo
    This algo splits list two-times in halves. And merges to halves in sorted list(recursively).
    Like divide and conquer. From top to middle from middle to bottom.
"""
def merge_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global mer_diff
    # set comparison in sorting as global
    global mer_com
    # set accesses in sorting as global
    global mer_acc
    # set variables to 0
    mer_diff = 0
    mer_com = 0
    mer_acc = 0
    n = len(random_list)
    P_name = "Merge"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    random_list = sorted(random_list)
    # >>
    end = time.time()
    mer_diff = round(end - start,ndigits=4)
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

# Quick
""" Description of the Quick Algo
    This algo is 
"""
def quick_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global qui_diff
    # set comparison in sorting as global
    global qui_com
    # set accesses in sorting as global
    global qui_acc
    # set variables to 0
    qui_diff = 0
    qui_com = 0
    qui_acc = 0
    n = len(random_list)
    P_name = "Quick"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    random_list = sorted(random_list)
    # >>
    end = time.time()
    qui_diff = round(end - start,ndigits=4)
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

# Heap
""" Description of the Heap Algo

"""
def heap_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global hea_diff
    # set comparison in sorting as global
    global hea_com
    # set accesses in sorting as global
    global hea_acc
    # set variables to 0
    hea_diff = 0
    hea_com = 0
    hea_acc = 0
    n = len(random_list)
    P_name = "Heap"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    random_list = sorted(random_list)
    # >>
    end = time.time()
    hea_diff = round(end - start,ndigits=4)
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

# Counting
""" Description of the Counting Algo

"""
def counting_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global cou_diff
    # set comparison in sorting as global
    global cou_com
    # set accesses in sorting as global
    global cou_acc
    # set variables to 0
    cou_diff = 0
    cou_com = 0
    cou_acc = 0
    n = len(random_list)
    P_name = "Counting"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    random_list = sorted(random_list)
    # >>
    end = time.time()
    cou_diff = round(end - start,ndigits=4)
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

# Radix
""" Description of the Radix Algo

"""
def radix_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global rad_diff
    # set comparison in sorting as global
    global rad_com
    # set accesses in sorting as global
    global rad_acc
    # set variables to 0
    rad_diff = 0
    rad_com = 0
    rad_acc = 0
    n = len(random_list)
    P_name = "Radix"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    random_list = sorted(random_list)
    # >>
    end = time.time()
    rad_diff = round(end - start,ndigits=4)
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

# Bucket
""" Description of the Bucket Algo

"""
def bucket_algo(random_list,sorted_list):
    # set difference in time later as float to global
    global buc_diff
    # set comparison in sorting as global
    global buc_com
    # set accesses in sorting as global
    global buc_acc
    # set variables to 0
    buc_diff = 0
    buc_com = 0
    buc_acc = 0
    n = len(random_list)
    P_name = "Bucket"
    # create a border
    print(len(P_name + P_Algo_init) * "#")
    print(P_name + P_Algo_init)
    start = time.time()
    # Algorithm sorting area
    # >>
    random_list = sorted(random_list)
    # >>
    end = time.time()
    buc_diff = round(end - start,ndigits=4)
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

        insertion_algo(random_list,sorted_list)
        print("---seconds %s---"%(ins_diff))
        print("---accesses %s---"%(ins_acc))
        print("---compairments %s---"%(ins_com))

        merge_algo(random_list,sorted_list)
        print("---seconds %s---"%(mer_diff))
        print("---accesses %s---"%(mer_acc))
        print("---compairments %s---"%(mer_com))

        quick_algo(random_list,sorted_list)
        print("---seconds %s---"%(qui_diff))
        print("---accesses %s---"%(qui_acc))
        print("---compairments %s---"%(qui_com))

        heap_algo(random_list,sorted_list)
        print("---seconds %s---"%(hea_diff))
        print("---accesses %s---"%(hea_acc))
        print("---compairments %s---"%(hea_com))

        counting_algo(random_list,sorted_list)
        print("---seconds %s---"%(cou_diff))
        print("---accesses %s---"%(cou_acc))
        print("---compairments %s---"%(cou_com))

        radix_algo(random_list,sorted_list)
        print("---seconds %s---"%(rad_diff))
        print("---accesses %s---"%(rad_acc))
        print("---compairments %s---"%(rad_com))

        bucket_algo(random_list,sorted_list)
        print("---seconds %s---"%(buc_diff))
        print("---accesses %s---"%(buc_acc))
        print("---compairments %s---"%(buc_com))

        # Ranking all Algos
        # Name of Algo, 1. Time, 2. Comparisons, 3. Accesses

        # After all algos
        print(P_exit)
    else:
        print(P_exit)

if __name__ == "__main__":
    main()
