class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def props(x):
    newDict=dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))
    dict2={}
    dict2['first_name']= newDict['first_name']
    dict2['last_name']= newDict['last_name']
    dict2['father']= newDict['father']
    return dict2
    #return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))

def print_object_depth(data, start=0):
    values = props(data)
    for key, value in values.items():
        print(key+':', start + 1)
        if isinstance(value, Person):
            print_object_depth(value, start + 1)

def print_depth(data, start=0):

    for key, value in data.items():
        if isinstance(value, dict):
            print(key, start + 1)
            print_depth(value, start=start+1)

        elif isinstance(value, Person):
            print(key+':', start + 1)
            print_object_depth(value, start + 1)
            break
        else:
            print(key, start + 1)

def inputDict():

    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)

    a = {
     "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
                    }
            },
        }
    return a

if __name__ == '__main__':
    a=inputDict()
    print_depth(a)
