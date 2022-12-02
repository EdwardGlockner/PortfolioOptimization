import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


"""
git commit -a -m <message>
git push origin main
"""

from functions import *

def run_calculations():
    GOOG = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/GOOG.csv", "GOOG")
    AMZN = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/AMZN.csv", "AMZN")
    TSLA = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/TSLA.csv", "TSLA")

    Portfolio = merge_dataframes(GOOG, AMZN, TSLA)
    Train, Test = split_timeseries(Portfolio)
    weights = uniform_weights(Portfolio)

    returns_Train = returns_timeseries(Train)
    returns_train_allocated = returns_allocated(returns_Train, weights)
    covariance_matrix = variance_matrix(returns_Train)
    training_variance = variance_timeseries(covariance_matrix, weights)
    training_volatility = volatility_timeseries(covariance_matrix, weights)

    mc = monte_carlo_simulation(Portfolio=Train, varianceMatrix=covariance_matrix)
    optimal_portfolio = optimal_sharpe_ratio(mc)
    sharpe_ratio = calculate_sharpe_ratio(optimal_portfolio)
    print("Sharpe ratio: ", sharpe_ratio)
    print(optimal_portfolio)

    #return tuple with sharpe ratio before/after optimization


def main():

    print("Hello world")

if __name__ == "__main__":
    main()
    
