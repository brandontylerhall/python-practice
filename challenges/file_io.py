from pathlib import Path

# file name turned into variable
filename = 'demo_file.txt'
path = Path(filename)

# this happens if the file exists
if path.is_file():
    with open('demo_file.txt', 'r') as file:
        # find how many lines are in a file
        """
        line_count = 0

        for line in file:
            line_count += 1
        print(f'There are {line_count} lines')
        """

        # counts and prints the number of words in a file
        """
        word_count = 0
        for line in file:
            for word in line.split():
                word_count += 1
        print(f'There are {word_count} words')
        """
    file.close()
    # opened in append mode
    with open('demo_file.txt', 'a') as file:
        file.write(f'\nthis information is appended to the file! (again)')
    file.close()
    




# creates a file at this name if one doesn't exist already
else:
    io_demo = open('demo_file.txt', 'x')
    io_demo.write('Hello world!')
    io_demo.close()
