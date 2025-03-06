import yfinance as yf
import matplotlib


#Initialize the variables for different tech stocks
Nvidia = yf.Ticker("NVDA")
Nvidia = Nvidia.history(period="max")
del Nvidia["Dividends"], Nvidia["Stock Splits"]

Tesla = yf.Ticker("TSLA")
Tesla = Tesla.history(period="max")
del Tesla["Dividends"], Tesla["Stock Splits"]

Meta = yf.Ticker("META")
Meta = Meta.history(period="max")
del Meta["Dividends"], Meta["Stock Splits"]

Microsoft = yf.Ticker("MSFT")
Microsoft = Microsoft.history(period="max")
del Microsoft["Dividends"], Microsoft["Stock Splits"]


#Plot the stock into a line graph
nvda_graph = Nvidia.plot.line(y="Close", use_index=True)




