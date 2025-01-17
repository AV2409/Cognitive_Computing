# 4
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# 4-i
u = A.union(B)
print(f"Unique scores achieved by both teams: {u}")

# 4-ii
i = A.intersection(B)
print(f"Scores common to both teams: {i}")

# 4-iii
sd = A.symmetric_difference(B)
print(f"Scores exclusive to each team: {sd}")

# 4-iv
is_A_subset = A.issubset(B)
is_B_superset = B.issuperset(A)
print(f"Are the scores of team A a subset of team B? {is_A_subset}")
print(f"Are the scores of team B a superset of team A? {is_B_superset}")

# 4-v
X = int(input("Enter the score to remove from team A: "))
if X in A:
    A.remove(X)
    print(f"Score {X} has been removed from team A. Updated set A: {A}")
else:
    print(f"Score {X} is not present in team A.")