import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


"""
git commit -a -m <message>
git push origin main
"""




from functions import *

def run_calculations():
    # First read the csv files
    GOOG = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/CVS.csv", "GOOG")
    AMZN = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/BRK-B.csv", "AMZN")
    TSLA = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/COST.csv", "TSLA")

    # Merge the csv files into a portfolio dataframe
    portfolio = merge_dataframes(GOOG, AMZN, TSLA)

    # Split the dataframe into a train set, and a test set. The train set is used to calibrate the allocation 
    # optimization, and the test set is for validating if the allocation leads to an increase in the sharpe ratio
    train, test = split_timeseries(portfolio)
    
    # Uniform weights of the portfolio
    weights = uniform_weights(portfolio)

    rtrns_train = returns_timeseries(train)
    rtrns_train_allocated = returns_allocated(rtrns_train, weights)
    covar_matrix = variance_matrix(rtrns_train)
    var_train = variance_timeseries(covar_matrix, weights)
    vol_train = volatility_timeseries(covar_matrix, weights)

    mc_train = monte_carlo_simulation(Portfolio=train, varianceMatrix=covar_matrix)
    optimal_portfolio = optimal_sharpe_ratio(mc_train)
    
    # Now we calculate the returns for the test set
    covari_matrix_test = variance_matrix(rtrns_train)
    rf = 0.01

    # We start with the uniform weights distribution
    weights_uniform = [1/3, 1/3, 1/3]
    indivi_rtrns_uniform = test.resample("D").last().pct_change().mean()
    rtrns_uniform = np.dot(weights_uniform, indivi_rtrns_uniform)
    var_uniform = covari_matrix_test.mul(weights_uniform, axis=0).mul(weights_uniform, axis=1).sum().sum()
    sd_uniform = np.sqrt(var_uniform)
    ann_sd_uniform = sd_uniform*np.sqrt(250)
    sharpe_test_uniform = (rtrns_uniform - rf)/ann_sd_uniform

    # Now we calculate for the optimal distribution
    
    weights_optimal = [optimal_portfolio["GOOG weight"], optimal_portfolio["AMZN weight"], optimal_portfolio["TSLA weight"]]
    indivi_rtrns_optimal = test.resample("D").last().pct_change().mean()
    rtrns_optimal = np.dot(weights_optimal, indivi_rtrns_optimal)
    var_optimal = covari_matrix_test.mul(weights_optimal, axis=0).mul(weights_optimal, axis=1).sum().sum()
    sd_optimal = np.sqrt(var_optimal)
    ann_sd_optimal = sd_optimal*np.sqrt(250)
    sharpe_test_optimal = (rtrns_optimal - rf)/ann_sd_optimal

    print("Sharpe ratio uniform: ", sharpe_test_uniform)
    print("Sharpe ratio optimal: ", sharpe_test_optimal)

    performance = 100 * (sharpe_test_optimal - sharpe_test_uniform)/abs(sharpe_test_uniform)
    print("Performance: ", performance, " %")



def main():
    run_calculations()

if __name__ == "__main__":
    main()
