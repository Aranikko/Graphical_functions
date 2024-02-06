import subprocess

def install_packages(package_list):
    for package in package_list:
        subprocess.call(['pip', 'install', package])
    
packages_to_install = ['customtkinter', 'Pillow', 'matplotlib', 'numpy'] # Добавьте сюда необходимые библиотеки

# Установка библиотек
install_packages(packages_to_install)
