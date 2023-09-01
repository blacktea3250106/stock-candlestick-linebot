import os
import datetime
from imgurpython import ImgurClient

client_id = '{client_id}'
client_secret = '{client_secret}'
access_token = '{access_token}'
refresh_token = '{refresh_token}'

def get_imgurl(stock_code):
    
    client= ImgurClient(client_id, client_secret, access_token, refresh_token)

    config = {
        'name': stock_code, 
        'title': stock_code, 
        'description': str(datetime.date.today()) 
        }   
    
    try:
        stock_imgurl = client.upload_from_path(stock_code+'.png', config=config, anon=False)['link']
    except Exception as e:
        print(f"An error occurred while uploading {stock_code} image: {e}")

    os.remove(stock_code+'.png')

    print(stock_imgurl)
    return stock_imgurl


