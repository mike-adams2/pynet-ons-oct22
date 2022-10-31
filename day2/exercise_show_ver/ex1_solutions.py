f = open("show_version.txt") 

data = f.read()


#do for to print all lines with text string

for line in data.splitlines():
    if "Processor board ID" in line:
        print(line)
        fields = line.split()
        serial_number = fields[-1]
        print(serial_number)
        print(f"\n\nSerial Number: {serial_number}\n\n")
        
f.close