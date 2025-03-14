import numpy as np
from datetime import datetime

class PredictionModel:
    """Machine learning model for stock price prediction"""
    
    def __init__(self):
        """Initialize the model - in a real app, this would load trained models"""
        # This would typically load pre-trained models
        pass
    
    def predict(self, symbol, timeframe='3m'):
        """Make a prediction for a specific stock and timeframe"""
        # In a real app, this would run actual ML inference
        # For now, generate mock prediction data
        
        # Use the symbol to create a deterministic but seemingly random prediction
        # This ensures the same symbol always gets the same prediction
        symbol_seed = sum(ord(c) for c in symbol)
        np.random.seed(symbol_seed)
        
        # Get a base price - would come from API in real app
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
            base_price = np.random.randint(50, 500) + np.random.random()
        
        # Generate a prediction with tendency toward positive (for demo purposes)
        percent_change = np.random.normal(8, 4)  # Mean 8% with 4% standard deviation
        predicted_price = base_price * (1 + percent_change/100)
        
        # Determine confidence level (60-95%)
        confidence = int(np.random.uniform(60, 95))
        
        # Determine recommendation based on percent change and confidence
        if percent_change > 10 and confidence > 75:
            recommendation = "STRONG BUY"
        elif percent_change > 5:
            recommendation = "BUY"
        elif percent_change > 0:
            recommendation = "HOLD"
        elif percent_change > -5:
            recommendation = "WATCH"
        else:
            recommendation = "SELL"
        
        # Generate contributing factors
        factors = []
        
        # Technical Analysis
        technical_weight = np.random.randint(25, 40)
        if percent_change > 0:
            technical_impact = "positive" if np.random.random() > 0.2 else "neutral"
            technical_desc = "Bullish patterns on multiple timeframes" if technical_impact == "positive" else "Mixed technical signals with moderate upside potential"
        else:
            technical_impact = "negative" if np.random.random() > 0.2 else "neutral"
            technical_desc = "Bearish patterns indicating downward momentum" if technical_impact == "negative" else "Mixed technical signals with cautious outlook"
            
        factors.append({
            "name": "Technical Analysis",
            "impact": technical_impact,
            "weight": technical_weight,
            "description": technical_desc
        })
        
        # Fundamental Analysis
        fundamental_weight = np.random.randint(20, 35)
        remaining_weight = 100 - technical_weight - fundamental_weight
        
        if percent_change > 0:
            fundamental_impact = "positive" if np.random.random() > 0.3 else "neutral"
            fundamental_desc = "Strong earnings growth and healthy balance sheet" if fundamental_impact == "positive" else "Steady financial performance with average growth metrics"
        else:
            fundamental_impact = "negative" if np.random.random() > 0.3 else "neutral"
            fundamental_desc = "Declining revenue growth and margin pressure" if fundamental_impact == "negative" else "Stable financials but facing industry headwinds"
            
        factors.append({
            "name": "Fundamental Analysis",
            "impact": fundamental_impact,
            "weight": fundamental_weight,
            "description": fundamental_desc
        })
        
        # Market Sentiment
        sentiment_weight = np.random.randint(15, 25)
        remaining_weight -= sentiment_weight
        
        if percent_change > 0:
            sentiment_impact = "positive" if np.random.random() > 0.25 else "neutral"
            sentiment_desc = "Positive news and social media sentiment" if sentiment_impact == "positive" else "Mixed media coverage with neutral social sentiment"
        else:
            sentiment_impact = "negative" if np.random.random() > 0.25 else "neutral"
            sentiment_desc = "Negative news cycle and bearish social indicators" if sentiment_impact == "negative" else "Limited media coverage with neutral sentiment"
            
        factors.append({
            "name": "Market Sentiment",
            "impact": sentiment_impact,
            "weight": sentiment_weight,
            "description": sentiment_desc
        })
        
        # Sector Performance
        sector_impact = np.random.choice(["positive", "neutral", "negative"], p=[0.4, 0.4, 0.2])
        if sector_impact == "positive":
            sector_desc = "Sector outperforming the broader market"
        elif sector_impact == "neutral":
            sector_desc = "Sector showing mixed signals"
        else:
            sector_desc = "Sector underperforming broader market"
            
        factors.append({
            "name": "Sector Performance",
            "impact": sector_impact,
            "weight": remaining_weight,
            "description": sector_desc
        })
        
        return {
            "symbol": symbol,
            "currentPrice": base_price,
            "predictedPrice": round(predicted_price, 2),
            "percentChange": round(percent_change, 2),
            "confidence": confidence,
            "timeframe": timeframe,
            "recommendation": recommendation,
            "factors": factors,
            "generatedAt": "2025-03-12 05:57:26",  # Using the provided timestamp
            "generatedBy": "lucifer0177continue"    # Using the provided username
        }