import webiopi
import subprocess

GPIO = webiopi.GPIO
def setup():
	pass
def loop():
	pass
def destroy():
	pass
@webiopi.macro
def temperature():
	result = subprocess.check_output("hostnamectl", shell=True)
	#return result[5:11]
	return result[:]
@webiopi.macro
def read_text_file():
    file_path = "/home/user/blood_pressure_03.txt"
    lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines
        
@webiopi.macro
def blep_request():
    options = [
        "Option 1: /macro/blep_01",
        "Option 2: /macro/blep_02",
        "Option 3: /macro/blep_03",
        "Option 4: /macro/blep_04\n"
    ]
    
    for option in options:
        print(option)

    return "\n".join(options)
    
@webiopi.macro   
def blep_01():
    file_path = "/home/user/blood_pressure_01.txt"
    lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines
    
@webiopi.macro    
def blep_02():
    file_path = "/home/user/blood_pressure_02.txt"
    lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines
    
@webiopi.macro    
def blep_03():
    file_path = "/home/user/blood_pressure_03.txt"
    lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines
    
@webiopi.macro    
def blep_04():
    file_path = "/home/user/blood_pressure_04.txt"
    lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines
