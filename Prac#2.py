# def pass_v3():
#     real_pass = "mohet123"
#     passes = input("Please Enter Password")
#     attempts = 0
#     while passes != real_pass:
#         print("access denied")
#         passes = input("Please Enter Password")
#         attempts += 1
#         if attempts==4 or real_pass == passes:
#             return "access granted"
#             break
#         else:
#             return "access denied"
#             break
#       pass_v3()
#
# if attempts !=3:
#     return "access granted"
# else:
#     return "access denied"


def pass_v3():
    attempts = 0
    real_pass = "mohet123"
    # passes = input("please enter password")
    while attempts!=3:
        passes = input("please enter password")
        if passes == real_pass:
            print("access granted")
            return True
        else:
            print("access denied wrong pass")
            attempts+=1
        if attempts==3:
            print("you have run out of attempts")
    return False
pass_v3()


