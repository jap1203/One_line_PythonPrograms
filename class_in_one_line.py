'''
This is a python class in one line using type meta class.
Example usage:

robo = Robot()
robo.say_hello("Jeet")

Output: Hi, I am Jeet
'''

Robot = type("Robot", (), { "say_hello": lambda self, name: "Hi, I am " + name, },)
robo = Robot()

print(robo.say_hello("Jeet"))