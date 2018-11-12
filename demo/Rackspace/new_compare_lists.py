""" Compare two lists element by element """
import sys

# list1 = ['VDS cPanel, managed, tsohost']
# list1 = ['Daily']
list1 = [None]
list2 = ['managed, VDS cPanel, tsohost']

# If one of the lists is emty return False
if (
    len(list1) == 0
    or len(list2) == 0
    or None in list1
    or None in list2
):
    print("Return False")
    sys.exit(1)    

new1 = list1[0].split(', ')
new2 = list2[0].split(', ')
for item in new1:
    # breakpoint()
    for item2 in new2:
        if str(item) == str(item2):
            break
    else:
        print("Return Flase")
        sys.exit()

print("Return True")
