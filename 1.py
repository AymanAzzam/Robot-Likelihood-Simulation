from Core.utility import deg_to_rad
from Core.robot import Robot


def assignment_3_1(initial_pose, s):
    robot = Robot(initial_pose)
    actions_list = []
    for motion in s:
        actions_list.append(motion)
    robot.draw_actions(actions_list)


if __name__ == "__main__":
    p_0 = (0, 0, 0)
    s_1 = (deg_to_rad(-20), 3, deg_to_rad(-30))
    s_2 = (deg_to_rad(20), 10, deg_to_rad(10))
    assignment_3_1(p_0, [s_1, s_2])
