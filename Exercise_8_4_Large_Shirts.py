# Modify the make_shirt() function so that shirts are large 
# by defaut with a message that reads I love Python. Make
# a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

def make_shirt(text, size='l'):
    """Display information about shirt"""
    print(f"Shirt size {size.upper()} with print '{text}' on it")

make_shirt('I love Python')
make_shirt('I love Games', 'XL')