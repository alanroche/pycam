import subprocess

directory_list = subprocess.check_output(['ls', '-l']).split("\n")

for line in directory_list:
    filename = line.split(" ")[-1]
    if filename.endswith(".py"):
        print filename.upper()
