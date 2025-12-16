def passes_check():
    password = "mohey123"
    passes = input("please enter password")
    while len(passes)<6 or passes != password:
        passes = input("please enter password\n incorrect pass try agan")
    return "access granted"
x=passes_check()
print(x)














