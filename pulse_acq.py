import numpy as np
import matplotlib.pyplot as plt
import pdb
st = pdb.set_trace

import external # imports external.py
import experiment as ex

def pulse_acq(f0, tx_amp, tx_duration, dw, npts, tx_pre, rx_pre):
    exp = ex.Experiment(lo_freq=f0,
                        rx_t=dw,
                        init_gpa=False,
                        grad_max_update_rate=0.1)
    t_tstart=100
    tx_post=100
    tx0_times = np.array([0, tx_duration])+t_tstart + tx_pre
    tx0_amps = np.array([tx_amp, 0])
    tx_gate_times=np.array([t_tstart, tx_duration +t_tstart + tx_post])
    rx_tstart=t_tstart+tx_pre+tx_duration+rx_pre
    rx_tend=rx_tstart+dw*npts
    event_dict = {
        'tx0': (tx0_times, tx0_amps),
        'rx0_en': ( np.array([rx_tstart, rx_tend]), np.array([1, 0]) ),
        'tx_gate': ( tx_gate_times, np.array([1, 0]) )
        }
    exp.add_flodict(event_dict)
    if False:
        exp.plot_sequence()
        plt.show()
    
    rxd, msgs = exp.run()
    if True:
        plt.plot( rxd['rx0'].real )
        plt.plot( rxd['rx0'].imag )
        plt.show()
    
    exp.close_server(only_if_sim=True)

if __name__ == "__main__":
        pulse_acq(8.997, 0.5, 10, 3.0, 1024, 30, 50)
	 
