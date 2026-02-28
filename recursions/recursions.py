# #  HEAD RECURSION
# count = 0
# def greet():
#     global count
#     if count == 4:
#         return
#     print("Rehan")
#     count += 1
#     greet()
# greet()

# # TAIL RECURSION
# count = 0
# def greet():
#     global count
#     if count == 4:
#         return
#     count += 1
#     greet()
#     print("Rehan")
# greet()


count = 0
def greet():
    global count
    if count == 4:
        return
    greet()
    count += 1
    print("Rehan")
greet()

