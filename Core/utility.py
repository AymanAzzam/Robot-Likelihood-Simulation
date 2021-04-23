from numpy import cos, sin, pi

import matplotlib.pyplot as plt
from Core.constants import ROBOT_SIZE


def perform_motion(pose, action):
    x, y, theta = pose
    s_rot_1, s_trans, s_rot_2 = action

    x = x + s_trans * cos(theta + s_rot_1)
    y = y + s_trans * sin(theta + s_rot_1)
    theta = theta + s_rot_1 + s_rot_2

    return x, y, theta


def adjust_graph(figure_axes, title):
    y_min, y_max = figure_axes.axes.get_ylim()
    x_min, x_max = figure_axes.axes.get_xlim()

    x_margin = (x_max - x_min) / 15 + ROBOT_SIZE
    y_margin = (y_max - y_min) / 15 + ROBOT_SIZE

    figure_axes.axis([x_min - x_margin,
                      x_max + x_margin,
                      y_min - y_margin,
                      y_max + y_margin])

    figure_axes.set_aspect(1)
    figure_axes.legend()
    figure_axes.set_title(title)

    plt.show()


def print_pose(pose):
    x, y, theta = pose
    theta = rad_to_deg(theta)
    print("x = " + str(x) + "m,     y = " + str(y) + "m,    theta = " + str(theta) + "°")


def deg_to_rad(deg):
    return deg * pi / 180


def rad_to_deg(rad):
    return rad * 180 / pi
