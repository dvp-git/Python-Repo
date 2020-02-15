# Stateful generators


def take(count,iterable):
    """ Take items from the front of an iterable

    Args :
        count : The maximum number of items to be taken
        iterable: The sequence of items

    Yields:
        At most 'count' items from 'iterable' """

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    """ Removes the duplicates and gives only distinct items

    Args:
        iterable : The sequence of items

    Yields:
        Unique elements of the iterable"""
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_pipeline():
    items = [1,3,4,1,35,6,7,1,43]
    for item in take(3,distinct(items)):
        print(type(distinct(items)))
        print(item)

# def run_take():
#     iterable = [1,1,2,4,5,7,6,2,4,5,6,7]
#     for item in distinct(iterable):
#         print(item)
#         print(type(item))




if '__main__' == __name__:
    run_pipeline()
