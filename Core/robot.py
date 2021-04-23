import random

from numpy import cos, sin, arange
import matplotlib.pyplot as plt

from Core.constants import ROBOT_SIZE, LINE_WIDTH, CIRCLE_WIDTH, ROBOT_COLORS
from Core.utility import perform_motion, adjust_graph, print_pose


class Robot:
    def __init__(self, initial_pose):
        self.initial_pose = initial_pose
        self.fig, self.figure_axes = plt.subplots()

    # Inputs: 
    #   action(rot_1, trans, rot_2)
    # Outputs:
    #   pose(x', y', theta')

    # Inputs:
    #   pose(x, y, theta)       robot_color(optional)
    #   robot_size(optional)    label(optional)  
    # Task: 
    #   1- Draw circle that represent the robot position
    #   2- Draw line that represent the robot direction
    def draw_robot(self, pose, robot_color=(1, 0, 0, 1), robot_size=ROBOT_SIZE, label='Robot'):
        x, y, theta = pose
        x2, y2 = x + cos(theta) * robot_size, y + sin(theta) * robot_size
        direction = plt.Line2D((x, x2), (y, y2), color=robot_color, linewidth=LINE_WIDTH)
        robot = plt.Circle((x, y), robot_size, linewidth=CIRCLE_WIDTH, label=label)
        robot.set_facecolor("black")
        self.figure_axes.add_artist(robot)
        self.figure_axes.add_artist(direction)
        self.figure_axes.plot(x, y, 'k,')
        print_pose(pose)

    # Inputs: 
    #   pose_list: where each pose is (x, y, theta)
    #   plot_style(optional): color of the drawn shapes     robot_size(optional)    label(optional)
    # Tasks:
    #   1- Draw robot at each pose
    #   2- Connect each two consecutive robots with a line      
    def draw_poses(self, pose_list, plot_style='r-', robot_size=ROBOT_SIZE, label=None):

        # draw initial pose
        p_0 = pose_list[0]
        self.draw_robot(p_0, robot_size=robot_size)

        for i in range(len(pose_list) - 1):
            j = i + 1
            x_i, y_i, theta_i = pose_list[i]
            x_j, y_j, theta_j = pose_list[j]
            self.figure_axes.plot([x_i, x_j], [y_i, y_j], plot_style, linewidth=LINE_WIDTH,
                                  label=label if i == 0 else None)
            self.draw_robot(pose_list[j], robot_size=robot_size)

    # Inputs:
    #   actions_list: where each action is (rot_1, trans, rot_2)
    # Tasks:
    #   1- Draw the robot pose after each action
    #   2- connect each two consecutive robots with a line
    def draw_actions(self, actions_list, plot_style='g-', robot_size=0.4):
        pose_list = [self.initial_pose]
        for action in actions_list:
            pose_list.append(perform_motion(pose=pose_list[-1], action=action))

        self.draw_poses(pose_list, plot_style, robot_size, label='path without $\epsilon$')

        # adjust graph bounds
        adjust_graph(self.figure_axes, title="Robot Pose after each action")

    # Inputs: 
    #   s(rot_1, trans, rot_2): the action      
    #   e(epsilon_rot1, epsilon_trans, epsilon_rot2): the error of action     
    #   steps: the number of steps to move      draw_paths: draw the likelihood paths when True
    #   ignore_epsilon: ignore the epsilon the last step when true
    # Tasks:
    #   1- Draw the expected positions of robot after each step(that happens because of the error)
    #   2- Draw the robot position after each step(without error)
    def draw_likelihoods(self, s, e, steps=1, draw_paths=False, ignore_epsilon=True, plot_style='b-'):
        # build error movements:
        s_errors = []
        s_errors_reduced = []
        for e_rot_1 in [e[0], -e[0]]:
            for e_trans in [e[1], -e[1]]:
                s_errors_reduced.append((s[0] + e_rot_1, s[1] + e_trans, s[2]))
                for e_rot_2 in [e[2], -e[2]]:
                    s_errors.append((s[0] + e_rot_1, s[1] + e_trans, s[2] + e_rot_2))

        if not ignore_epsilon:
            s_errors_reduced = s_errors

        p_regular = [self.initial_pose]
        p_lists = [[self.initial_pose]]
        for step in range(steps):
            p_regular.append(perform_motion(pose=p_regular[-1], action=s))
            p_lists_new = []
            # for each last path i got
            for p_list in p_lists:
                p_last = p_list[-1]
                # do all the possible movements for my last pose in that path
                for s_i in (s_errors if step + 1 < steps else s_errors_reduced):
                    p_next = perform_motion(pose=p_last, action=s_i)
                    p_lists_new.append(p_list + [p_next])
            p_lists = p_lists_new
            # draw new robot positions
            for p_list in p_lists:
                p_last = p_list[-1]
                self.draw_robot(p_last, ROBOT_COLORS[step - 1 % len(ROBOT_COLORS)])

        print("plotting " + str(len(p_lists)) + " paths...")

        # draw regular pose
        self.draw_poses(p_regular, plot_style='g-', label='path without $\epsilon$')

        if draw_paths:
            label = 'path with $\epsilon$'
            for i in range(len(p_lists)):
                x_1, y_1, _ = p_lists[i][-2]
                x_2, y_2, _ = p_lists[i][-1]
                self.figure_axes.plot([x_1, x_2], [y_1, y_2], plot_style, linewidth=LINE_WIDTH,
                                      label=label if i == 0 else None)

        # adjust graph bounds
        likelihood = len(s_errors) ** steps
        if ignore_epsilon:
            likelihood = int(likelihood / 2)
        title = "likelihoods after " + str(steps) + " steps ( $P(p_{t=" + str(steps) + "}) = 1/"
        title += str(likelihood) + "$ :"
        adjust_graph(self.figure_axes, title)
        # Initialize new Figure
        self.fig, self.figure_axes = plt.subplots()

    # Inputs: 
    #   s(rot_1, trans, rot_2): the action      
    #   e(epsilon_rot1, epsilon_trans, epsilon_rot2): the error of action     
    #   steps: the number of steps to move      samples: the number of robots at the initial pose
    # Tasks:
    #   Draw the samples poses of robots at the final step
    def draw_samples(self, s, e, steps=1, samples=100):
        # error sample sets:
        # e_rot1 = [e[0], - e[0]]
        # e_trans = [e[1], - e[1]]
        # e_rot2 = [e[2], - e[2]]
        e_rot1 = arange(-e[0], e[0], 0.1).tolist()
        e_trans = arange(-e[1], e[1], 0.1).tolist()
        e_rot2 = arange(-e[2], e[2], 0.1).tolist()

        end_poses = []
        for i in range(samples):
            p = self.initial_pose
            for i in range(steps):
                s_sample = (s[0] + random.sample(k=1, population=e_rot1)[0],
                            s[1] + random.sample(k=1, population=e_trans)[0],
                            s[2] + random.sample(k=1, population=e_rot2)[0])
                p = perform_motion(pose=p, action=s_sample)
            end_poses.append(p)

        # plot start pose:
        self.draw_robot(self.initial_pose)
        # plot samples:
        for p in end_poses:
            self.draw_robot(p, robot_color=ROBOT_COLORS[(steps - 1) % len(ROBOT_COLORS)])

        # adjust graph bounds
        title = str(samples) + " samples for t = " + str(steps)
        adjust_graph(figure_axes=self.figure_axes, title=title)
        # Initialize new Figure
        self.fig, self.figure_axes = plt.subplots()
