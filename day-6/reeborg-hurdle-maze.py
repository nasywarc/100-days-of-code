# def turn_right() :
#     turn_left()
#     turn_left()
#     turn_left()

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

# def left_is_clear() :
#     turn_around()
#     right_is_clear()
#     turn_around()

# def search() :
#     while not at_goal() :
#         while front_is_clear() or right_is_clear():
#             if right_is_clear() and not at_goal() :
#                 turn_right()
#                 move()
#             else :
#                 if not at_goal() :
#                     move()
#                 else :
#                     break
#         turn_around()

# i = 0
# while not at_goal() :
#     search()
