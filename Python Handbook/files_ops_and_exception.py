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

# you can use for loop on file_object to read file line by line,
# remember that each line if printed, will have an implicit blank line
# consider the code below

with open("alpha.txt", "r", encoding="utf-8") as file_object:
    for each_lines in file_object:
        print(each_lines)

# you can store lines as list if you want to access them outside of "with" block
# or do some manipulation on the read data

with open("alpha.txt", "r", encoding="utf-8") as file_object:
    lines: list[str] = [line.rstrip() for line in file_object.readlines()]

print(lines)

# different kinds of modes with which files can be opened are: r(for read), w(for write)
# a(for append), r+(for read/write)

# open() creates a file if doesn't exists
with open("greetings.txt", "w", encoding="utf-8") as file_object:
    file_object.write("Hello World!!")

# python can only insert string to a text file, type casting to string is required
# if you are trying to insert data other than string

# when writing multiple lines to a text file, remember to add new line like \n, \r, etc.
# as python won't add a new line after writing a line in text file

# EXCEPTIONS
# exceptions are special objects that python uses to manage errors
# that arises during program execution

# you can use try-except or try-except-else block to handle exceptions
# syntax:
# try:
    # code block that may produce an error
# except <EXCEPTION_NAME>:
    # code block that will run in case of error
# else:
    # code block that will only run if try block is executed successfully (else block is optional)

try:
    result = 5/0
except ZeroDivisionError:
    print("You can't divide a number by zero")
else:
    # will never be executed in this case, but if the expression in try block was valid,
    # result would be printed
    print(result)

# when exception occurs and it's not handled, the program execution halts

# you can use "pass" keyword in except block if you want to program to execute
# and do nothing in case exception occured
