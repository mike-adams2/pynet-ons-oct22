'''
Loops Exercise 1
----------------

1. Read the ‘show_ip_bgp.txt’ file.

2. Strip out the BGP header information so you are just left with the route table.

3. Parse each BGP line such that you retrieve the prefix and the as_path.

4. Save the prefix and as_path to a file.
'''


with open("show_ip_bgp.txt") as my_file:
    show_bgp = my_file.read()

print(show_bgp)

