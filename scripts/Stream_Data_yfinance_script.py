import boto3
import yfinance as yf
import json
import time
import numpy as np

def put_data_to_firehose(delivery_stream_name, data):
    firehose_client = boto3.client('firehose')
    data_str = json.dumps(data, default=convert_to_json_serializable) + '\n'
    response = firehose_client.put_record(
        DeliveryStreamName=delivery_stream_name,
        Record={
            'Data': data_str
        }
    )
    return response

def convert_to_json_serializable(obj):
    if isinstance(obj, (np.integer, np.floating, np.bool_)):
        return obj.item()
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def fetch_stock_data(symbol):
    data = yf.download(symbol, period="1d", interval="1m")
    if not data.empty:
        last_row = data.iloc[-1]
        return {
            'symbol': symbol,
            'timestamp': int(time.time()),
            'open': float(last_row['Open'].iloc[0]),  
            'high': float(last_row['High'].iloc[0]),   
            'low': float(last_row['Low'].iloc[0]),     
            'close': float(last_row['Close'].iloc[0]), 
            'volume': int(last_row['Volume'].iloc[0])  
        }
    return None

def main():
    delivery_stream_name = 'stock-market-data'  # Replace with your Kinesis Data Firehose Delivery Stream name
    symbols = ['AAPL', 'MSFT', 'GOOGL','NFLX','AMZN','META','ADBE','ABNB','NVDA']  # Add more stock symbols as needed
    interval_seconds = 60  # Fetch data every 60 seconds

    while True:
        for symbol in symbols:
            data = fetch_stock_data(symbol)
            if data:
                response = put_data_to_firehose(delivery_stream_name, data)
                print(f"Data sent to Kinesis Firehose for {symbol}. RecordId: {response['RecordId']}")
        time.sleep(interval_seconds)

if __name__ == '__main__':
    main()