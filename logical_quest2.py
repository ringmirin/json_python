# j_str={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}

# import json
# j_str={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# new_str=json.dumps(j_str, sort_keys=True)
# print(new_str)


n=int(input("enter the number: "))
if n%2!=0:
    print("weird")
elif n%2==0:
    if n<=2 or n>=5:
        print("not weird")
elif n%2==0:
    if n<=6 or n>=20:
        print("weird")
elif n%2==0:
    if n>20:
        print("not weird")