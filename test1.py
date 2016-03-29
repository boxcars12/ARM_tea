#from class_definitions import *
#classes move to class_definitions.py


class Robot:

    def __init__(self, start_coordinates, links, joints, end_effector, placeholder):
        print "Robot created"
        self.start_coordinates = start_coordinates
        self.links = links
        self.joints = joints
        self.end_effector = end_effector
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Link:

    def __init__(self, start_coordinates, end_coordinates, orientation, length, width, joint_types, placeholder):
        print "Link created"
        self.start_coordinates = start_coordinates
        self.end_coordinates = end_coordinates
        self.orientation = orientation
        self.length = length
        self.width = width
        self.joint_types = joint_types
        self.placeholder = placeholder


class Joint:

    def __init__(self, position, joint_type, motors, range, placeholder):
        print "Joint created"
        self.position = position
        self.joint_type = joint_type
        self.motors = motors
        self.range = range
        self.placeholder = placeholder


class EndEffector:

    def __init__(self):
        pass


class Goal:

    def __init__(self, coordinates, size, orientable, shape, placeholder):
        print "Goal created"
        self.coordinates = coordinates
        self.size = size
        self.orientable = orientable
        self.shape = shape
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Goals:

    def __init__(self):
        print "Goals created"
        self.list = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Moat:

    def __init__(self, coordinates, size, orientable, shape, placeholder):
        print "Moat created"
        self.coordinates = coordinates
        self.size = size
        self.orientable = orientable
        self.shape = shape
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Moats:

    def __init__(self):
        print "Moats created"
        self.list = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Path:

    def __init__(self, steps, complexity, placeholder):
        print "Path created"
        self.steps = steps
        self.complexity = complexity
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Input:

    def __init__(self, goals, moats, path, placeholder):
        print "Input created"
        self.goals = goals
        self.moats = moats
        self.path = path
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)





#input move to input.txt


#input parser
#readfile
#goal1 = line1
goal1 = Goal([0, 0, 0], [1, 1, 1], 1, 1, 1)
goal2 = Goal([1, 1, 1], [1, 1, 1], 0, 1, 1)
goal3 = Goal([1, 1, 0], [1, 1, 1], 0, 1, 1)
goals1 = Goals()
goals1.list.append(goal1)
goals1.list.append(goal2)
goals1.list.append(goal3)

moat1 = Moat([0.75, 0.75, 0.75], [0.1, 0.1, 0.1], 0, 1, 1)
moats1 = Moats()
moats1.list.append(moat1)

path1 = Path([1, 2, 3, 2, 3, 2, 1], 1, 1)

input1 = Input(goals1, moats1, path1, 1)

#print str(input1.goals.list[0])
#print repr(input1.goals.list[0])
#print str(goals1.list[1])
#print repr(goals1.list[1])


#create robot
print goals1.list[0], goals1.list[1], goals1.list[2]

max_x_value = 0.0
min_x_value = 0.0
max_y_value = 0.0
min_y_value = 0.0
max_z_value = 0.0
min_z_value = 0.0

for goal in goals1.list:
    if goal.coordinates[0] > max_x_value:
        max_x_value = goal.coordinates[0]
    if goal.coordinates[0] < min_x_value:
        min_x_value = goal.coordinates[0]
    if goal.coordinates[1] > max_y_value:
        max_y_value = goal.coordinates[1]
    if goal.coordinates[1] < min_y_value:
        min_y_value = goal.coordinates[1]
    if goal.coordinates[2] > max_z_value:
        max_z_value = goal.coordinates[2]
    if goal.coordinates[2] < min_z_value:
        min_z_value = goal.coordinates[2]

print "x: (%.2f, %.2f)" % (min_x_value, max_x_value)
print "y: (%.2f, %.2f)" % (min_y_value, max_y_value)
print "z: (%.2f, %.2f)" % (min_z_value, max_z_value)


#robot1 = Robot([(max_x_value-min_x_value)/2, (max_y_value-min_y_value)/2, (max_z_value-min_z_value)/2], None, None, 1, 1)

