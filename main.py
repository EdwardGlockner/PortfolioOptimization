import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random

from functions import *

def data_manipulation():
    pass

def simulate(portfolios, path):
    results = []
    for i in range(0, len(portfolios)):
        # Create our portfolio and prepare for simulation
        current_portfolio = portfolios[i]
        data = [read_csv(path + tick + ".csv", tick) for tick in current_portfolio]
        portfolio = merge_dataframes(data)
        train, test = split_timeseries(portfolio)
        weights_uniform = uniform_weights(portfolio)

        # Calculate 
        rtrns_train = returns_timeseries(train)
        rtrns_test = returns_timeseries(test)
        covar_matrix = variance_matrix(rtrns_train)

        #plot_heatmap(covar_matrix)
        mc_train = monte_carlo_simulation(Portfolio = train, varianceMatrix= covar_matrix)
        optimal_portfolio = optimal_sharpe_ratio(mc_train)
        print(optimal_portfolio)
        results.append(run_live(rtrns_test, test, optimal_portfolio))

    return results

def run_live(rtrns_test, test, optimal_portfolio):
    covari_matrix_test = variance_matrix(rtrns_test) # EJ SÄKER PÅ DENNA. SKA DET INTE VARA TEST????
    rf = 0.01
    
    # We start with the uniform weights distribution
    weights_uniform = uniform_weights(test)
    individ_rtrns_uniform = test.resample("D").last().pct_change().mean()
    rtrns_uniform = np.dot(weights_uniform, individ_rtrns_uniform)
    var_uniform = covari_matrix_test.mul(weights_uniform, axis=0).mul(weights_uniform, axis=1).sum().sum()
    sd_uniform = np.sqrt(var_uniform)
    ann_sd_uniform = sd_uniform*np.sqrt(250)
    sharpe_ratio_uniform = (rtrns_uniform - rf)/ann_sd_uniform

    # Now we calculate for the optimal allocation
    weights_optimal = [optimal_portfolio[i] for i in range(2, len(optimal_portfolio))]
    individ_rtrns_optimal = test.resample("D").last().pct_change().mean()
    rtrns_optimal = np.dot(weights_optimal, individ_rtrns_optimal)
    var_optimal = covari_matrix_test.mul(weights_optimal, axis=0).mul(weights_optimal, axis=1).sum().sum()
    sd_optimal = np.sqrt(var_optimal)
    ann_sd_optimal = sd_optimal*np.sqrt(250)
    sharpe_ratio_optimal = (rtrns_optimal - rf)/ann_sd_optimal

    return (sharpe_ratio_uniform, sharpe_ratio_optimal)

def print_results(sharpe_ratio_uniform, sharpe_ratio_optimal):
    print("Sharpe ratio uniform: ", sharpe_ratio_uniform)
    print("Sharpe ratio optimal: ", sharpe_ratio_optimal)
    performance = 100 * (sharpe_ratio_optimal - sharpe_ratio_uniform)/abs(sharpe_ratio_uniform)
    print("Performance: ", performance, " %")


def main():
    tickers = ["AMZN", "BAC", "BRK-B", "COST", "CVS", "ET", 
                "FDX", "GM", "GOOG", "GS", "HP", "IBM", 
                "KO", "NKE", "PFE", "RTX", "TSLA", "XOM"]

    portfolios = [] # A list of all different portfolios we are going to test

    for i in range(0, 15):
        new_portfolio = random.sample(tickers,4)
        portfolios.append(new_portfolio)

    path = "/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/PortfolioOptimization/Data/"
    results = simulate(portfolios, path)

    for i in range(0, len(results)):
        print_results(results[i][0], results[i][1])



if __name__ == "__main__":
    main()
