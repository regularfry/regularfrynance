Yahoo! Finance market data downloader
=====================================

.. image:: https://img.shields.io/github/stars/regularfry/regularfrynance.svg?style=social&label=Star&maxAge=60
    :target: https://github.com/regularfry/regularfrynance
    :alt: Star this repo

.. image:: https://img.shields.io/twitter/follow/regularfry.svg?style=social&label=Follow&maxAge=60
    :target: https://twitter.com/regularfry
    :alt: Follow me on twitter


Ever since `Yahoo! finance <https://finance.yahoo.com>`_ decommissioned
their historical data API, many programs that relied on it to stop working.

**regularfrynance** aims to solve this problem by offering a reliable, threaded,
and Pythonic way to download historical market data from Yahoo! finance.

NOTE
~~~~

This project was forked from the upstream **yfinance** for two reasons:

1. I was needing to put somewhere to put bug-fixes in the upstream, so
   I wanted a fork for PRs.
2. I wanted to address rate limiting (which the upstream doesn't
   handle) and error handling in ways that need the published API to change.
3. I've got a chance to break with python 2.7 that the upstream might
   not.  Python 3 only from here on in.

This means that you should **continue to use yfinance** if you need
API compatibility with existing code, or if you need to be on python 2.7.

Quick Start
===========

The Ticker module
~~~~~~~~~~~~~~~~~

The ``Ticker`` module, which allows you to access
ticker data in a Pythonic way:

.. code:: python

    import regularfrynance as rf

    msft = rf.Ticker("MSFT")

    # check the ticker is available at Yahoo
    if not msft.is_available():
	raise Exception("MSFT is not available")

    # get stock info
    msft.info

    # get historical market data
    hist = msft.history(period="max")

    # show actions (dividends, splits)
    msft.actions

    # show dividends
    msft.dividends

    # show splits
    msft.splits

    # show financials
    msft.financials
    msft.quarterly_financials

    # show major holders
    msft.major_holders

    # show institutional holders
    msft.institutional_holders

    # show balance heet
    msft.balance_sheet
    msft.quarterly_balance_sheet

    # show cashflow
    msft.cashflow
    msft.quarterly_cashflow

    # show earnings
    msft.earnings
    msft.quarterly_earnings

    # show the currency used for balance_sheet, cashflow, earnings
    # Note that this is not always the same as .info['currency'].
    msft.financials_currency

    # show sustainability
    msft.sustainability

    # show analysts recommendations
    msft.recommendations

    # show next event (earnings, etc)
    msft.calendar

    # show options expirations
    msft.options

    # get option chain for specific expiration
    opt = msft.option_chain('YYYY-MM-DD')
    # data available via: opt.calls, opt.puts

If you want to use a proxy server for downloading data, use:

.. code:: python

    import regularfrynance as rf

    msft = rf.Ticker("MSFT", proxy="PROXY_SERVER")
    ...

To initialize multiple ``Ticker`` objects, use

.. code:: python

    import regularfrynance as rf

    tickers = rf.Tickers('msft aapl goog')
    # ^ returns a named tuple of Ticker objects

    # access each ticker using (example)
    tickers.msft.info
    tickers.aapl.history(period="1mo")
    tickers.goog.actions


Fetching data for multiple tickers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import regularfrynance as rf
    data = rf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")


I've also added some options to make life easier :)

.. code:: python

    data = rf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = "SPY AAPL MSFT",

            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            period = "ytd",

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = "1m",

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = 'ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust = True,

            # download pre/post regular market hours data
            # (optional, default is False)
            prepost = True,

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads = True,

            # proxy URL scheme use use when downloading
            # (optional, default is None)
            proxy = None
        )


``pandas_datareader`` override
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your code uses ``pandas_datareader`` and you want to download data faster,
you can "hijack" ``pandas_datareader.data.get_data_yahoo()`` method to use
**regularfrynance** while making sure the returned data is in the same format as
**pandas_datareader**'s ``get_data_yahoo()``.

.. code:: python

    from pandas_datareader import data as pdr

    import regularfrynance as rf
    rf.pdr_override() # <== that's all it takes :-)

    # download dataframe
    data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")


Requirements
------------

* `Python <https://www.python.org>`_ >= 3.4+
* `Pandas <https://github.com/pydata/pandas>`_ (tested to work with >=0.23.1)
* `Numpy <http://www.numpy.org>`_ >= 1.11.1
* `requests <http://docs.python-requests.org/en/master/>`_ >= 2.14.2


Optional (if you want to use ``pandas_datareader``)
---------------------------------------------------

* `pandas_datareader <https://github.com/pydata/pandas-datareader>`_ >= 0.4.0

Legal Stuff
------------

**regularfrynance** is distributed under the **Apache Software License**. See the `LICENSE.txt <./LICENSE.txt>`_ file in the release for details.


P.S.
------------

Please drop me an note with any feedback you have.

Alex Young alex@blackkettle.org
