import mplfinance as mpf
import matplotlib.pyplot as plt

def draw_candlestick_chart(stock_code, stock_history):
    kwargs = dict(
    type='candle',
    mav=(5, 10, 20, 60),
    tight_layout=False,
    volume=True,
    figratio=(2, 1),  # 調整為適合的長寬比例
    figscale=2,      # 調整整體圖表的大小
    title='\n\n               ' + stock_code,
    ylabel='',
    ylabel_lower=''
    )

    # 定義市場顏色
    mc = mpf.make_marketcolors(
        up='#FC585B',
        down='#45C68A',
        edge='i',
        wick='i',
        volume='in',
        inherit=True
    )

    # 定義繪圖風格
    s = mpf.make_mpf_style(
            gridaxis='both', 
            gridstyle=':', 
            y_on_right=True, 
            marketcolors=mc,
            mavcolors=['darkorange', '#2196F3', 'purple', 'green'],
            rc={'font.size':20, "xtick.color": 'none'}
    )

    # 設定中文字體和正負號顯示
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False

    # 儲存圖表參數
    saving_params = dict(fname=stock_code + '.png', bbox_inches='tight', pad_inches=0.5)


    # 繪製股票圖表
    mpf.plot(stock_history, **kwargs, style=s, savefig=saving_params)

