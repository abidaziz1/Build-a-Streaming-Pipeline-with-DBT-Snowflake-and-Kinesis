# Build a Streaming Pipeline with DBT, Snowflake, and Kinesis

A comprehensive data pipeline project demonstrating real-time stock market data streaming and analytics using modern data engineering tools.

## 🏗️ Architecture Overview

This project implements a complete data pipeline that:
- Fetches real-time stock market data using yfinance
- Streams data through AWS Kinesis Data Firehose
- Stores data in AWS S3 and Snowflake
- Transforms data using DBT (Data Build Tool)
- Provides analytics on both batch and streaming data

## 📁 Project Structure

```
├── scripts/                          # Python data pipeline scripts
│   ├── Batch_Data_yfinance_script.py # Batch data collection from Yahoo Finance
│   └── Stream_Data_yfinance_script.py # Real-time streaming data script
├── sql/                              # Raw SQL files for additional queries
├── docs/                             # Documentation and process guides
├── models/                           # DBT models for data transformation
│   ├── stock_market/                 # Stock market data models
│   │   ├── staging/                  # Staging models for raw data
│   │   └── fact/                     # Fact tables for analytics
│   └── netflix/                      # Netflix analytics models (example)
├── datasets/                         # Sample datasets
├── tests/                            # DBT data quality tests
├── macros/                           # DBT macros for reusable SQL
└── analyses/                         # Ad-hoc analysis queries
```

## 🚀 Features

### Data Ingestion
- **Batch Processing**: Historical stock data collection for multiple tickers
- **Real-time Streaming**: Live stock price updates via Kinesis Data Firehose
- **Multi-source**: Support for various financial data providers

### Data Transformation (DBT Models)
- **Staging Models**: Raw data cleaning and standardization
- **Fact Tables**: Aggregated analytics tables including:
  - Rolling 2-year high/low calculations
  - Stock trend analysis
  - Volume and price analytics

### Analytics & Insights
- Stock performance trends
- Rolling window calculations
- Volume analysis
- Price movement patterns

## 🛠️ Technology Stack

- **Data Collection**: Python, yfinance
- **Streaming**: AWS Kinesis Data Firehose
- **Storage**: AWS S3, Snowflake
- **Transformation**: DBT (Data Build Tool)
- **Analytics**: SQL, Python

## 📊 Data Sources

- **Primary**: Yahoo Finance (via yfinance library)
- **Stock Symbols**: AAPL, MSFT, GOOGL, NFLX, AMZN, META, ADBE, ABNB, NVDA
- **Data Points**: Open, High, Low, Close, Volume, Timestamp

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8+
- AWS Account with Kinesis and S3 access
- Snowflake account
- DBT installed and configured

### Setup
1. Install Python dependencies:
   ```bash
   pip install yfinance boto3 dbt-snowflake
   ```

2. Configure AWS credentials
3. Set up Snowflake connection in DBT profiles
4. Run batch data collection:
   ```bash
   python scripts/Batch_Data_yfinance_script.py
   ```

5. Start streaming pipeline:
   ```bash
   python scripts/Stream_Data_yfinance_script.py
   ```

6. Run DBT transformations:
   ```bash
   dbt run
   dbt test
   ```

## 📈 Analytics Models

### Stock Market Models
- `YAHOO_STOCKS_BATCH_DATA`: Staging table for historical data
- `YAHOO_STOCKS_STREAMING_DATA`: Staging table for real-time data
- `ROLLING_TWO_YEAR_HIGH`: 2-year rolling high calculations
- `ROLLING_TWO_YEAR_LOW`: 2-year rolling low calculations
- `STOCK_TRENDS`: Trend analysis and patterns

## 📝 Documentation

Additional documentation can be found in the `docs/` directory:
- Process steps for data ingestion
- Batch data model specifications
- SQL code examples

## 🧪 Testing

The project includes DBT tests for data quality:
- Null value checks
- Data freshness tests
- Referential integrity tests

Run tests with:
```bash
dbt test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [DBT Documentation](https://docs.getdbt.com/)
- [Snowflake Documentation](https://docs.snowflake.com/)
- [AWS Kinesis Documentation](https://docs.aws.amazon.com/kinesis/)
- [yfinance Documentation](https://pypi.org/project/yfinance/)
