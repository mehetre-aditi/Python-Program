dict={'Mon':3,'Tue':4,'Wed':5,'Thu':6}
print("The given dictionary: ",dict)

check_key=input("Enter key to check: ")
check_value=input("Enter value: ")

if check_key in dict:
    print("key is present")
    dict[check_key]=check_value
else:
    print("key is not present")
    dict[check_key]=check_value
print("Updated Dictionary:",dict)