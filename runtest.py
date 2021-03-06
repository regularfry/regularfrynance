#!/usr/bin/env python
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/regularfry/regularfrynance

"""
Sanity check for most common library uses all working

- Stock: Microsoft
- ETF: Russell 2000 Growth
- Mutual fund: Vanguard 500 Index fund
- Index: S&P500
- Currency BTC-USD
"""

import regularfrynance as rf


def test_regularfrynance():
    assert rf.Ticker("NOSUCHTICKER").is_available() is False

    symbols = [
        "MSFT", 
        "VOD.L",
        "IWO", 
        "VFINX", 
        "^GSPC", 
        "BTC-USD"
    ]
    
    for symbol in symbols:
        print(">>", symbol, end=" ... ")
        ticker = rf.Ticker(symbol)
        assert ticker.is_available()

        # always should have info and history for valid symbols
        assert ticker.info is not None and ticker.info != {}
        assert ticker.history(period="max").empty is False

        # following should always gracefully handled, no crashes
        ticker.cashflow
        ticker.balance_sheet
        ticker.financials
        ticker.sustainability
        ticker.major_holders
        ticker.institutional_holders

        print("OK")


if __name__ == "__main__":
    test_regularfrynance()
