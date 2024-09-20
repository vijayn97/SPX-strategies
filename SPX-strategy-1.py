"""
This test computes the number of days the difference between daily open and close of SPX is <1%.
"""
import yfinance as yf

spy = yf.download('SPY')
hit = 0 # number of days difference between daily open and close of SPX is <1%
miss = 0 # number of days difference between daily open and close of SPX is >1%
iterator = 0
for day in spy.index:
    if iterator >= spy.index.size:
        break
    # find the difference between open and close and track hits
    elif (((spy['Close'].iloc[iterator] - spy['Open'].iloc[iterator])/spy['Open'].iloc[iterator]) * 100) < 1:
        hit += 1
        iterator += 1
        continue
    else:
        miss += 1
        iterator += 1
        continue

sampleSize = spy.index.size
percentDaysHit = round(hit/(hit + miss) * 100, 2)

print ("Number of days tested (sample size):", sampleSize)
print ("Percentage of days difference between open and close of SPX is <1%:", percentDaysHit, "%")

"""
CONCLUSION: 90.4% of days have closes that are <1% of open. 
POTENTIAL TRADING IDEAS:
1. (>20 IV) Open SPX iron condor with shorts 1% away from open price at market open everyday.
2. (>20 IV) Open SPX strangle with shorts 1% away from open price at market open everyday.
"""
