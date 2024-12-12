d1 = {'a': 100, 'b': 200, 'c': 300, 'e': 50}
d2 = {'a': 300, 'b': 200, 'd': 400, 'f': 150}

# Task 1: Add two dictionaries (sum values with matching keys)
def add_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

result1 = add_dicts(d1, d2)
print("Ket qua 1:", result1)


# Task 2: Create a new dictionary with larger values for common keys
def merge_dicts(dict1, dict2):
  result = {}
  all_keys = set(dict1.keys()).union(dict2.keys())
  for key in all_keys:
    val1 = dict1.get(key, 0) # Handle keys missing in one dict.
    val2 = dict2.get(key, 0)
    result[key] = max(val1, val2)
  return result

result2 = merge_dicts(d1,d2)
print("Ket qua 2:", result2)

# Task 3: Find the maximum value across both dictionaries
def max_value(dict1, dict2):
    all_values = list(dict1.values()) + list(dict2.values())
    return max(all_values)

result3 = max_value(d1, d2)
print("Ket qua 3:", result3)
