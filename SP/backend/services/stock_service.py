import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class StockService:
    """Service for interacting with stock market data sources"""
    
    def __init__(self):
        # In a real app, you would initialize API clients here
        # and possibly set up credentials for data providers
        pass
    
    def search_stocks(self, query, limit=10):
        """Search for stocks based on a query string"""
        # In a real app, this would query a stock API
        # For now, return mock data
        all_stocks = [
            {"symbol": "AAPL", "name": "Apple Inc."},
            {"symbol": "MSFT", "name": "Microsoft Corporation"},
            {"symbol": "GOOGL", "name": "Alphabet Inc."},
            {"symbol": "AMZN", "name": "Amazon.com Inc."},
            {"symbol": "META", "name": "Meta Platforms Inc."},
            {"symbol": "TSLA", "name": "Tesla Inc."},
            {"symbol": "NVDA", "name": "NVIDIA Corporation"},
            {"symbol": "JPM", "name": "JPMorgan Chase & Co."},
            {"symbol": "V", "name": "Visa Inc."},
            {"symbol": "JNJ", "name": "Johnson & Johnson"}
        ]
        
        # Filter by query
        if query:
            query = query.lower()
            filtered_stocks = [
                stock for stock in all_stocks 
                if query in stock["symbol"].lower() or query in stock["name"].lower()
            ]
            return filtered_stocks[:limit]
        
        return all_stocks[:limit]
    
    def get_stock_details(self, symbol):
        """Get detailed information about a specific stock"""
        # In a real app, this would fetch data from an API
        # Return mock data based on the symbol
        base_price = 0
        if symbol == "AAPL":
            base_price = 243.56
        elif symbol == "MSFT":
            base_price = 415.67
        elif symbol == "GOOGL":
            base_price = 187.32
        elif symbol == "AMZN":
            base_price = 192.45
        elif symbol == "META":
            base_price = 532.78
        elif symbol == "TSLA":
            base_price = 267.89
        elif symbol == "NVDA":
            base_price = 1245.67
        else:
            # Generate a semi-random price for other symbols
            # Use the sum of ASCII values of the symbol as a seed
            seed = sum(ord(c) for c in symbol)
            np.random.seed(seed)
            base_price = np.random.randint(50, 500) + np.random.random()
        
        change_percent = np.random.normal(0, 2)  # Random change with normal distribution
        change = base_price * change_percent / 100
        
        return {
            "symbol": symbol,
            "name": next((s["name"] for s in self.search_stocks("", 100) if s["symbol"] == symbol), f"{symbol} Corp"),
            "price": base_price,
            "change": change,
            "percentChange": change_percent,
            "marketCap": round(base_price * np.random.randint(10, 100) * 1e6 / 1e12, 2),  # In trillions
            "volume": round(np.random.randint(1, 100) * 1e6 / 1e6, 1),  # In millions
            "avgVolume": round(np.random.randint(1, 100) * 1e6 / 1e6, 1),  # In millions
            "pe": round(np.random.randint(10, 40) + np.random.random(), 1),
            "eps": round(base_price / np.random.randint(10, 40), 2),
            "dividend": round(np.random.random() * 3, 2),  # 0-3% dividend
            "high52w": round(base_price * (1 + np.random.random() * 0.3), 2),  # Up to 30% higher
            "low52w": round(base_price * (1 - np.random.random() * 0.3), 2),  # Up to 30% lower
            "open": round(base_price - change * np.random.random(), 2),
            "previousClose": round(base_price - change, 2),
            "timestamp": datetime.now().isoformat(),
            "analyst": {
                "buy": np.random.randint(5, 30),
                "hold": np.random.randint(1, 15),
                "sell": np.random.randint(0, 5)
            }
        }
    
    def get_historical_data(self, symbol, timeframe='1m'):
        """Get historical price data for a stock over a specified timeframe"""
        # Determine data points based on timeframe
        if timeframe == '1d':
            # 5-minute intervals for a day (78 points for 6.5 hour trading day)
            periods = 78
            freq = '5min'
            start_date = datetime.now() - timedelta(days=1)
            date_format = '%H:%M'
        elif timeframe == '1w':
            # Hourly for a week
            periods = 7 * 6
            freq = '1h'
            start_date = datetime.now() - timedelta(weeks=1)
            date_format = '%a'
        elif timeframe == '1m':
            # Daily for a month
            periods = 30
            freq = '1D'
            start_date = datetime.now() - timedelta(days=30)
            date_format = 'Week %U'
        elif timeframe == '3m':
            # Daily for 3 months
            periods = 90
            freq = '1D'
            start_date = datetime.now() - timedelta(days=90)
            date_format = '%b'
        elif timeframe == '1y':
            # Weekly for a year
            periods = 52
            freq = '1W'
            start_date = datetime.now() - timedelta(days=365)
            date_format = '%b'
        elif timeframe == 'all':
            # Monthly for 5 years
            periods = 60
            freq = '1M'
            start_date = datetime.now() - timedelta(days=365 * 5)
            date_format = '%Y'
        else:
            # Default to monthly data
            periods = 30
            freq = '1D'
            start_date = datetime.now() - timedelta(days=30)
            date_format = '%b %d'
            
        # Get current stock price and info to base historical data on
        stock_info = self.get_stock_details(symbol)
        current_price = stock_info['price']
        
        # Create a date range
        date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
        
        # Generate synthetic price data with a trend and some randomness
        # Base the trend direction on the current percent change
        trend = 0.02 if stock_info['percentChange'] > 0 else -0.02
        
        # Generate a semi-random walk with the trend
        np.random.seed(sum(ord(c) for c in symbol))  # Set seed based on symbol
        random_walk = np.random.normal(trend, 0.02, periods).cumsum()
        
        # Scale to start from a logical past price and end at the current price
        start_factor = 1 - random_walk[-1]  # Adjust to make the last point end at 0
        price_factors = 1 + random_walk + start_factor
        
        # Calculate prices and ensure the last price matches current price
        prices = current_price / price_factors[-1] * price_factors
        
        # Format dates according to the timeframe
        labels = [date.strftime(date_format) for date in date_range]
        
        # For timeframes like 1m that use "Week X" formatting, make labels unique
        if timeframe == '1m':
            # Group by week number and count occurrences
            week_counts = {}
            for i, label in enumerate(labels):
                week_counts[label] = week_counts.get(label, 0) + 1
            
            # Only keep one instance of each week label
            unique_labels = []
            for label in labels:
                if label in week_counts and week_counts[label] > 0:
                    unique_labels.append(label)
                    week_counts[label] = 0
                else:
                    unique_labels.append("")
            
            labels = unique_labels
            
        # Return formatted historical data
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "labels": labels,
            "data": prices.tolist(),
            "timestamps": [date.isoformat() for date in date_range],
            "updated_at": datetime.now().isoformat(),
            "updated_by": "lucifer0177continue"  # Using the provided username
        }
    
    def get_market_summary(self):
        """Get a summary of the overall market including major indices"""
        # This would typically fetch real market data
        # For now, return mock data
        current_timestamp = datetime.now().isoformat()
        
        return {
            "indices": [
                {"name": "S&P 500", "value": 5923.47, "change": 47.88, "percentChange": 0.81},
                {"name": "Dow Jones", "value": 40654.32, "change": 315.56, "percentChange": 0.78},
                {"name": "Nasdaq", "value": 18732.91, "change": -24.53, "percentChange": -0.13},
                {"name": "Russell 2000", "value": 2354.76, "change": 12.34, "percentChange": 0.53}
            ],
            "sectorPerformance": [
                {"name": "Technology", "percentChange": 1.2},
                {"name": "Healthcare", "percentChange": 0.8},
                {"name": "Financials", "percentChange": 0.5},
                {"name": "Consumer Discretionary", "percentChange": -0.3},
                {"name": "Communication Services", "percentChange": 0.9},
                {"name": "Industrials", "percentChange": 0.4},
                {"name": "Energy", "percentChange": -0.7},
                {"name": "Utilities", "percentChange": 0.2},
                {"name": "Materials", "percentChange": -0.1},
                {"name": "Real Estate", "percentChange": 0.3}
            ],
            "marketStatus": "open",
            "timestamp": "2025-03-12 05:55:29",  # Using the provided timestamp
            "updatedBy": "lucifer0177continue"   # Using the provided username
        }
        
    def get_market_movers(self, limit=5):
        """Get top gainers and losers in the market"""
        # This would typically fetch real market data
        # For now, return mock data
        
        # Top gainers
        gainers = [
            {"symbol": "XYZ", "name": "XYZ Corp", "price": 134.21, "change": 12.45, "percentChange": 10.23},
            {"symbol": "ABC", "name": "ABC Inc", "price": 56.78, "change": 4.32, "percentChange": 8.24},
            {"symbol": "DEF", "name": "DEF Holdings", "price": 89.45, "change": 5.67, "percentChange": 6.77},
            {"symbol": "GHI", "name": "GHI Tech", "price": 45.67, "change": 2.78, "percentChange": 6.48},
            {"symbol": "JKL", "name": "JKL Systems", "price": 112.34, "change": 6.23, "percentChange": 5.87},
            {"symbol": "MNO", "name": "MNO Pharma", "price": 78.90, "change": 4.12, "percentChange": 5.51},
            {"symbol": "PQR", "name": "PQR Energy", "price": 34.56, "change": 1.78, "percentChange": 5.43},
            {"symbol": "STU", "name": "STU Networks", "price": 23.45, "change": 1.12, "percentChange": 5.01}
        ]
        
        # Top losers
        losers = [
            {"symbol": "AAA", "name": "AAA Industries", "price": 42.63, "change": -8.21, "percentChange": -16.15},
            {"symbol": "BBB", "name": "BBB Tech", "price": 105.32, "change": -12.45, "percentChange": -10.57},
            {"symbol": "CCC", "name": "CCC Systems", "price": 27.89, "change": -2.34, "percentChange": -7.74},
            {"symbol": "DDD", "name": "DDD Electronics", "price": 67.54, "change": -4.87, "percentChange": -6.73},
            {"symbol": "EEE", "name": "EEE Medical", "price": 89.32, "change": -5.43, "percentChange": -5.73},
            {"symbol": "FFF", "name": "FFF Retail", "price": 45.67, "change": -2.34, "percentChange": -4.87},
            {"symbol": "GGG", "name": "GGG Financial", "price": 123.45, "change": -5.67, "percentChange": -4.39},
            {"symbol": "HHH", "name": "HHH Motors", "price": 56.78, "change": -2.31, "percentChange": -3.91}
        ]
        
        return {
            "gainers": gainers[:limit],
            "losers": losers[:limit],
            "timestamp": "2025-03-12 05:55:29",  # Using the provided timestamp
            "updatedBy": "lucifer0177continue"   # Using the provided username
        }
    
    def get_most_watched(self, limit=5):
        """Get most watched/popular stocks"""
        # This would typically be based on user activity data
        # For now, return mock data
        watched = [
            {"symbol": "AAPL", "name": "Apple Inc.", "price": 243.56, "change": 3.21, "percentChange": 1.34},
            {"symbol": "MSFT", "name": "Microsoft Corp.", "price": 415.67, "change": 5.67, "percentChange": 1.38},
            {"symbol": "GOOGL", "name": "Alphabet Inc.", "price": 187.32, "change": -1.23, "percentChange": -0.65},
            {"symbol": "AMZN", "name": "Amazon.com Inc.", "price": 192.45, "change": 2.34, "percentChange": 1.23},
            {"symbol": "TSLA", "name": "Tesla Inc.", "price": 267.89, "change": -3.45, "percentChange": -1.27},
            {"symbol": "NVDA", "name": "NVIDIA Corp.", "price": 1245.67, "change": 75.34, "percentChange": 6.43},
            {"symbol": "META", "name": "Meta Platforms Inc.", "price": 532.78, "change": 7.89, "percentChange": 1.50},
            {"symbol": "JPM", "name": "JPMorgan Chase & Co.", "price": 210.45, "change": 1.23, "percentChange": 0.59}
        ]
        
        return {
            "stocks": watched[:limit],
            "timestamp": "2025-03-12 05:57:26",  # Using the updated timestamp
            "updatedBy": "lucifer0177continue"
        }