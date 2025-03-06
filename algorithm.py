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

Apple = yf.Ticker("APPL")
Apple = Apple.history(period="max")
del Apple["Dividends"], Apple["Stock Splits"]

Google = yf.Ticker("GOOGL")
Google = Google.history(period = "max")
del Google["Dividends"], Google["Stock Splits"]

Amazon yf.Ticker("AMZN")
Amazon = Amazon.history(period = "max")
del Amazon["Dividends"], Amazon["Stock Splits"]

#Plot the stock into a line graph
nvda_graph = Nvidia.plot.line(y="Close", use_index=True)
tsla_graph = Tesla.plot.line(y="Close", use_index=True)
meta_graph = Meta.plot.line(y="Close", use_index=True)
msft_graph = Microsoft.plot.line(y="Close", use_index=True)
appl_graph = Apple.plot.line(y = "Close", use_index = True)
amzn_graph = Amazon.plot.line(y = "Close", use_index = True)




