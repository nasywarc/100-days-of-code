# def turn_right() :
#     turn_left()
#     turn_left()
#     turn_left()

# def left_is_clear():
#     turn_left()
#     turn_left()
#     right_is_clear()

# def turn_around() :
#     turn_left()
#     turn_left()

# def jump() :
#     turn_left()
#     move()
#     global i
#     i+=1
#     turn_right()
#     if front_is_clear():
#         move()
#         turn_right()
#         for i in range (0, i):
#             move()
#         i = 0
#         turn_left()
#     else :
#         jump()

# def search() :
#     turn = 0
#     if right_is_clear() and turn < 4:
#         turn_right()
#         while front_is_clear():
#             move()
#             turn+=1
#             if not at_goal() :
#                 search()
#     else :
#         turn_around()
#         move()
#         search()

# i = 0
# found = False
# while not at_goal() :
#     search()
