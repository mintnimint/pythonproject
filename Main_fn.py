"""Main of Programe"""

import numpy as np
import matplotlib.pyplot as plt


def year_2009():
    """Plot rate graph in year 2009
    """

    n = 10
    rate = (88.3, 55.6, 24.7, 29, 22.9, 20.8, 13.5, 10.5, 11.1, 7.2)
    ind = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate, width, color="r")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death in Year 2009 (Rates)")
    ax.set_xticks(ind + width+0.2)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                        "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                        "Tuberculosis"), rotation="vertical")

    # attach some text labels
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%.1f' % height,\
                ha='center', va='bottom')
    plt.show()

def year_2010():
    """Plot rate graph in year 2010
    """
    
    n = 10
    rate = (91.2, 51.6, 31.4, 28.9, 25.7, 21.6, 13.8, 11.1, 10.8, 7)
    ind = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate, width, color="r")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death in Year 2010 (Rates)")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                        "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                        "Tuberculosis"), rotation="vertical")

    # attach some text labels
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,\
                '%.1f' % height, ha='center', va='bottom')

    plt.show()

def year_2011():
    """Plot rate graph in year 2011
    """
    
    n = 10
    rate = (95.2, 52.8, 35.8, 31.4, 26.3, 23, 14, 10.6, 11.9, 7.5)
    ind = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate, width, color="r")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death in Year 2011 (Rates)")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                        "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                        "Tuberculosis"), rotation="vertical")


    # attach some text labels
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,\
                '%.1f' % height, ha='center', va='bottom')

    plt.show()

def year_2012():
    """Plot rate graph in year 2012
    """
    
    n = 10
    rate = (98.5, 51.6, 37.4, 32.9, 26.1, 22.9, 14.6, 10.8, 12.1, 8.3)
    ind = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate, width, color="r")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death in Year 2012 (Rates)")
    ax.set_xticks(ind + width+0.2)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                        "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                        "Tuberculosis"),rotation="vertical")

    # attach some text labels
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,\
                '%.1f' % height, ha='center', va='bottom')

    plt.show()
    
def year_2013():
    """Plot rate graph in year 2013
    """
    
    n = 10
    rate = (104.8, 50.2, 44, 38.1, 33.5, 23.5, 16.6, 10.8, 15, 8.5)
    ind = np.arange(n)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind + width, rate, width, color="r")

    ax.set_ylabel("Rates")
    ax.set_title("Cause of Death in Year 2013 (Rates)")
    ax.set_xticks(ind + width+0.2)
    ax.set_xticklabels(("Cancer and Tumor", "Accidents", "High Blood Pressure", "Heart Disease",\
                        "Lung Disease", "Nephritis", "Liver Disease", "Commit Suicide", "Diabetes",\
                        "Tuberculosis"), rotation="vertical")

    # attach some text labels
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.1f' % height, ha='center', va='bottom')

    plt.show()

    
year_2009()
year_2010()
year_2011()
year_2012()
year_2013()

