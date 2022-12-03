import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Here all the functions will be declared


def read_csv(file_path, tick):
    """
    @params:

    @returns:

    Reads a file_path for a given ticker, and returns a dataframe with a column: close.
    """
    temp = pd.read_csv(file_path, parse_dates=[0], index_col=0)
    temp.rename(columns={"Close" : tick}, inplace = True)
    temp.drop(["Open", "High", "Low", "Adj Close", "Volume"], axis = 1, inplace = True)
    return temp

def merge_dataframes(*args):
    """
    @params:

    @returns:

    Merges dataframes into one dataframe.
    """
    Portfolio = args[0]
    for i in range(1, len(args)):
        Portfolio = pd.merge(Portfolio, args[i], on = "Date")
    return Portfolio

def split_timeseries(timeSeries):
    """
    @params:

    @returns:

    Splits a dataframe into a training set containing 80% of the data, and a testing set containing 
    """
    Train = timeSeries[round(len(timeSeries)*0.5) : round(len(timeSeries)*0.8)]
    Test = timeSeries[round(len(timeSeries)*0.8) : len(timeSeries)]
    return Train, Test

def uniform_weights(timeSeries):
    """
    @params:

    @returns:
    
    """
    numAssets = len(timeSeries.columns)
    return [1/numAssets for i in range(0, numAssets) ]

def plot_timeSeries(timeSeries):
    """
    @params:

    @returns:
    
    """
    timeSeries.plot()
    plt.show()

def returns_timeseries(timeSeries):
    """
    @params:

    @returns:
    
    """
    return timeSeries.pct_change()

def returns_allocated(returns_timeseries, weights):
    """
    @params:

    @returns:
    
    """
    return returns_timeseries.dot(weights)

def plot_returns(returns):
    """
    @params:

    @returns:
    
    """
    returns.plot(colormap= "jet", title = "sdfsdf")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def histogram_returns(returns):
    """
    @params:

    @returns:
    
    """
    returns.hist(bins=40, grid=True, figsize=(7,4), color='#86bf91', zorder=2, rwidth=0.9)
    plt.xlabel("Returns")
    plt.ylabel("Frequency")
    plt.title("sdfsf")
    plt.show()

def variance_matrix(returns):
    """
    @params:

    @returns:
    
    """
    return returns.cov()*252

def variance_timeseries(VarianceMatrix, Weights):
    """
    @params:

    @returns:
    
    """
    return np.transpose(Weights)@VarianceMatrix@Weights

def volatility_timeseries(VarianceMatrix, Weights):
    """
    @params:

    @returns:
    
    """
    return np.sqrt(variance_timeseries(VarianceMatrix, Weights))

def monte_carlo_simulation(Portfolio, varianceMatrix, numSimulations=20000):
    PortfolioReturns = []
    PortfolioWeights = []
    PortfolioVolatility = []
    numAssets = len(Portfolio.columns)
    individual_returns = Portfolio.resample("D").last().pct_change().mean()
    for port in range(numSimulations):
        weights = np.random.random(numAssets)
        weights = weights/np.sum(weights)
        PortfolioWeights.append(weights)
        returns = np.dot(weights, individual_returns)
        PortfolioReturns.append(returns)
        var = varianceMatrix.mul(weights, axis=0).mul(weights, axis=1).sum().sum()
        sd = np.sqrt(var)
        ann_sd = sd*np.sqrt(250)
        PortfolioVolatility.append(ann_sd)

    data = {"Returns" : PortfolioReturns, "Volatility" : PortfolioVolatility}
    for counter, symbol in enumerate(Portfolio.columns.tolist()):
        data[symbol + " weight"] = [w[counter] for w in PortfolioWeights]


    return pd.DataFrame(data)

def optimal_sharpe_ratio(PortfolioVersions):
    rf = 0.01
    optimal_risky_portfolio = PortfolioVersions.iloc[((PortfolioVersions["Returns"] - rf)/PortfolioVersions["Volatility"]).idxmax()]
    return optimal_risky_portfolio

def calculate_sharpe_ratio(portfolio):
    rf = 0.01
    return (portfolio["Returns"]-rf)/portfolio["Volatility"]

