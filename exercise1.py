# from the official documentation: python does not have support for arrays, but lists are an ok substitute!
# declaring the lists
ids = [35, 98, 23, 43, 50]
names = ["John", "Peter", "Mariah", "Bill", "Chris"]


# 1 - creating a function to put the ids in crescent order
def sorts_out_ids(id, index):
    smaller_index = index
    for i in range(index + 1, len(id)):
        if id[i][0] < id[smaller_index][0]:
            smaller_index = i
    return smaller_index


# 2 - combining both lists into a tuple
unsorted_ids_and_names = tuple(zip(ids, names))

# 3 - had to turn the tuple back into a list to proceed, could not figure out yet how to do it with tuples
ids_and_names = list(unsorted_ids_and_names)
print(ids_and_names)

# 4 - sorting out items by crescent order
for i in range(len(ids_and_names) - 1):  # using len - 1 to avoid an out of range error since arrays/lists start at 0
    lowerIdIndex = sorts_out_ids(ids_and_names,
                                 i)  # for each item we have to check if there exists an index with a smaller number
    if i != lowerIdIndex:  # checks if [i] current item is different from the smallest index...
        ids_and_names[i], ids_and_names[lowerIdIndex] = ids_and_names[lowerIdIndex], ids_and_names[i]  # and if so and
        # [i] is greater they switch positions

print(ids_and_names)
# 5 - switching original id numbers for sequential 1-5 numbers
for i in range(len(ids_and_names)):
    ids_and_names[i] = (i + 1, ids_and_names[i][1])

print(ids_and_names)

# 6 - switching out names that have even ids for N/A
for i in range(len(ids_and_names)):
    if ids_and_names[i][0] % 2 == 0:  # checking if the ids are even
        ids_and_names[i] = (ids_and_names[i][0], "N/A") # switching the names of even ids

print(ids_and_names)
