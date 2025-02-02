
'''
Review Exercise2
-----------------

Process the 'show_arp.txt' file and create a data structure from it.

1. Create a dictionary where the keys are the ip addresses and the corresponding 
   values are the mac-addresses.

2. Create a second dictionary where the keys are the mac-addresses and the 
   corresponding values are the ip addresses.

3. Use rich.print to print these two data structures to the screen.



Your output should look something like the following:


IP Address to Mac mapping
--------------------------------------------------
{'10.220.88.1': '0062.ec29.70fe',
 '10.220.88.20': 'c89c.1dea.0eb6',
 '10.220.88.21': '1c6a.7aaf.576c',
 '10.220.88.28': '5254.aba8.9aea',
 '10.220.88.29': '5254.abbe.5b7b',
 '10.220.88.30': '5254.ab71.e119',
 '10.220.88.32': '5254.abc7.26aa',
 '10.220.88.37': '0001.00ff.0001',
 '10.220.88.38': '0002.00ff.0001',
 '10.220.88.39': '6464.9be8.08c8',
 '10.220.88.40': '001c.c4bf.826a',
 '10.220.88.41': '001b.7873.5634'}



Mac Address to IP mapping
--------------------------------------------------
{'0001.00ff.0001': '10.220.88.37',
 '0002.00ff.0001': '10.220.88.38',
 '001b.7873.5634': '10.220.88.41',
 '001c.c4bf.826a': '10.220.88.40',
 '0062.ec29.70fe': '10.220.88.1',
 '1c6a.7aaf.576c': '10.220.88.21',
 '5254.ab71.e119': '10.220.88.30',
 '5254.aba8.9aea': '10.220.88.28',
 '5254.abbe.5b7b': '10.220.88.29',
 '5254.abc7.26aa': '10.220.88.32',
 '6464.9be8.08c8': '10.220.88.39',
 'c89c.1dea.0eb6': '10.220.88.20'}

'''

with open("show_arp.txt") as my_file:
    show_ip = my_file.read()

print(show_ip)

my_ds = {}