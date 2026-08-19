# Create two sets of numbers and display their union, intersection, difference, and symmetric difference.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union 
union_set = set1.union(set2)
# Intersection
intersection_set = set1.intersection(set2)
# Difference
difference_set = set1.difference(set2)
# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)