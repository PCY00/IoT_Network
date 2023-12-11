
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