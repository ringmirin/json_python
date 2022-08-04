###3. Write a Python program to convert Python objects into JSON strings. 
###Print all the values. 

# import json
# python_obj={"Name":"David","Age":6}
# python_str="Python string"
# json_obj=json.dumps(python_obj)
# json_str=json.dumps(python_str)
# print(json_obj)
# print(json_str)


import json
python_data={"color":"blue","size":"small","code":123}
# print(python_data)
# print(json.dumps(python_data,sort_keys=True,indent=4))

print(python_data)
json_data=json.dumps(python_data)
