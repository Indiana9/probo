from probo.marketdata import MarketData
from probo.payoff import ExoticPayoff, arithmeticAsianCallPayoff, arithmeticAsianPutPayoff
from probo.engine import MonteCarloEngine, PathwiseNaiveMonteCarloPricer, ControlVariateAsianPrice, ControlVariatePricer 
from probo.facade import OptionFacade

## Set up the market data
spot = 41.0
rate = 0.08
volatility = 0.30
dividend = 0.0
thedata = MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 1.0
strike = 40.0
thecall = ExoticPayoff(expiry, strike, arithmeticAsianCallPayoff)
theput = ExoticPayoff(expiry, strike, arithmeticAsianPutPayoff)

## Set up Naive Monte Carlo
nreps = 100000
steps = 1
pricer = ControlVariatePricer
pricer = ControlVariateAsianPrice
pricer = PathwiseNaiveMonteCarloPricer
mcengine = MonteCarloEngine(nreps, steps, pricer)

## Calculate the price
option1 = OptionFacade(thecall, mcengine, thedata)
price1 = option1.price()
print("The call price via Naive Monte Carlo is: {0:.3f}. Standard error is {1:.3f}".format(price1))

option2 = OptionFacade(theput, mcengine, thedata)
price2 = option2.price()
print("The put price via Naive Monte Carlo is: {0:.3f}. Standard error is {1:.3f}".format(price2))

## Table 

The results of our computations are given below: 

print(  Name of Option  | Option Price | Standard Error |)
print(Simple Monte Carlo|----{0:.3f}---|-----{1:.3f}----|)
print(    Geometric     |----{0:.3f}---|-----{1:.3f}----|)

