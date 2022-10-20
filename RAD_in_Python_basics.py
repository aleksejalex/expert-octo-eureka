"""

Created by AG, 20221013
"""

# importy balicku
import inspect  # to get variable name
import numpy as np
import scipy as scp  # also 'random' ands 'stats'
import pandas as pd  # dataframes
import csv     
import seaborn as sbn  # cool plots
import matplotlib as mpt
from matplotlib import pyplot as plt
from scipy import stats as st


def retrieve_name(var):
    """
    returns variable name
    Example:
    > examplevarr = 4
    > print(examplevarr)
    > print(retrieve_name(examplevarr))
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


def get_array_from_df(row_or_column_df):
    """
    input: dataFrame bud radkovy nebo sloupcovy
    output: tytez cisla ale v numpy.array promenne
    """
    #data.loc[:, "Girth"]
    list = row_or_column_df.to_list()
    nparray = np.array(list)
    return nparray

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import datasetu (pomoci Pandas)
# (puvodne dataset byl stazen z >>  https://r-data.pmagunia.com/dataset/trees  )
url = "https://raw.githubusercontent.com/aleksejalex/expert-octo-eureka/main/dataset_cars_from_R.csv"
data = pd.read_csv(url)

data
#data.info

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# definice vlastnich fci na "manualni" vypocet E[.] a Var[.]
def stredni_hodnota(x):
    """
    spocte stredni hodnotu vektoru dat podle SS vzorce
    """
    n = len(x)
    E = 1/n * np.sum(x)
    return E


def rozptyl(x):
    """
    spocte rozptyl vektoru dat podle SS vzorce
    """
    n = len(x)
    E = 1/n * np.sum(x)
    Var = np.sqrt(  1/n * np.sum( (x - E)**2 )  )
    return Var

def test_zda_fce_vyse_funguji():
    # test zda funkce funguji (zbytecne pro puvodni ukol)
    vect = np.random.normal(0,1,1000000)
    plt.plot(vect, '.')
    print("stredni hodnota podle vzorce = " + str(stredni_hodnota(vect)))
    print("stredni hodnota NumPy = " + str(np.mean(vect)))
    print("rozptyl podle vzorce = " + str(rozptyl(vect)))
    print("rozptyl podle NumPy = " + str(np.var(vect)))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# zkousim si linearni regreesi - napsana rucne:
# tj. vypocet podle vzorcu

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	plt.xlabel('x')
	plt.ylabel('y')

	# function to show plot
	plt.show()

def main():
	# observations / data
	x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

	# estimating coefficients
	b = estimate_coef(x, y)
	print("Estimated coefficients:\nb_0 = {} \
		\nb_1 = {}".format(b[0], b[1]))

	# plotting regression line
	plot_regression_line(x, y, b)

if __name__ == "__main__":
	main()




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

