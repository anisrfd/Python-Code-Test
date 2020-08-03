
def print_depth(data, start=0):
    for key, value in data.items():
        print(key, start + 1)
        if isinstance(value, dict):
            print_depth(value, start=start+1)

def print_depth(data):
    stack = [(data, list(data.keys()))]
    while stack:
        val, keys = stack.pop()
        while keys:
            k, keys = keys[0], keys[1:]
            print(k, len(stack) + 1)
            v = val[k]
            if isinstance(v, dict):
                 stack.append((val, keys))
                 stack.append((v, list(v.keys())))
                 break

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
            }
        }
    }

print_depth(a)
