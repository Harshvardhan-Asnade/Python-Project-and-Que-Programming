info = {
    "name": "Harsh",  
    "skills": {
     "C++": "DSA",
     "Python": "Basic",
    }, 
    "age": 18,  
       
    
}  
print(info)
print("\n")
#1 dic.keys
print( info.keys())
print("\n")
#2 Dic.value()
print(info.values())
# items
print("\n")
print(info.items())
# 3 get
print("\n")
print(info.get("skills"))
#4 update 
New_info={"height" : 5.8}
info.update(New_info)
print(info) 