# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:35:48 2021
@author: preet
@rollno: 18d110019
"""

if __name__ == "__main__":

    import numpy as np
    import matplotlib.pyplot as plt

    ########## Reading a file ############

    file =open("lat.dat", "r")
    mod_file = open("modlat.dat", "w")
    data =[]
    while True:
        line = file.readline()
        if line:
            data.append(list(map(float, line.split()[0:])))
        if not line:
            break
    file.close()
    print (data[0]), print (data[0][0])

    ########### Writing the file #############

    for i in range(len(data)):
        mod_file.write('%6.6f %6.6f \n' %(4/3*np.pi*data[i][0]**3, data[i][1] ))
    mod_file.close()

    ############ Direct reading #################

    x, y = np.loadtxt('lat.dat', delimiter=None, unpack=True)
    print (x[0],y[0])

    ############ Plotting ####################

    plt.xlabel("lattice_parameter (A)")
    plt.ylabel("Energy (eV)")
    plt.plot(x,y, label='Loaded from file!')
    plt.show()

    x1, y1 = np.loadtxt('modlat.dat', delimiter=None, unpack=True)
    print (x1[0],y1[0])
    plt.xlabel("lattice_volume (V)")
    plt.ylabel("Energy (eV)")
    plt.plot(x1,y1, label='Loaded from file!')
    plt.savefig('latenergy.jpg')
    plt.show()

    __author__ = "Preet Shah"

    class EOSBase:
        """
        Abstract class that must be subcalssed by all equation of state
        implementations.
        """

        def __init__(self, volumes, energies):
            """
             Args:
                 volumes (list/numpy.array): volumes in Ang^3
                 energies (list/numpy.array): energy in eV
            """
            self.volumes = np.array(volumes)
            self.energies = np.array(energies)
            # minimum energy(e0), buk modulus(b0),
            # derivative of bulk modulus wrt pressure(b1), minimum volume(v0)
            self._params = None
            self.opt_params = None
            
        def fit_initial_guess(self, en):
            """
            Quadratic fit to get an initial guess for the parameters.
            Returns:
                tuple: (e0, b0, b1, v0)
            """
            a, b, c = np.polyfit(self.volumes, en, 2)

            v0 = -b / (2 * a)
            e0 = a * (v0 ** 2) + b * v0 + c
            b0 = 2 * a * v0
            b1 = 4  # b1 is usually a small number like 4

            vmin, vmax = min(self.volumes), max(self.volumes)

            if not vmin < v0 and v0 < vmax:
                raise EOSError('The minimum volume of a fitted parabola is '
                               'not in the input volumes\n.')
            print(e0, b0, b1, v0)

            return e0, b0, b1, v0

    class BirchMurnaghan(EOSBase):
        """
        BirchMurnaghan EOS
        """

        def perform_opt(self, volume, params):
            """
            BirchMurnaghan equation
            """
            e0, b0, b1, v0 = tuple(params)
            eta = (v0 / volume) ** (1. / 3.)

            return (e0 +
                    9. * b0 * v0 / 16. * (eta ** 2 - 1) ** 2 *
                    (6 + b1 * (eta ** 2 - 1.) - 4. * eta ** 2))

        def get_optimum_params(self):

            self._params = self.fit_initial_guess(self.energies)
            opt_energies = self.perform_opt(self.volumes, self._params)
            print (self.volumes[0], opt_energies[0])
            plt.xlabel("lattice_volume (V)")
            plt.ylabel("Energy (eV)")
            plt.plot(self.volumes, opt_energies, label='Loaded from file!')
            plt.show()
            self.opt_params = self.fit_initial_guess(opt_energies)
            return self.opt_params

    eos_bin = BirchMurnaghan(x1, y1)
    e0, b0, b1, v0 = tuple(eos_bin.get_optimum_params())
    print('e0 =' + str(e0) +'\nb0 =' + str(b0) +'\nb1 =' + str(b1) +'\nv0 =' + str(v0))
    
"""
e0 =-362202.46082134405
b0 =0.1268656924380577
b1 =4
v0 =4381.61499632735
"""
