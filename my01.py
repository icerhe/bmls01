#my first machine learning code

import os
import scipy as sp
import matplotlib.pyplot as plt

class Scatter:

    dataDir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data")

    chartDir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "charts")


    def genChart01(self):
        #load file
        data = self.loadCsv('data.csv')
        print(data)




    def loadCsv(self,csvFileName):
        data = sp.genfromtxt(os.path.join(Scatter.dataDir, csvFileName), delimiter=",")
        return data


sc = Scatter()
sc.genChart01()