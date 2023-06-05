#!/usr/bin/env python
from __future__ import division
from threading import Lock
import numpy as np
import rospy

from std_msgs.msg import Float64
from vesc_msgs.msg import VescStateStamped


class KinematicCarMotionModel:
    """The kinematic car motion model."""

    def __init__(self, car_length, **kwargs):
        """Initialize the kinematic car motion model.

        Args:
            car_length: the length of the car
            **kwargs (object): any number of optional keyword arguments:
                vel_std (float): std dev of the control velocity noise
                delta_std (float): std dev of the control delta noise
                x_std (float): std dev of the x position noise
                y_std (float): std dev of the y position noise
                theta_std (float): std dev of the theta noise
        """
        defaults = {
            "vel_std": 0.05,
            "delta_std": 0.5,
            "x_std": 0.05,
            "y_std": 0.05,
            "theta_std": 0.05,
        }
        if not set(kwargs).issubset(set(defaults)):
            raise ValueError("Invalid keyword argument provided")
        # These next two lines set the instance attributes from the defaults and
        # kwargs dictionaries. For example, the key "vel_std" becomes the
        # instance attribute self.vel_std.
        self.__dict__.update(defaults)
        self.__dict__.update(kwargs)

        if car_length <= 0.0:
            raise ValueError(
                "The model is only defined for defined for positive, non-zero car lengths"
            )
        self.car_length = car_length

    def compute_changes(self, states, controls, dt, delta_threshold=1e-2):
        """Integrate the (deterministic) kinematic car model.

        Given vectorized states and controls, compute the changes in state when
        applying the control for duration dt.

        If the absolute value of the applied delta is below delta_threshold,
        round down to 0. We assume that the steering angle (and therefore the
        orientation component of state) does not change in this case.

        Args:
            states: np.array of states with shape M x 3
            controls: np.array of controls with shape M x 2
            dt (float): control duration
            delta_threshold (float): steering angle threshold

        Returns:
            M x 3 np.array, where the three columns are dx, dy, dtheta
        """
        # BEGIN QUESTION 1.1
        "*** REPLACE THIS LINE ***"
        new_m = np.zeros_like(states, dtype=float)

        c = controls[:,1]

        app_c   = np.where(np.abs(c) < delta_threshold, 0, c)
        d_theta = np.multiply(np.divide(controls[:,0], self.car_length), np.tan(app_c)) * dt
        d_x     = np.multiply(np.divide(self.car_length, np.tan(app_c)), (np.sin((states[:,2] + d_theta))) - np.sin(states[:,2]))
        d_y     = np.multiply(np.divide(self.car_length, np.tan(app_c)), ((-1 * np.cos((states[:,2] + d_theta)))) + np.cos(states[:,2]))

        mask = app_c == 0

        d_x0 = np.multiply(controls[:,0], np.cos(states[:,2])) * dt
        d_y0 = np.multiply(controls[:,0], np.sin(states[:,2])) * dt
        d_x[mask] = d_x0[mask]
        d_y[mask] = d_y0[mask]
        new_m[:,0] = d_x
        new_m[:,1] = d_y
        new_m[:,2] = d_theta
 
        # for i in range(len(states)):
        #     #d_theta = (controls[i][0] / self.car_length) * (np.tan(controls[i][1])) * dt
        # #d_theta = np.where(np.abs(controls[:][1]) < delta_threshold, 0, (controls[:][0] / self.car_length) * (np.tan(controls[:][1])) * dt)
        # #d_x = np.where(np.abs(controls[:][1]) < delta_threshold, controls[:][0] * np.cos(states[:][2]) * dt, (self.car_length / np.tan(controls[:][1])) * (np.sin(d_theta) - np.sin(states[:][2])))
        # #d_y = np.where(np.abs(controls[:][1]) < delta_threshold, controls[:][0] * np.sin(states[:][2]) * dt, (self.car_length / np.tan(controls[:][1])) * ((-1 * np.cos(d_theta)) + np.cos(states[:][2])))
        #     d_theta = 0
        #     d_x = 0
        #     d_y = 0
        #     if (np.abs(controls[i][1]) < delta_threshold):
        #         d_theta = 0
        #         d_x = controls[i][0] * np.cos(states[i][2]) * dt
        #         d_y = controls[i][0] * np.sin(states[i][2]) * dt
        #     else:
        #         d_theta = (controls[i][0] / self.car_length) * (np.tan(controls[i][1])) * dt
        #         d_x = (self.car_length / np.tan(controls[i][1])) * (np.sin((states[i][2] + d_theta)) - np.sin(states[i][2]))
        #         d_y = (self.car_length / np.tan(controls[i][1])) * ((-1 * np.cos((states[i][2] + d_theta)) + np.cos(states[i][2])))
        #     new_m[i][0] = d_x
        #     new_m[i][1] = d_y
        #     new_m[i][2] = d_theta

        #return np.zeros_like(states, dtype=float)
        return new_m
        # END QUESTION 1.1

    def apply_motion_model(self, states, vel, delta, dt):
        """Propagate states through the noisy kinematic car motion model.

        Given the nominal control (vel, delta), sample M noisy controls.
        Then, compute the changes in state with the noisy controls.
        Finally, add noise to the resulting states.

        NOTE: This function does not have a return value: your implementation
        should modify the states argument in-place with the updated states.

        >>> states = np.ones((3, 2))
        >>> states[2, :] = np.arange(2)  #  modifies the row at index 2
        >>> a = np.array([[1, 2], [3, 4], [5, 6]])
        >>> states[:] = a + a            # modifies states; note the [:]

        Args:
            states: np.array of states with shape M x 3
            vel (float): nominal control velocity
            delta (float): nominal control steering angle
            dt (float): control duration
        """
        n_particles = states.shape[0]

        # Hint: you may find the np.random.normal function useful
        # BEGIN QUESTION 1.2
        "*** REPLACE THIS LINE ***"
        vel_noise   = np.random.normal(vel, self.vel_std, (n_particles,1))
        delta_noise = np.random.normal(delta, self.delta_std, (n_particles,1)) 

        state_noise = self.compute_changes(states, np.concatenate((vel_noise, delta_noise), axis=1), dt)

        states[:,0] += np.random.normal(state_noise[:,0], self.x_std)
        states[:,1] += np.random.normal(state_noise[:,1], self.y_std)
        states[:,2] += np.random.normal(state_noise[:,2], self.theta_std)

        states[:,2] %= (2 * np.pi)

        states[:,2][states[:,2] > np.pi] -= (2 * np.pi)
        # END QUESTION 1.2


class KinematicCarMotionModelROS:
    """A ROS subscriber that applies the kinematic car motion model.

    This applies the motion model to the particles whenever it receives a
    message from the control topic. Each particle represents a state (pose).

    These implementation details can be safely ignored, although you're welcome
    to continue reading to better understand how the entire state estimation
    pipeline is connected.
    """

    def __init__(self, particles, noise_params=None, state_lock=None, **kwargs):
        """Initialize the kinematic car model ROS subscriber.

        Args:
            particles: the particles to update in-place
            noise_params: a dictionary of parameters for the motion model
            state_lock: guarding access to the particles during update,
                since it is shared with other processes
            **kwargs: must include
                motor_state_topic (str):
                servo_state_topic (str):
                speed_to_erpm_offset (str): Offset conversion param from rpm to speed
                speed_to_erpm_gain (float): Gain conversion param from rpm to speed
                steering_to_servo_offset (float): Offset conversion param from servo position to steering angle
                steering_to_servo_gain (float): Gain conversion param from servo position to steering angle
                car_length (float)
        """
        self.particles = particles
        required_keyword_args = {
            "speed_to_erpm_offset",
            "speed_to_erpm_gain",
            "steering_to_servo_offset",
            "steering_to_servo_gain",
            "car_length",
        }
        if not required_keyword_args.issubset(set(kwargs)):
            raise ValueError("Missing required keyword argument")
        # This sets the instance attributes from the kwargs dictionary.
        self.__dict__.update(kwargs)

        self.state_lock = state_lock or Lock()
        noise_params = {} if noise_params is None else noise_params
        self.motion_model = KinematicCarMotionModel(self.car_length, **noise_params)

        self.last_servo_cmd = None
        self.last_vesc_stamp = None

        self.servo_subscriber = rospy.Subscriber(
            "servo_state", Float64, self.servo_callback, queue_size=1
        )

        self.motion_subscriber = rospy.Subscriber(
            "vesc/sensors/core", VescStateStamped, self.motion_callback, queue_size=1
        )

        self.initialized = False

    def start(self):
        self.initialized = True

    def servo_callback(self, msg):
        """Cache the most recent servo position command.

        This command is used by motion_callback to compute the steering angle.

        Args:
            msg: a std_msgs/Float64 servo message
        """
        self.last_servo_cmd = msg.data

    def motion_callback(self, msg):
        """Apply the motion model to self.particles.

        Convert raw VESC message to vel and delta controls.

        Args:
            msg: a vesc_msgs/VescStateStamped message
        """
        if self.last_servo_cmd is None:
            # We haven't received any servo command, can't apply motion model
            rospy.logwarn_throttle(5, "No servo command received")
            return

        if self.last_vesc_stamp is None:
            rospy.loginfo("Motion information received for the first time")
            self.last_vesc_stamp = msg.header.stamp
            return

        if not self.initialized:
            return
        # Convert raw msgs to controls
        # Note that control = (raw_msg_val - offset_param) / gain_param
        curr_speed = (
            msg.state.speed - self.speed_to_erpm_offset
        ) / self.speed_to_erpm_gain

        curr_steering_angle = (
            self.last_servo_cmd - self.steering_to_servo_offset
        ) / self.steering_to_servo_gain

        dt = (msg.header.stamp - self.last_vesc_stamp).to_sec()

        # Acquire the lock that synchronizes access to the particles. This is
        # necessary because self.particles is shared by the other particle
        # filter classes.
        #
        # The with statement automatically acquires and releases the lock.
        # See the Python documentation for more information:
        # https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement
        with self.state_lock:
            # Propagate particles with the motion model
            self.motion_model.apply_motion_model(
                self.particles, curr_speed, curr_steering_angle, dt
            )

        self.last_vesc_stamp = msg.header.stamp
