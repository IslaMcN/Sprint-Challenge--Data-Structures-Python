import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


##Sort them first so that I can use comparision ops in my dupes function
names_1_sorted = sorted(names_1)
names_2_sorted = sorted(names_2)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#Using Binary Search
def dupes(o, t):
    #first in array
    begin = 0
    #last in array
    end = len(o) - 1
    while begin <= end:
        #Middle is the begin and the end cut in half
        middle = (begin + end) //2
        mid = o[middle]
        #The comparison itself is done character by character. The order
        #depends on the order of the characters in the alphabet. This 
        # order depends on the character table that is in use on your 
        # machine while executing the Python code.
        # Keep in mind the order is case-sensitive. As an example for 
        # the Latin alphabet, "Bus" comes before "bus".
        if mid > t:
            end = middle - 1
        elif mid < t:
            begin = middle + 1
        else:
            return mid

for name in names_1_sorted:
    names = dupes(names_2_sorted, name)
    if name == names:
        duplicates.append(name)
#Runtime is O(1)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
