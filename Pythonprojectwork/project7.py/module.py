# File Operations Module

def create_file(filename):
    """Create a new file."""
    try:
        with open(filename, "w") as file:
            file.write("")
        print(f"{filename} created successfully!")

    except OSError as e:
        print(f"Error: {e}")


def write_file(filename, content):
    """Write data into a file."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Data saved in {filename}!")

    except OSError as e:
        print(f"Error: {e}")


def read_file(filename):
    """Read data from a file."""
    try:
        with open(filename, "r") as file:
            data = file.read()
        print(f"\nContent of {filename}:")
        print(data)

    except FileNotFoundError:
        print(f"{filename} does not exist!")

    except OSError as e:
        print(f"Error: {e}")


def append_file(filename, content):
    """Add new data at the end of a file."""
    try:
        with open(filename, "a") as file:
            file.write("\n" + content)
        print(f"New data added to {filename}!")

    except OSError as e:
        print(f"Error: {e}")


