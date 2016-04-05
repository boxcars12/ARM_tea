from class_definitions import *
from math import sqrt, fabs

#from function_definitions import *
#move to function_definitions.py
def euc_distance(iniCoor, endCoor):
    return sqrt(pow(fabs(iniCoor[0] - endCoor[0]), 2) + pow(fabs(iniCoor[1] - endCoor[1]), 2) + pow(fabs(iniCoor[2] - endCoor[2]), 2))




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
#print goals1.list[0], goals1.list[1], goals1.list[2]

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


robot1 = Robot([(max_x_value-min_x_value)/2, (max_y_value-min_y_value)/2, (max_z_value-min_z_value)/2], None, None, 1, 1)

#zero z
robot1.start_coordinates[2] = 0

#create first link
link1 = Link(robot1.start_coordinates, robot1.start_coordinates, 0, [0, 0, 1], 1, 1, 1)
robot1.links.list.append(link1)

#modify link1 length
link1.length = euc_distance(robot1.start_coordinates, [max_x_value, max_y_value, max_z_value])

#does link 1 intersect any moat?
print(moats1)

#smallest configuration going over moat's z:

max_values = [0, 0, 0]
for moat in moats1.list:
    if moat.coordinates + moat.size > max_values:
        max_values = moat.coordinates + moat.size

link1.end_coordinates = max_values
link1.length = euc_distance(link1.start_coordinates, link1.end_coordinates)

link2 = Link(link1.end_coordinates, [max_x_value, max_y_value, max_z_value])
link2.length = euc_distance(link2.start_coordinates, link2.end_coordinates)
robot1.links.list.append(link2)

for link in robot1.links.list:
    #export truss info here
    pass

#link3
#angle change l1 to l2 should be reversed from l2 to l3

print "link1: %s" % link1

print robot1

