# ============================================================
#   PYTHON NOTES: Dictionary & Set
#   Author  : [Your Name]
#   GitHub  : [Your GitHub]
# ============================================================


# ────────────────────────────────────────────────────────────
# 1. DICTIONARY  (mutable, ordered*, key-value pairs, no duplicate keys)
#    * ordered since Python 3.7+
# ────────────────────────────────────────────────────────────

# --- Creating a dictionary ---
student = {"name": "Alice", "age": 21, "city": "Jaipur"}
empty_d = {}                                    # empty dict
also_d  = dict(name="Bob", age=25)             # using dict() constructor

# --- Accessing values ---
print(student["name"])            # Alice
print(student.get("age"))        # 21
print(student.get("grade", "N/A"))  # N/A  (default if key missing)
# student["grade"]              # ❌ KeyError if key doesn't exist → use .get()

# --- Adding & updating ---
student["grade"] = "A"            # add new key
student["age"]   = 22             # update existing key
student.update({"city": "Delhi", "score": 95})  # update multiple at once

# --- Removing from a dictionary ---
removed = student.pop("score")    # removes key & returns its value
student.popitem()                 # removes & returns last inserted (key, value)
del student["grade"]              # delete by key
student.clear()                   # empty the whole dict

# --- Dictionary methods ---
info = {"name": "Alice", "age": 21, "city": "Jaipur"}

print(info.keys())    # dict_keys(['name', 'age', 'city'])
print(info.values())  # dict_values(['Alice', 21, 'Jaipur'])
print(info.items())   # dict_items([('name', 'Alice'), ('age', 21), ('city', 'Jaipur')])

copy_info = info.copy()           # shallow copy
info.setdefault("grade", "A")    # add key only if it doesn't exist

# --- Looping through a dictionary ---
for key in info:
    print(key, "→", info[key])

for key, value in info.items():
    print(f"{key}: {value}")

for value in info.values():
    print(value)

# --- Membership test (checks keys by default) ---
print("name" in info)             # True
print("Alice" in info.values())   # True

# --- Dictionary comprehension ---
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

filtered = {k: v for k, v in squares.items() if v > 5}
# {3: 9, 4: 16, 5: 25}

# --- Nested dictionary ---
employees = {
    "emp1": {"name": "Alice", "dept": "Engineering"},
    "emp2": {"name": "Bob",   "dept": "Marketing"},
}
print(employees["emp1"]["name"])   # Alice

# --- Merging dictionaries ---
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}

merged = {**d1, **d2}              # d2 values overwrite d1 on conflicts
# OR (Python 3.9+)
merged = d1 | d2

# --- Counting with dict (frequency map) ---
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)   # {'apple': 3, 'banana': 2, 'cherry': 1}

# Cleaner with collections.Counter
from collections import Counter
freq2 = Counter(words)
print(freq2.most_common(2))   # [('apple', 3), ('banana', 2)]

# --- defaultdict (auto-creates missing keys) ---
from collections import defaultdict

groups = defaultdict(list)
data = [("fruits", "apple"), ("veggies", "carrot"), ("fruits", "banana")]
for category, item in data:
    groups[category].append(item)
print(dict(groups))
# {'fruits': ['apple', 'banana'], 'veggies': ['carrot']}

# --- OrderedDict (keeps insertion order — mostly for older Python) ---
from collections import OrderedDict
od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3


# ────────────────────────────────────────────────────────────
# 2. SET  (mutable, unordered, no duplicates, not subscriptable)
# ────────────────────────────────────────────────────────────

# --- Creating a set ---
fruits  = {"apple", "banana", "cherry"}
nums    = {1, 2, 3, 4, 5}
empty_s = set()           # IMPORTANT: {} creates a dict, NOT a set!

# --- From a list (removes duplicates automatically) ---
raw   = [1, 2, 2, 3, 4, 4, 5]
clean = set(raw)          # {1, 2, 3, 4, 5}

# --- Sets are UNORDERED → no indexing ---
# fruits[0]              # ❌ TypeError: 'set' object is not subscriptable

# --- Adding & removing ---
fruits.add("mango")          # add one element
fruits.update(["kiwi", "grape"])  # add multiple elements

fruits.remove("banana")      # removes; raises KeyError if not found
fruits.discard("banana")     # removes; NO error if not found
popped_s = fruits.pop()      # removes & returns a random element
fruits.clear()               # empties the set

# --- Membership test (very fast — O(1)) ---
colors = {"red", "green", "blue"}
print("red" in colors)       # True
print("yellow" not in colors)  # True

# ── SET OPERATIONS ───────────────────────────────────────────

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union – all elements from both
print(A | B)              # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))         # same

# Intersection – only common elements
print(A & B)              # {4, 5}
print(A.intersection(B))  # same

# Difference – in A but NOT in B
print(A - B)              # {1, 2, 3}
print(A.difference(B))    # same

# Symmetric Difference – in A or B but NOT both
print(A ^ B)                       # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))   # same

# ── SET RELATIONSHIP METHODS ─────────────────────────────────

X = {1, 2}
Y = {1, 2, 3, 4}

print(X.issubset(Y))       # True  – all of X is in Y
print(Y.issuperset(X))     # True  – Y contains all of X
print(X.isdisjoint({5,6})) # True  – no common elements

# ── IN-PLACE SET OPERATIONS ──────────────────────────────────

A |= {9, 10}               # update A with union
A &= {1, 2, 9}             # keep only intersection
A -= {9}                   # remove elements in right set
A ^= {1}                   # symmetric difference in-place

# ── FROZEN SET (immutable set — can be used as dict key) ─────

fs = frozenset([1, 2, 3])
# fs.add(4)               # ❌ AttributeError: frozenset has no .add()
lookup = {fs: "triangle"}  # ✅ valid dict key


# ────────────────────────────────────────────────────────────
# 3. DICT  vs  SET  – Quick Reference
# ────────────────────────────────────────────────────────────
#
#  Feature          | Dictionary          | Set
#  -----------------+---------------------+---------------------
#  Syntax           | {key: value}        | {value}  or set()
#  Mutable          | ✅ Yes               | ✅ Yes
#  Ordered          | ✅ Yes (3.7+)        | ❌ No
#  Duplicates       | ❌ No (keys unique)  | ❌ No
#  Indexing         | By key              | ❌ Not supported
#  Lookup speed     | O(1) avg            | O(1) avg
#  Use when         | Key-value mapping   | Unique items / math ops
#  Immutable ver.   | types.MappingProxy  | frozenset
#
# ────────────────────────────────────────────────────────────


# ────────────────────────────────────────────────────────────
# 4. COMMON PATTERNS
# ────────────────────────────────────────────────────────────

# Pattern 1: Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# Pattern 2: Group items by a property using dict
people = [
    {"name": "Alice", "dept": "Eng"},
    {"name": "Bob",   "dept": "HR"},
    {"name": "Carol", "dept": "Eng"},
]
by_dept = {}
for p in people:
    by_dept.setdefault(p["dept"], []).append(p["name"])
print(by_dept)   # {'Eng': ['Alice', 'Carol'], 'HR': ['Bob']}

# Pattern 3: Remove duplicates while preserving order (dict trick)
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_ordered = list(dict.fromkeys(items))
print(unique_ordered)   # [3, 1, 4, 5, 9, 2, 6]

# Pattern 4: Find common elements between two lists using sets
list1 = ["apple", "banana", "cherry", "mango"]
list2 = ["banana", "mango", "grape"]
common = set(list1) & set(list2)
print(common)   # {'banana', 'mango'}

# Pattern 5: Check if two strings are anagrams
def are_anagrams(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False


# ────────────────────────────────────────────────────────────
# 5. PRACTICE EXERCISES
# ────────────────────────────────────────────────────────────

# Exercise 1: Count character frequency in a string using a dict.
text = "mississippi"
char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print(char_freq)   # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# Exercise 2: Find unique elements across three lists using sets.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = [5, 6, 7, 8]
all_unique = set(a) | set(b) | set(c)
print(sorted(all_unique))   # [1, 2, 3, 4, 5, 6, 7, 8]

# Exercise 3: Find elements ONLY in list a (not in b or c).
only_in_a = set(a) - set(b) - set(c)
print(only_in_a)   # {1, 2}

# Exercise 4: Build a phone book and look up numbers safely.
phonebook = {"Alice": "9876543210", "Bob": "9123456780"}
phonebook["Carol"] = "9988776655"   # add entry
name = "Dave"
print(phonebook.get(name, f"{name} not found"))   # Dave not found

# Exercise 5: Dict comprehension – convert Celsius to Fahrenheit.
celsius    = {"Delhi": 42, "Jaipur": 45, "Mumbai": 35, "Shimla": 18}
fahrenheit = {city: (temp * 9/5) + 32 for city, temp in celsius.items()}
print(fahrenheit)
# {'Delhi': 107.6, 'Jaipur': 113.0, 'Mumbai': 95.0, 'Shimla': 64.4}