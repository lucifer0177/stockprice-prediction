import numpy as np
import pandas as pd
from datetime import datetime

class ModelExplainer:
    """Explainable AI component for making model predictions interpretable"""
    
    def __init__(self, model):
        self.model = model
    
    def explain_prediction(self, symbol, prediction_data):
        """Generate human-readable explanations for a prediction"""
        # In a real app, this would use techniques like SHAP, LIME, etc.
        # For now, create explanations from the mock prediction data
        
        factors = prediction_data.get('factors', [])
        
        # Generate overall explanation
        overall_sentiment = "bullish" if prediction_data['percentChange'] > 0 else "bearish"
        timeframe = prediction_data['timeframe']
        confidence = prediction_data['confidence']
        
        explanation = {
            "summary": f"The model has a {overall_sentiment} outlook for {symbol} over the next {timeframe} with {confidence}% confidence.",
            "factors": {},
            "interpretation": [],
            "caveats": [
                "This prediction is based on historical patterns and may not account for unexpected events.",
                "Past performance is not indicative of future results.",
                "The model works best in stable market conditions and may be less accurate during high volatility."
            ],
            "methodology": {
                "description": "This prediction uses a hybrid model combining technical analysis, fundamental metrics, and market sentiment.",
                "features": [
                    "Historical price patterns and technical indicators",
                    "Financial metrics and company fundamentals",
                    "News sentiment and social media analysis",
                    "Market sector performance and macroeconomic factors"
                ]
            },
            "timestamp": "2025-03-12 05:57:26",  # Using the provided timestamp
            "analyst": "lucifer0177continue"     # Using the provided username
        }
        
        # Process each factor
        for factor in factors:
            factor_name = factor['name']
            impact = factor['impact']
            weight = factor['weight']
            description = factor['description']
            
            explanation['factors'][factor_name] = {
                "impact": impact,
                "weight": weight,
                "description": description,
                "interpretation": self._generate_interpretation(factor_name, impact, weight, description)
            }
            
            # Add to overall interpretation list
            explanation['interpretation'].append({
                "factor": factor_name,
                "explanation": self._generate_interpretation(factor_name, impact, weight, description)
            })
        
        return explanation
    
    def _generate_interpretation(self, factor_name, impact, weight, description):
        """Generate interpretation text for a specific factor"""
        if factor_name == "Technical Analysis":
            if impact == "positive":
                return f"Technical indicators suggest a bullish trend with {weight}% influence on the prediction. {description}."
            elif impact == "negative":
                return f"Technical indicators suggest a bearish trend with {weight}% influence on the prediction. {description}."
            else:
                return f"Technical indicators are showing mixed signals with {weight}% influence on the prediction. {description}."
        
        elif factor_name == "Fundamental Analysis":
            if impact == "positive":
                return f"Company fundamentals appear strong with {weight}% influence on the prediction. {description}."
            elif impact == "negative":
                return f"Company fundamentals show concerns with {weight}% influence on the prediction. {description}."
            else:
                return f"Company fundamentals are stable but mixed with {weight}% influence on the prediction. {description}."
        
        elif factor_name == "Market Sentiment":
            if impact == "positive":
                return f"Market sentiment is favorable with {weight}% influence on the prediction. {description}."
            elif impact == "negative":
                return f"Market sentiment is unfavorable with {weight}% influence on the prediction. {description}."
            else:
                return f"Market sentiment is neutral with {weight}% influence on the prediction. {description}."
        
        elif factor_name == "Sector Performance":
            if impact == "positive":
                return f"The sector is performing well with {weight}% influence on the prediction. {description}."
            elif impact == "negative":
                return f"The sector is underperforming with {weight}% influence on the prediction. {description}."
            else:
                return f"The sector is showing average performance with {weight}% influence on the prediction. {description}."
        
        else:
            return f"{factor_name} has a {impact} impact with {weight}% influence on the prediction. {description}."