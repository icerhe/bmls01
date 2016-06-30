# -*- coding: utf-8 -*-
# my first machine learning code
#

import os
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl


class Scatter:
    dataDir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "data")

    chartDir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "charts")

    zhfont = mpl.font_manager.FontProperties(
        fname='/usr/share/fonts/winf/YaHei.Consolas.1.12.ttf')

    colors = ['g', 'k', 'b', 'm', 'r']

    linestyles = ['-', '-.', '--', ':', '-']

    def gen_char01(self):
        # load file
        data = Scatter.load_csv("dyb_reserve.csv")
        x = data[:, 0]
        y = data[:, 1]
        x = x[~(x > 400)]
        y = y[~(x > 400)]
        print(x, y)

        fp1, res1, rank1, sv1, rcond1 = sp.polyfit(x, y, 10, full=True)
        print("Model parameters of fp1: %s" % fp1)
        print("Error of the model of fp1:", res1)
        f1 = sp.poly1d(fp1)

        Scatter.plot_models(x, y, [f1], "chart02")

    @staticmethod
    def load_csv(csv_file_name):
        return sp.genfromtxt(os.path.join(Scatter.dataDir, csv_file_name), delimiter=",")

    @staticmethod
    def plot_models(x, y, models, outfile, mx=None, y_max=None, x_min=None):

        plt.figure(num=None, figsize=(8,6))
        plt.clf()
        plt.scatter(x, y, s=10)
        plt.title("重量/价格关系表", fontproperties=Scatter.zhfont)
        plt.xlabel("weight")
        plt.ylabel("price")
        #plt.xlim(0,10)
        #plt.ylim(0,1000)
        if models:
            if mx is None:
                mx = sp.linspace(0, 400, 500)
            for model, style, color in zip(models, Scatter.linestyles, Scatter.colors):
                # print "Model:",model
                # print "Coeffs:",model.coeffs
                plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

            plt.legend(["d=%i" % m.order for m in models], loc="upper left")

        plt.autoscale(tight=True)
        plt.grid(True, linestyle='-', color='0.75')
        plt.show()
        #plt.savefig(os.path.join(Scatter.chartDir, outfile))

sc = Scatter()
sc.gen_char01()
