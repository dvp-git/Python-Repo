# Iterable protocols

#Demonstration of iterable or not
def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")

List_test = first(["1st","2nd","Three"])
print(List_test)

Dict_test = first({"again","under","Three"})
print(Dict_test)

print(first(set()))
