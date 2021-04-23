from Core.utility import deg_to_rad
from Core.robot import Robot


def assignment_3_4(initial_pose, s, error, samples=100, steps=3):
    robot = Robot(initial_pose)
    for i in range(1, steps + 1):
        robot.draw_samples(s, error, steps=i, samples=samples)


if __name__ == "__main__":
    p_0 = (0, 0, 0)
    s_1 = (deg_to_rad(-20), 3, deg_to_rad(-30))
    e = (deg_to_rad(10), 0.5, deg_to_rad(5))
    assignment_3_4(p_0, s_1, e, samples=100, steps=3)
