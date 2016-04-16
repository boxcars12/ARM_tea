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

    def __init__(self, start_coordinates, end_coordinates, length, orientation, width, joint_types, placeholder):
        print "Link created"
        self.start_coordinates = start_coordinates
        self.end_coordinates = end_coordinates
        self.length = length
        self.orientation = orientation
        self.width = width
        self.joint_types = joint_types
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Joint:

    def __init__(self, position, joint_type, motors, range, placeholder):
        print "Joint created"
        self.position = position
        self.joint_type = joint_type
        self.motors = motors
        self.range = range
        self.placeholder = placeholder

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


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