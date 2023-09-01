import requests
import datetime
import pandas as pd

from fugle_marketdata import RestClient

fugle_token = '{fugle_token}'
fugle_api_key = '{fugle_api_key}'
FinMind_token = "{FinMind_token}"

def get_date():
    start_date = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.today().strftime("%Y-%m-%d")
    return start_date, end_date

# connect fugle api to get stock name
def get_stock_name(stock_code):
    client = RestClient(api_key=fugle_api_key)
    stock = client.stock
    stock = stock.intraday.ticker(symbol=stock_code)
    stock_name = stock['name']

    return stock_name

def get_stock_data(stock_code):

    # 設定 API 請求的 URL
    finmind_api_url = "https://api.finmindtrade.com/api/v4/data"

    start_date, end_date = get_date()

    # 設定 API 請求參數
    parameter = {
        "dataset": "TaiwanStockPrice",
        "data_id": stock_code,
        "start_date": start_date,
        "end_date": end_date,
        "token": FinMind_token  # 參考登入，獲取金鑰
    }

    # 透過 HTTP GET 請求獲取股票資料
    resp = requests.get(finmind_api_url, params=parameter)
    stock_data = resp.json()

    # 將 JSON 資料轉換成 Pandas DataFrame 格式
    stock = pd.DataFrame(stock_data["data"])

    # 將日期欄位轉換為索引，並設定為日期格式
    stock.index = pd.to_datetime(stock['date'])

    # 移除不需要的欄位
    del stock['Trading_money']
    del stock['Trading_turnover']
    del stock['date']
    del stock['spread']
    del stock['stock_id']

    # 重新命名欄位名稱以便更好的表示股票資訊
    stock.rename(columns={
        'Trading_Volume': 'Volume',
        'close': 'Close',
        'max': 'High',
        'min': "Low",
        'open': 'Open'
    }, inplace=True)

    # 設定 DataFrame 的索引名稱為 'Date'
    stock.index.name = 'Date'

    # 將交易量除以 1000，以便縮小顯示
    stock['Volume'] = stock['Volume'].apply(lambda x: int(x / 1000))

    return stock

