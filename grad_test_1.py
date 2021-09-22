import numpy as np
import matplotlib.pyplot as plt
import pdb
st = pdb.set_trace

import external # imports external.py
import experiment as ex

def trapezoid(plateau_a, total_t, ramp_t, ramp_pts, total_t_end_to_end=True, base_a=0):
    """Helper function that just generates a Numpy array starting at time
    0 and ramping down at time total_t, containing a trapezoid going from a
    level base_a to plateau_a, with a rising ramp of duration ramp_t and
    sampling period ramp_ts."""

    # ramp_pts = int( np.ceil(ramp_t/ramp_ts) ) + 1
    rise_ramp_times = np.linspace(0, ramp_t, ramp_pts)
    rise_ramp = np.linspace(base_a, plateau_a, ramp_pts)

    # [1: ] because the first element of descent will be repeated
    descent_t = total_t - ramp_t if total_t_end_to_end else total_t
    t = np.hstack([rise_ramp_times, rise_ramp_times[:-1] + descent_t])
    a = np.hstack([rise_ramp, np.flip(rise_ramp)[1:]])
    return t, a

def grad_test_1():
        exp = ex.Experiment(lo_freq=8.997,
                        rx_t=3.125,
                        init_gpa=True,
                        grad_max_update_rate=0.2
                        )
        t_tstart=100
        tx_duration=60
        tx_post=1
        tx0_times = np.array([100,160])
        tx0_amps = np.array([1.0, 0])
        gxt,gxa=trapezoid(0.05,3000,400,20)
        tx_gate_times=np.array([t_tstart, tx_duration +t_tstart + tx_post])
        event_dict = {'tx0': (tx0_times, tx0_amps),
                      'rx0_en': (np.array([500, 3000]), np.array([1, 0])),
                      'ocra1_vx': ( gxt + 1000, gxa ),
                      'tx_gate': ( tx_gate_times, np.array([1, 0]))}
        exp.add_flodict(event_dict)
        rxd, msgs = exp.run()
        if False:
            exp.plot_sequence()
            plt.show()    
        if True:
            plt.plot( rxd['rx0'].real )
            plt.plot( rxd['rx0'].imag )
            plt.show()
        exp.close_server(only_if_sim=True)
        if False:
            np.savetxt('output2.txt', rxd['rx0'].real)

if __name__ == "__main__":
        grad_test_1()
	 
