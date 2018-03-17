from    coinapi_v1 import CoinAPIv1
import  datetime

test_key  =  'DFC28861-D035-41E6-AE27-5CBCF871416E'


start_of_2015 = datetime.date(2015, 1, 1)
start_of_2016 = datetime.date(2016, 1, 1)
start_of_2017 = datetime.date(2017, 1, 1)
start_of_2018 = datetime.date(2018, 1, 1)


api       = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()
assets    = api.metadata_list_assets()
symbols   = api.metadata_list_symbols()
periods   = api.ohlcv_list_all_periods()

current_rates = api.exchange_rates_get_all_current_rates('BTC')

#some pre-processing for practical module specific names are not that bad a practice generally...
asset_ids    = []
exchange_ids = []
symbol_ids   = []
period_ids   = []

for asset in assets:
    asset_ids.append(asset['asset_id'])

for exchange in exchanges:
    exchange_ids.append(exchange['exchange_id'])

for symbol in symbols:
    symbol_ids.append(symbol['symbol_id'])

for period in periods:
    period_ids.append(period['period_id'])

# details(thing_id) prints short info related to the thing_id
# finish all coinapi specific iterables like symbols, exchanges and assets etc... 
# than populate a list named all_ids
# implement a details(thing_id)) function which searchs the list which contains all ids.

def print_exchanges():
    global exchanges
    print('\n[coinapi: exchanges list]')
    for exchange in exchanges:
        print('  Exchange ID: %s'      % exchange['exchange_id'])
        print('  Exchange website: %s' % exchange['website'])
        print('  Exchange name: %s'    % exchange['name'])
        print('\n')
        
def print_assets():
    global assets
    print('\n[coinapi: assets list]')
    for asset in assets:
        print('Asset ID: %s'             % asset['asset_id'])
        print('Asset name: %s'           % asset['name'])
        print('Asset type (crypto?): %s' % asset['type_is_crypto'])
        print('\n')

def print_symbols():
    global symbols
    print('\n[coinapi: symbols list]')
    for symbol in symbols:
        print('Symbol ID: %s'   % symbol['symbol_id'])    
        print('Exchange ID: %s' % symbol['exchange_id'])
        print('Symbol type: %s' % symbol['symbol_type'])
        print('Asset ID base: %s' % symbol['asset_id_base'])
        print('Asset ID quote: %s' % symbol['asset_id_quote'])
        if (symbol['symbol_type'] == 'FUTURES'):
            print('Future delivery time: %s' % symbol['future_delivery_time'])
        if (symbol['symbol_type'] == 'OPTION'):
            print('Option type is call: %s' % symbol['option_type_is_call'])
            print('Option strike price: %s' % symbol['option_strike_price'])
            print('Option contract unit: %s' % symbol['option_contract_unit'])
            print('Option exercise style: %s' % symbol['option_exercise_style'])
            print('Option expiration time: %s' % symbol['option_expiration_time'])
        print('\n')

def exchange_rate(asset_1, asset_2):
    global api
    result = {}
    exchange_rate   = api.exchange_rates_get_specific_rate(asset_1, asset_2)
    result['time']  = exchange_rate['time']
    result['base']  = exchange_rate['asset_id_base']
    result['quote'] = exchange_rate['asset_id_quote']
    result['rate']  = exchange_rate['rate']
    return result

# overload the exchange_rate function for the sake of generality
def exchange_rate(asset_1, asset_2, date_time):
    global api
    date_time_iso   = date_time.isoformat()
    result = {}
    exchange_rate   = api.exchange_rates_get_specific_rate(asset_1, asset_2, {'time' : date_time_iso})
    result['time']  = exchange_rate['time']
    result['base']  = exchange_rate['asset_id_base']
    result['quote'] = exchange_rate['asset_id_quote']
    result['rate']  = exchange_rate['rate']
    return result

def print_exchange_rate(asset_1, asset_2):
    global api
    exchange_rate   = api.exchange_rates_get_specific_rate(asset_1, asset_2)
    print('Time:  %s' % exchange_rate['time'])
    print('Base:  %s' % exchange_rate['asset_id_base'])
    print('Quote: %s' % exchange_rate['asset_id_quote'])
    print('Rate:  %s' % exchange_rate['rate'])
    print('\n')

def print_exchange_rate(asset_1, asset_2, date_time, date_time):
    global api
    date_time_iso   = date_time.isoformat()
    result = {}
    exchange_rate   = api.exchange_rates_get_specific_rate(asset_1, asset_2, {'time' : date_time_iso})
    print('Time:  %s' % exchange_rate['time'])
    print('Base:  %s' % exchange_rate['asset_id_base'])
    print('Quote: %s' % exchange_rate['asset_id_quote'])
    print('Rate:  %s' % exchange_rate['rate'])
    print('\n')

def print_periodes():
    global periods
    for period in periods:
        print('ID: %s' % period['period_id'])
        print('Seconds: %s' % period['length_seconds'])
        print('Months: %s' % period['length_months'])
        print('Unit count: %s' % period['unit_count'])
        print('Unit name: %s' % period['unit_name'])
        print('Display name: %s' % period['display_name'])
        print('\n')
    
def current_rates():
    current_rates = api.exchange_rates_get_all_current_rates('BTC')
    return current_rates

def print_current_rates():
    current_rates = api.exchange_rates_get_all_current_rates('BTC')
    print("Asset ID Base: %s" % current_rates['asset_id_base'])
    for rate in current_rates['rates']:
        print('Time: %s' % rate['time'])
        print('Quote: %s' % rate['asset_id_quote'])
        print('Rate: %s' % rate['rate'])
        print('\n')

def ohlcv_latest():
    ohlcv_latest = api.ohlcv_latest_data('BITSTAMP_SPOT_BTC_USD', {'period_id': '1MIN'})
    return ohlcv_latest

def print_ohlcv_latest():
    ohlcv_latest = api.ohlcv_latest_data('BITSTAMP_SPOT_BTC_USD', {'period_id': '1MIN'})
    for period in ohlcv_latest:
        print('Period start: %s' % period['time_period_start'])
        print('Period end: %s' % period['time_period_end'])
        print('Time open: %s' % period['time_open'])
        print('Time close: %s' % period['time_close'])
        print('Price open: %s' % period['price_open'])
        print('Price close: %s' % period['price_close'])
        print('Price low: %s' % period['price_low'])
        print('Price high: %s' % period['price_high'])
        print('Volume traded: %s' % period['volume_traded'])
        print('Trades count: %s' % period['trades_count'])
        print('\n')

def btc_ohlcv_historical(_time_start, _period_id):
    '''returns historical value of the bitcoin for _period_id starting from _time_start
    @params
    _period_id      string
    _time_start     datetime.datetime 

    @return
    dictionary containing ohlcv data
    '''
    global api
    _time_start_iso         = _time_start.isoformat()
    return api.ohlcv_historical_data('BITSTAMP_SPOT_BTC_USD', {'period_id': _period_id, 'time_start': _time_start_iso})

def btc_ohlcv_historical(_time_start, _period_id):
    '''returns historical value of the bitcoin for _period_id starting from _time_start
    @params
    _period_id      string
    _time_start     datetime.datetime 

    @return
    void
    '''
    global api
    _time_start_iso         = _time_start.isoformat()
    ohlcv_historical = api.ohlcv_historical_data('BITSTAMP_SPOT_BTC_USD', {'period_id': _period_id, 'time_start': _time_start_iso})
    for period in ohlcv_historical:
        print('Period start: %s' % period['time_period_start'])
        print('Period end: %s' % period['time_period_end'])
        print('Time open: %s' % period['time_open'])
        print('Time close: %s' % period['time_close'])
        print('Price open: %s' % period['price_open'])
        print('Price close: %s' % period['price_close'])
        print('Price low: %s' % period['price_low'])
        print('Price high: %s' % period['price_high'])
        print('Volume traded: %s' % period['volume_traded'])
        print('\n')

def latest_trades():
    global api
    return api.trades_latest_data_all()

def print_latest_trades():
    global api
    latest_trades = api.trades_latest_data_all()
    for data in latest_trades:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('UUID: %s' % data['uuid'])
        print('Price: %s' % data['price'])
        print('Size: %s' % data['size'])
        print('Taker Side: %s' % data['taker_side'])
        print('\n')


# exchange_rate function should be tested in many ways before proceeding.


'''

exchange_rate = api.exchange_rates_get_specific_rate('BTC', 'USD')

last_week = datetime.date(2017, 5, 18).isoformat()
exchange_rate_last_week = api.exchange_rates_get_specific_rate('BTC', 'USD', {'time': last_week})
print('Time: %s' % exchange_rate_last_week['time'])
print('Base: %s' % exchange_rate_last_week['asset_id_base'])
print('Quote: %s' % exchange_rate_last_week['asset_id_quote'])
print('Rate: %s' % exchange_rate_last_week['rate'])


# testing the datetime information...

last_week = datetime.datetime(2017, 5, 18, 21, 19, 45).isoformat()
exchange_rate_last_week = api.exchange_rates_get_specific_rate('BTC', 'USD', {'time': last_week})
print('Time: %s' % exchange_rate_last_week['time'])
print('Base: %s' % exchange_rate_last_week['asset_id_base'])
print('Quote: %s' % exchange_rate_last_week['asset_id_quote'])
print('Rate: %s' % exchange_rate_last_week['rate'])






# It is meaningful to focus on this function more deeply.
# define the following variables like start_of_2016, start_of_2017, start_of_2018, start_of_2019...



start_of_2016 = datetime.date(2016, 1, 1).isoformat()
ohlcv_historical = api.ohlcv_historical_data('BITSTAMP_SPOT_BTC_USD', {'period_id': '1MIN', 'time_start': start_of_2016})
for period in ohlcv_historical:
    print('Period start: %s' % period['time_period_start'])
    print('Period end: %s' % period['time_period_end'])
    print('Time open: %s' % period['time_open'])
    print('Time close: %s' % period['time_close'])
    print('Price open: %s' % period['price_open'])
    print('Price close: %s' % period['price_close'])
    print('Price low: %s' % period['price_low'])
    print('Price high: %s' % period['price_high'])
    print('Volume traded: %s' % period['volume_traded'])
    print('Trades count: %s' % period['trades_count'])






latest_trades_doge = api.trades_latest_data_symbol('BITTREX_SPOT_BTC_DOGE')
for data in latest_trades_doge:
    print('Symbol ID: %s' % data['symbol_id'])
    print('Time Exchange: %s' % data['time_exchange'])
    print('Time CoinAPI: %s' % data['time_coinapi'])
    print('UUID: %s' % data['uuid'])
    print('Price: %s' % data['price'])
    print('Size: %s' % data['size'])
    print('Taker Side: %s' % data['taker_side'])

historical_trades_btc = api.trades_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})
for data in historical_trades_btc:
    print('Symbol ID: %s' % data['symbol_id'])
    print('Time Exchange: %s' % data['time_exchange'])
    print('Time CoinAPI: %s' % data['time_coinapi'])
    print('UUID: %s' % data['uuid'])
    print('Price: %s' % data['price'])
    print('Size: %s' % data['size'])
    print('Taker Side: %s' % data['taker_side'])

current_quotes = api.quotes_current_data_all()
print(current_quotes)
for quote in current_quotes:
    print('Symbol ID: %s' % quote['symbol_id'])
    print('Time Exchange: %s' % quote['time_exchange'])
    print('Time CoinAPI: %s' % quote['time_coinapi'])
    print('Ask Price: %s' % quote['ask_price'])
    print('Ask Size: %s' % quote['ask_size'])
    print('Bid Price: %s' % quote['bid_price'])
    print('Bid Size: %s' % quote['bid_size'])
    if 'last_trade' in quote:
        print('Last Trade: %s' % quote['last_trade'])

current_quote_btc_usd = api.quotes_current_data_symbol('BITSTAMP_SPOT_BTC_USD')
print('Symbol ID: %s' % current_quote_btc_usd['symbol_id'])
print('Time Exchange: %s' % current_quote_btc_usd['time_exchange'])
print('Time CoinAPI: %s' % current_quote_btc_usd['time_coinapi'])
print('Ask Price: %s' % current_quote_btc_usd['ask_price'])
print('Ask Size: %s' % current_quote_btc_usd['ask_size'])
print('Bid Price: %s' % current_quote_btc_usd['bid_price'])
print('Bid Size: %s' % current_quote_btc_usd['bid_size'])
if 'last_trade' in current_quote_btc_usd:
    last_trade = current_quote_btc_usd['last_trade']
    print('Last Trade:')
    print('- Taker Side: %s' % last_trade['taker_side'])
    print('- UUID: %s' % last_trade['uuid'])
    print('- Time Exchange: %s' % last_trade['time_exchange'])
    print('- Price: %s' % last_trade['price'])
    print('- Size: %s' % last_trade['size'])
    print('- Time CoinAPI: %s' % last_trade['time_coinapi'])


current_quotes = api.quotes_current_data_all()
print(current_quotes)
for quote in current_quotes:
    print('Symbol ID: %s' % quote['symbol_id'])
    print('Time Exchange: %s' % quote['time_exchange'])
    print('Time CoinAPI: %s' % quote['time_coinapi'])
    print('Ask Price: %s' % quote['ask_price'])
    print('Ask Size: %s' % quote['ask_size'])
    print('Bid Price: %s' % quote['bid_price'])
    print('Bid Size: %s' % quote['bid_size'])
    if 'last_trade' in quote:
        print('Last Trade: %s' % quote['last_trade'])


current_quote_btc_usd = api.quotes_current_data_symbol('BITSTAMP_SPOT_BTC_USD')
print('Symbol ID: %s' % current_quote_btc_usd['symbol_id'])
print('Time Exchange: %s' % current_quote_btc_usd['time_exchange'])
print('Time CoinAPI: %s' % current_quote_btc_usd['time_coinapi'])
print('Ask Price: %s' % current_quote_btc_usd['ask_price'])
print('Ask Size: %s' % current_quote_btc_usd['ask_size'])
print('Bid Price: %s' % current_quote_btc_usd['bid_price'])
print('Bid Size: %s' % current_quote_btc_usd['bid_size'])
if 'last_trade' in current_quote_btc_usd:
    last_trade = current_quote_btc_usd['last_trade']
    print('Last Trade:')
    print('- Taker Side: %s' % last_trade['taker_side'])
    print('- UUID: %s' % last_trade['uuid'])
    print('- Time Exchange: %s' % last_trade['time_exchange'])
    print('- Price: %s' % last_trade['price'])
    print('- Size: %s' % last_trade['size'])
    print('- Time CoinAPI: %s' % last_trade['time_coinapi'])


quotes_latest_data = api.quotes_latest_data_all()
for quote in quotes_latest_data:
    print('Symbol ID: %s' % quote['symbol_id'])
    print('Time Exchange: %s' % quote['time_exchange'])
    print('Time CoinAPI: %s' % quote['time_coinapi'])
    print('Ask Price: %s' % quote['ask_price'])
    print('Ask Size: %s' % quote['ask_size'])
    print('Bid Price: %s' % quote['bid_price'])
    print('Bid Size: %s' % quote['bid_size'])


quotes_latest_data_btc_usd = api.quotes_latest_data_symbol('BITSTAMP_SPOT_BTC_USD')
for quote in quotes_latest_data_btc_usd:
    print('Symbol ID: %s' % quote['symbol_id'])
    print('Time Exchange: %s' % quote['time_exchange'])
    print('Time CoinAPI: %s' % quote['time_coinapi'])
    print('Ask Price: %s' % quote['ask_price'])
    print('Ask Size: %s' % quote['ask_size'])
    print('Bid Price: %s' % quote['bid_price'])
    print('Bid Size: %s' % quote['bid_size'])


quotes_historical_data_btc_usd = api.quotes_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})
for quote in quotes_historical_data_btc_usd:
    print('Symbol ID: %s' % quote['symbol_id'])
    print('Time Exchange: %s' % quote['time_exchange'])
    print('Time CoinAPI: %s' % quote['time_coinapi'])
    print('Ask Price: %s' % quote['ask_price'])
    print('Ask Size: %s' % quote['ask_size'])
    print('Bid Price: %s' % quote['bid_price'])
    print('Bid Size: %s' % quote['bid_size'])


orderbooks_current_data = api.orderbooks_current_data_all()
for data in orderbooks_current_data:
    print('Symbol ID: %s' % data['symbol_id'])
    print('Time Exchange: %s' % data['time_exchange'])
    print('Time CoinAPI: %s' % data['time_coinapi'])
    print('Asks:')
    for ask in data['asks']:
        print('- Price: %s' % ask['price'])
        print('- Size: %s' % ask['size'])
    print('Bids:')
    for bid in data['bids']:
        print('- Price: %s' % bid['price'])
        print('- Size: %s' % bid['size'])

orderbooks_current_data_btc_usd = api.orderbooks_current_data_symbol('BITSTAMP_SPOT_BTC_USD')
print('Symbol ID: %s' % orderbooks_current_data_btc_usd['symbol_id'])
print('Time Exchange: %s' % orderbooks_current_data_btc_usd['time_exchange'])
print('Time CoinAPI: %s' % orderbooks_current_data_btc_usd['time_coinapi'])
print('Asks:')
for ask in orderbooks_current_data_btc_usd['asks']:
    print('- Price: %s' % ask['price'])
    print('- Size: %s' % ask['size'])
print('Bids:')
for bid in orderbooks_current_data_btc_usd['bids']:
    print('- Price: %s' % bid['price'])
    print('- Size: %s' % bid['size'])

orderbooks_historical_data_btc_usd = api.orderbooks_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})
for data in orderbooks_historical_data_btc_usd:
    print('Symbol ID: %s' % data['symbol_id'])
    print('Time Exchange: %s' % data['time_exchange'])
    print('Time CoinAPI: %s' % data['time_coinapi'])
    print('Asks:')
    for ask in data['asks']:
        print('- Price: %s' % ask['price'])
        print('- Size: %s' % ask['size'])
    print('Bids:')
    for bid in data['bids']:
        print('- Price: %s' % bid['price'])
        print('- Size: %s' % bid['size'])


twitter_latest_data = api.twitter_latest_data()
twitter_historical_data = api.twitter_historical_data({'time_start': start_of_2016})




'''






