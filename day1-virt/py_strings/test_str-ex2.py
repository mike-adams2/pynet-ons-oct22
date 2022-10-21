#!/usr/bin/env python

#a. Create a python script that prompts for an IP address.
#b. Use #! at top of file; make executable
#c. split on '.'      
#d. Print out four octets with column width of 12; left aligned.
#e. Check your code into git & github

ipaddr = input("IP Address: ")
octets = ipaddr.split(".")

print()
print(f"{octets[0]:<10}{octets[1]:<12}{octets[2]:<12}{octets[3]:<12}")
print()


#line
print(ipaddr)

#new line