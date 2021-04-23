from Core.utility import deg_to_rad
from Core.robot import Robot


def assignment_3_2(initial_pose, s, error):
    robot = Robot(initial_pose)
    robot.draw_likelihoods(s, error, steps=1, draw_paths=True, ignore_epsilon=False)


if __name__ == "__main__":
    p_0 = (0, 0, 0)
    s_1 = (deg_to_rad(-20), 3, deg_to_rad(-30))
    e = (deg_to_rad(10), 0.5, deg_to_rad(5))
    assignment_3_2(p_0, s_1, e)
