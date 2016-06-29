# my first machine learning code

import os
import scipy as sp
import matplotlib.pyplot as plt


class Scatter:
    dataDir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data")

    chartDir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "charts")

    def gen_char01(self):
        # load file
        data = Scatter.load_csv("data.csv")
        x = data[:, 0]
        y = data[:, 1]
        print(x,y)



    @staticmethod
    def load_csv(csv_file_name):
        return sp.genfromtxt(os.path.join(Scatter.dataDir, csv_file_name), delimiter=",")

    def plot_models(self, x, y, models, outfile, mx=None, y_max=None, x_min=None):
        plt.figure(num=None, figsize=(8,6))

sc = Scatter()
sc.gen_char01()
