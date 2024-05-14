"""file manipulation and exceptions and errors"""

# you can read an entire file at once or one line at a time

# "with" usage closes the file once its access is no longer needed
# therefore we don't have to use close() to close the file which is mandatory otherwise
with open("pi.txt", "r", encoding="utf-8") as file_object:
    content = file_object.read() # reads complete content of a file and puts it in a variable
    # difference between file output and printed content is that
    # printed content has extra blank line at the end(which occurs because read() returns
    # an empty line once it reaches the end of file which shows up as blank line,
    # use rstrip() or strip() to remove it)
    print(content)
