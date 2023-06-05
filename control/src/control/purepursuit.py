from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PurePursuitController(BaseController):
    def __init__(self, **kwargs):
        self.car_length = kwargs.pop("car_length")

        # Get the keyword args that we didn't consume with the above initialization
        super(PurePursuitController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the Pure Pursuit error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: Pure Pursuit error
        """
        return compute_position_in_frame(reference_xytv[:3], pose)

    def get_control(self, pose, reference_xytv, error):
        """Compute the Pure Pursuit control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
        """
        # BEGIN QUESTION 3.1
        "*** REPLACE THIS LINE ***"
        #raise NotImplementedError

           #k_p = np.array = 
        """
        difference = reference_xytv[0:2] - pose[0:2]
        cos = np.cos(reference_xytv[2])
        sin = np.sin(reference_xytv[2])
        rotate = np.array([[cos, sin], [-sin, cos]])
        a_b = np.dot(rotate, difference)
        """
        #rpp = ((a_b[0] ** 2) + (a_b[1] ** 2)) / (2 * a_b[1])
        rpp = np.sum(np.power(error, 2)) / (2 * error[1])

        return np.array([reference_xytv[3], np.arctan(self.car_length / rpp)])
        
        # END QUESTION 3.1
