import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#
# Create the individual stocks as dataframes
#

def read_csv(file_path, tick):
    """
    
    """
    temp = pd.read_csv(file_path, parse_dates=[0], index_col=0)
    temp.rename(columns={"Close" : tick}, inplace = True)
    temp.drop(["Open", "High", "Low", "Adj Close", "Volume"], axis = 1, inplace = True)
    return temp

def merge_dataframes(*args):
    """
    
    """
    Portfolio = args[0]
    for i in range(1, len(args)):
        Portfolio = pd.merge(Portfolio, args[i], on = "Date")
    return Portfolio

def split_timeseries(timeSeries):
    """
    
    """
    Train = timeSeries[0 : round(len(timeSeries)*0.85)]
    Test = timeSeries[round(len(timeSeries)*0.85) : len(timeSeries)]
    return Train, Test

def uniform_weights(timeSeries):
    """
    
    """
    numAssets = len(timeSeries.columns)
    return [1/numAssets for i in range(0, numAssets) ]

def plot_timeSeries(timeSeries):
    """
    
    """
    timeSeries.plot()
    plt.show()

def returns_timeseries(timeSeries):
    """
    
    """
    return timeSeries.pct_change()

def returns_allocated(returns_timeseries, weights):
    """
    
    """
    return returns_timeseries.dot(weights)

def plot_returns(returns):
    """
    
    """
    returns.plot(colormap= "jet", title = "sdfsdf")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def histogram_returns(returns):
    """
    
    """
    returns.hist(bins=40, grid=True, figsize=(7,4), color='#86bf91', zorder=2, rwidth=0.9)
    plt.xlabel("Returns")
    plt.ylabel("Frequency")
    plt.title("sdfsf")
    plt.show()

def variance_matrix(returns):
    """
    
    """
    return returns.cov()*252

def variance_timeseries(VarianceMatrix, Weights):
    """
    
    """
    return np.transpose(Weights)@VarianceMatrix@Weights

def volatility_timeseries(VarianceMatrix, Weights):
    """
    
    """
    return np.sqrt(variance_timeseries(VarianceMatrix, Weights))

def monte_carlo_simulation():
    """
    
    
    """
    PortfolioReturns = []
    PortfolioVolatility = []
    PortfolioWeights = []

    numAssets = len(Train.columns)
    numSimulations = 10000
    individual_rets = Train.resample ('Y').last ().pct_change ().mean ()

    for port in range (numSimulations):
        # Randomly generate weigh combination
        weights = np.random.random(numAssets)
        # Normalize weight so that they sum to 1
        weights = weights/np.sum(weights)
        PortfolioWeights.append(weights)
        # Returns are the dot product of individual expected returns of asset and its weights
        returns = np. dot (weights, individual_rets)
        PortfolioReturns.append(returns)
        # Computing Portfolio Variance
        var = VarianceMatrix.mul(weights, axis=0) .mul(weights, axis=1) .sum () .sum ()
        # Daily standard deviation : volatility is square root of variance
        sd = np.sqrt(var)
        # Annualizing the standard deviation will give us the volatility
        ann_sd = sd*np.sqrt(250)
        PortfolioVolatility.append(ann_sd)



def main():
    GOOG = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/Projekt/Data/GOOG.csv", "GOOG")
    AMZN = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/Projekt/Data/AMZN.csv", "AMZN")
    TSLA = read_csv("/Users/edwardglockner/Library/CloudStorage/OneDrive-Uppsalauniversitet/Fristående Kurser/Inferensteori I/Projekt/Data/TSLA.csv", "TSLA")

    Portfolio = merge_dataframes(GOOG, AMZN, TSLA)
    Train, Test = split_timeseries(Portfolio)
    weights = uniform_weights(Portfolio)

    returns_Train = returns_timeseries(Train)
    returns_train_allocated = returns_allocated(returns_Train, weights)
    covariance_matrix = variance_matrix(returns_Train)


if __name__ == "__main__":
    main()
    