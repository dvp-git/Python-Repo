## File like behaviours [ Polymorphism]
from urllib.request import urlopen


def words_per_line(FileLikeObject):
    """ Read the number of words per line in the file"""
    return [len(line.split()) for line in FileLikeObject.readlines()]


### Using the fucntion on a text file
with open('wasteland.txt', mode = 'rt', encoding = 'utf-8') as read_file:
    wpl = words_per_line(read_file)


print(wpl)
print("Text file type is {}".format(type(read_file)))     # Text_type : _io.TextIOWrapper'>



## using the function on a URL HTTP file
with urlopen("https://sixty-north.com/c/t.txt") as web_file:
    wpl = words_per_line(web_file)

print(wpl)
print("HTTP fetched file type is {}".format(type(read_file)))    # Type : http.client.HTTPResponse


# Both executes file like behavious, since both are file-like objects
