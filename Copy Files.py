from sys import argv
from os.path import exists #to check path exists or not

script, from_file, to_file = argv


print(f"Copying from {from_file} to {to_file}, be patient...")

in_file = open(from_file, encoding = 'UTF-8') #We are taking read only #Encoding is optional by default it is cp1252
print(">>>>>>>> in_file", repr(in_file)) # to check the in_file raw format
data = in_file.read()

print(f"The input file is {len(data)} bytes long") #gives byte size

print(f"Does the output file exist? {exists(to_file)}") # Will op true(exist) or false(not exist)
print("Ready, hit RETURN to continue, CTRL-C CTRL^C to abort.")
input()


out_file = open(to_file, 'w')
out_file.write(data) #will write copied data

print("Successful")

out_file.close()
in_file.close()