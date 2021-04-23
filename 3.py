from Core.utility import deg_to_rad
from Core.robot import Robot


def assignment_3_3(initial_pose, s, error, steps=3):
    robot = Robot(initial_pose)
    for i in range(1, steps + 1):
        robot.draw_likelihoods(s, error, steps=i)


if __name__ == "__main__":
    p_0 = (0, 0, 0)
    s_1 = (deg_to_rad(-20), 3, deg_to_rad(-30))
    e = (deg_to_rad(10), 0.5, deg_to_rad(5))
    assignment_3_3(p_0, s_1, e, steps=3)
