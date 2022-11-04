def read_file(filename):
    with open(filename) as f:
        return f.read()


def find_serial_number(show_version):
    for line in show_version.splitlines():
        if "Processor board ID" in line:
            fields = line.split()
            serial_number = fields[-1]
            return serial_number


show_ver = read_file("show_version.txt")
my_serial_number = find_serial_number(show_ver)
print(f"\n\nSerial Number: {my_serial_number}\n\n")
