
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

def inputDict():
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
                }
            }
        }
    return a

if __name__ == '__main__':
    a=inputDict()
    print_depth(a)
