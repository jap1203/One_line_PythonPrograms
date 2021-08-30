'''
This is a python class in one line using type meta class.
Example usage:

robo = Robot()
robo.say_hello("Ayush")

Output: Hi, I am Ayush
'''

Robot = type("Robot", (), { "say_hello": lambda self, name: "Hi, I am " + name, },)