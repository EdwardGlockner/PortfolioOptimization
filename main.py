import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


"""
git commit -a -m <message>
git push origin main
"""

from functions import *

def run_calculations():
    GOOG = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/HP.csv", "GOOG")
    AMZN = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/KO.csv", "AMZN")
    TSLA = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/AMZN.csv", "TSLA")

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
    
    # Now we calculate the returns for the test set

    weights_uniform = [1/3, 1/3, 1/3]
    weights_optimal = [optimal_portfolio["GOOG weight"], optimal_portfolio["AMZN weight"], optimal_portfolio["TSLA weight"]]
    print(weights_optimal)
    individual_returns_uniform = Test.resample("D").last().pct_change().mean()
    individual_returns_optimal = Test.resample("D").last().pct_change().mean()

    returns_Test = returns_timeseries(Test)
    covariance_matrix_Test = variance_matrix(returns_Train)

    returns_uniform = np.dot(weights_uniform, individual_returns_uniform)
    returns_optimal = np.dot(weights_optimal, individual_returns_optimal)
    
    variance_uniform = covariance_matrix_Test.mul(weights_uniform, axis=0).mul(weights_uniform, axis=1).sum().sum()
    variance_optimal = covariance_matrix_Test.mul(weights_optimal, axis=0).mul(weights_optimal, axis=1).sum().sum()
    
    sd_uniform = np.sqrt(variance_uniform)
    sd_optimal = np.sqrt(variance_optimal)

    ann_sd_uniform = sd_uniform*np.sqrt(250)
    ann_sd_optimal = sd_optimal*np.sqrt(250)


    rf = 0.01
    sharpe_test_uniform = (returns_uniform - rf)/ann_sd_uniform
    sharpe_test_optimal = (returns_optimal - rf)/ann_sd_optimal

    print("Sharpe ratio uniform: ", sharpe_test_uniform)
    print("Sharpe ratio optimal: ", sharpe_test_optimal)

    performance = 100 * (sharpe_test_optimal - sharpe_test_uniform)/abs(sharpe_test_uniform)
    print("Performance: ", performance, " %")
def main():
    run_calculations()

if __name__ == "__main__":
    main()
