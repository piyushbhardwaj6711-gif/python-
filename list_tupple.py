# ============================================================
#   PYTHON NOTES: Lists & Tuples
# ============================================================


# ────────────────────────────────────────────────────────────
# 1. LIST  (mutable, ordered, allows duplicates)
# ────────────────────────────────────────────────────────────

# --- Creating a list ---
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "hello", 3.14, True]        # can hold different types
empty  = []                               # empty list

# --- Accessing elements (0-indexed) ---
print(fruits[0])       # apple
print(fruits[-1])      # cherry  (negative = from the end)

# --- Slicing  [start : stop : step] ---
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])       # [1, 2, 3]
print(nums[::2])       # [0, 2, 4]  (every 2nd element)
print(nums[::-1])      # [5, 4, 3, 2, 1, 0]  (reversed)

# --- Modifying a list ---
fruits[1] = "mango"            # update
fruits.append("grape")         # add to end
fruits.insert(1, "kiwi")       # insert at index 1
fruits.extend(["lemon", "lime"])  # add multiple items

# --- Removing from a list ---
fruits.remove("apple")         # removes first match
popped = fruits.pop()          # removes & returns last item
popped_idx = fruits.pop(0)     # removes & returns item at index 0
del fruits[0]                  # delete by index
fruits.clear()                 # empty the whole list

# --- Common list methods ---
colors = ["red", "blue", "green", "blue"]
print(colors.count("blue"))    # 2  – count occurrences
print(colors.index("green"))   # 2  – first index of value
colors.sort()                  # sort in-place (ascending)
colors.sort(reverse=True)      # sort descending
colors.reverse()               # reverse in-place
copy_colors = colors.copy()    # shallow copy

# --- List comprehension ---
squares = [x**2 for x in range(1, 6)]          # [1, 4, 9, 16, 25]
evens   = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

# --- Nested list (2D / matrix) ---
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][2])    # 6  (row 1, col 2)

# --- Useful built-ins on lists ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))       # 8
print(min(nums))       # 1
print(max(nums))       # 9
print(sum(nums))       # 31
print(sorted(nums))    # returns new sorted list (original unchanged)

# --- Looping ---
for fruit in ["apple", "banana"]:
    print(fruit)

for i, fruit in enumerate(["apple", "banana"]):
    print(i, fruit)    # 0 apple, 1 banana

# --- Membership test ---
print("apple" in ["apple", "banana"])   # True
print("grape" not in ["apple", "mango"])  # True


# ────────────────────────────────────────────────────────────
# 2. TUPLE  (immutable, ordered, allows duplicates)
# ────────────────────────────────────────────────────────────

# --- Creating a tuple ---
point       = (10, 20)
rgb         = (255, 128, 0)
single      = (42,)           # IMPORTANT: trailing comma for 1-element tuple
without_par = 1, 2, 3         # parentheses optional
empty_t     = ()              # empty tuple

# --- Accessing & slicing (same as list) ---
print(point[0])        # 10
print(rgb[-1])         # 0
print(rgb[1:])         # (128, 0)

# --- Tuples are IMMUTABLE ---
# point[0] = 99       # ❌ TypeError: 'tuple' object does not support item assignment

# --- Tuple methods (only 2) ---
data = (1, 2, 2, 3, 2)
print(data.count(2))   # 3  – count occurrences
print(data.index(3))   # 3  – first index of value

# --- Unpacking ---
x, y       = point              # x=10, y=20
a, b, c    = rgb                # a=255, b=128, c=0
first, *rest = (1, 2, 3, 4, 5) # first=1, rest=[2,3,4,5]

# --- Swap variables using tuples ---
a, b = 5, 10
a, b = b, a   # Pythonic swap; a=10, b=5

# --- Named tuple (from collections) ---
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])
p = Person("Alice", 30, "Jaipur")
print(p.name)    # Alice
print(p[1])      # 30   (index access still works)

# --- Tuple as dictionary key (lists cannot be keys) ---
locations = {(26.9124, 75.7873): "Jaipur", (28.6139, 77.2090): "Delhi"}
print(locations[(26.9124, 75.7873)])   # Jaipur

# --- zip() – combine two iterables into tuples ---
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
paired = list(zip(names, scores))   # [('Alice', 95), ('Bob', 87), ('Carol', 92)]

for name, score in zip(names, scores):
    print(f"{name}: {score}")




# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────────────────────
# 4. CONVERSION between list & tuple
# ────────────────────────────────────────────────────────────

my_list  = [1, 2, 3]
my_tuple = tuple(my_list)    # list → tuple
back     = list(my_tuple)    # tuple → list

print(type(my_tuple))        # <class 'tuple'>
print(type(back))            # <class 'list'>


# ────────────────────────────────────────────────────────────
# 5. PRACTICE EXERCISES
# ────────────────────────────────────────────────────────────

# Exercise 1: Create a list of 5 cities and sort them alphabetically.
cities = ["Mumbai", "Delhi", "Jaipur", "Chennai", "Kolkata"]
cities.sort()
print(cities)

# Exercise 2: Remove duplicates from a list using a set, then convert back.
nums_with_dupes = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums_with_dupes))
print(sorted(unique_nums))    # [1, 2, 3, 4, 5]

# Exercise 3: Unpack a tuple returned by a function.
def min_max(data):
    return min(data), max(data)   # returns a tuple

low, high = min_max([4, 7, 1, 9, 2])
print(f"Min: {low}, Max: {high}")

# Exercise 4: List comprehension – filter and transform.
words = ["hello", "world", "python", "is", "fun"]
long_upper = [w.upper() for w in words if len(w) > 3]
print(long_upper)   # ['HELLO', 'WORLD', 'PYTHON']