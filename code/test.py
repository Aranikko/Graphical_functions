import os

def check_file_availability(file_name):
    return os.path.exists(file_name)

# Example usage
file_name = "Grap.png"
print(check_file_availability(file_name))