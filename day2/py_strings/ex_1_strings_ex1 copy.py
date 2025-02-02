'''
with open("aruba_show_ap_database.txt") as aruba_file:
    ap_database = aruba_file.read()

header = True
footer = False
print()
for line in ap_database.splitlines():
    # Strip header and footer information
    if header:
        if "Name" in line and "Standby IP" in line:
            header = False
        continue
    elif "---------" in line:
        continue
    elif footer:
        continue

    if "Flags" in line and "Unprovisioned" in line:
        footer = True
        continue
    print(line)

Read in the “aruba_show_ap_database.txt” file.

Process the data such that all of the header and footer information is excluded.

In other words, only print out the tabular data from the file. Your output should look as follows:

-----------------
library-1          sjc      225      10.10.10.13  Up 8m:29s     Rc2    10.5.200.21    0.0.0.0
library-1          sjc      225      10.10.10.10  Down          Rc2    10.5.200.21    0.0.0.0
library-2          sjc      225      10.10.10.12  Down          Rc2    10.5.200.21    0.0.0.0
rm135-1            sjc      135      10.10.10.9   Down          Rc2    10.5.200.21    0.0.0.0
rm135-2            sjc      135      10.10.10.11  Down          Rc2    10.5.200.21    0.0.0.0
rm137-1            sjc      225      192.168.1.1  Up 1h:2m:05s  R      10.5.200.21    0.0.0.0
rm137-2            sjc      225      10.10.10.8   Down          Rc2    10.5.200.21    0.0.0.0
-----------------


'''


