import numpy as np
import matplotlib.pyplot as plt
import pdb
st = pdb.set_trace

import external # imports external.py
import experiment as ex

def my_first_experiment():
        exp = ex.Experiment(lo_freq=8.997,
                        rx_t=3.125,
                        init_gpa=False,
                        grad_max_update_rate=0.2
                        )
        tx0_times = np.array([50, 60])
        tx0_amps = np.array([1.0, 0])
        event_dict = {'tx0': (tx0_times, tx0_amps)}
        exp.add_flodict(event_dict)
        exp.add_flodict({'rx0_en': (np.array([100, 4000]), np.array([1, 0]))})
        rxd, msgs = exp.run()
        #exp.plot_sequence()
        #plt.show()    
        if True:
            plt.plot( rxd['rx0'].real )
            plt.plot( rxd['rx0'].imag )
            plt.show()
        exp.close_server(only_if_sim=True)
        #f=open("rxd.txt","w")
        #f.write(str(rxd))
        #f.close()
        #np.savetxt('output2.txt', rxd['rx0'].real)

if __name__ == "__main__":
        my_first_experiment()
	 
