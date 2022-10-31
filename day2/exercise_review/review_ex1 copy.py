

from rich import print

'''
with open("show_ip_int_brief.txt") as my_file:
    show_ip = my_file.read()


my_ds = {}
for line in show_ip.splitlines():
    if "Interface" in line and "Protocol" in line:
        continue

    intf, ip_addr, _, _, line_status, line_protocol = line.split()
    my_ds[intf] = line_protocol

print()
print(my_ds)
print()

Review Exercise1
-----------------

Process the 'show_ip_int_brief.txt' file and create a data structure from it.

Process the 'show_ip_int_brief.txt' file and create a data structure from it.

1. Create a dictionary where the keys are the interface names

2. The corresponding values should be the line “Protocol” field.
  
3. Use rich.print to print out your data structure.
'''

with open("show_ip_int_brief.txt") as my_file:
    show_ip = my_file.read()

print(show_ip)

my_ds = {}
for line in show_ip.splitlines():
    if "Interface" in line and "Protocol" in line:
        continue
    
    intfs, ip_addr, _, _, line_stat, Line_Protocol = line.split()
    my_ds[intfs] = Line_Protocol
    
print(my_ds)