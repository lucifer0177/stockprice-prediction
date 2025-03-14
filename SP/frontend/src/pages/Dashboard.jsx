import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import StockCard from '../components/stocks/StockCard';
import MarketSummary from '../components/dashboard/MarketSummary';
import TrendingStocks from '../components/dashboard/TrendingStocks';
import TopMovers from '../components/dashboard/TopMovers';
import PredictionHighlights from '../components/dashboard/PredictionHighlights';
import RecentNews from '../components/dashboard/RecentNews';

const Dashboard = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [marketData, setMarketData] = useState(null);

  // Mock market data loading (would be API call in real app)
  useEffect(() => {
    const fetchData = async () => {
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 800));
      
      // Mock data
      const data = {
        marketSummary: {
          indices: [
            { name: 'S&P 500', value: 5923.47, change: 47.88, percentChange: 0.81 },
            { name: 'Dow Jones', value: 40654.32, change: 315.56, percentChange: 0.78 },
            { name: 'Nasdaq', value: 18732.91, change: -24.53, percentChange: -0.13 },
            { name: 'Russell 2000', value: 2354.76, change: 12.34, percentChange: 0.53 }
          ],
          timestamp: "2025-03-12 05:45:36"
        },
        topGainers: [
          { symbol: 'XYZ', name: 'XYZ Corp', price: 134.21, change: 12.45, percentChange: 10.23 },
          { symbol: 'ABC', name: 'ABC Inc', price: 56.78, change: 4.32, percentChange: 8.24 },
          { symbol: 'DEF', name: 'DEF Holdings', price: 89.45, change: 5.67, percentChange: 6.77 }
        ],
        topLosers: [
          { symbol: 'MNO', name: 'MNO Industries', price: 42.63, change: -8.21, percentChange: -16.15 },
          { symbol: 'PQR', name: 'PQR Tech', price: 105.32, change: -12.45, percentChange: -10.57 },
          { symbol: 'STU', name: 'STU Systems', price: 27.89, change: -2.34, percentChange: -7.74 }
        ],
        mostWatched: [
          { symbol: 'AAPL', name: 'Apple Inc.', price: 243.56, change: 3.21, percentChange: 1.34 },
          { symbol: 'MSFT', name: 'Microsoft Corp.', price: 415.67, change: 5.67, percentChange: 1.38 },
          { symbol: 'GOOGL', name: 'Alphabet Inc.', price: 187.32, change: -1.23, percentChange: -0.65 },
          { symbol: 'AMZN', name: 'Amazon.com Inc.', price: 192.45, change: 2.34, percentChange: 1.23 },
          { symbol: 'TSLA', name: 'Tesla Inc.', price: 267.89, change: -3.45, percentChange: -1.27 }
        ],
        bestPerforming: {
          symbol: 'NVDA',
          name: 'NVIDIA Corporation',
          price: 1245.67,
          change: 75.34,
          percentChange: 6.43,
          prediction: {
            target: 1350,
            confidence: 87,
            timeframe: '3 months'
          }
        },
        topPredictions: [
          { 
            symbol: 'AAPL', 
            name: 'Apple Inc.', 
            currentPrice: 243.56, 
            predictedPrice: 275.00, 
            change: 31.44, 
            percentChange: 12.91,
            confidence: 85,
            recommendation: 'BUY'
          },
          { 
            symbol: 'META', 
            name: 'Meta Platforms Inc.', 
            currentPrice: 532.78, 
            predictedPrice: 595.50, 
            change: 62.72, 
            percentChange: 11.77,
            confidence: 79,
            recommendation: 'BUY'
          },
          { 
            symbol: 'AMD', 
            name: 'Advanced Micro Devices, Inc.', 
            currentPrice: 187.34, 
            predictedPrice: 208.10, 
            change: 20.76, 
            percentChange: 11.08,
            confidence: 76,
            recommendation: 'BUY'
          }
        ],
        recentNews: [
          {
            id: 1,
            title: 'Federal Reserve Signals Potential Rate Cuts in Coming Months',
            source: 'Financial Times',
            timestamp: '2025-03-12 04:15:22',
            url: '#',
            sentiment: 'positive'
          },
          {
            id: 2,
            title: 'Tech Sector Surges as AI Advancements Continue to Drive Growth',
            source: 'Bloomberg',
            timestamp: '2025-03-12 03:45:11',
            url: '#',
            sentiment: 'positive'
          },
          {
            id: 3,
            title: 'Global Supply Chain Issues Easing According to New Report',
            source: 'Reuters',
            timestamp: '2025-03-12 02:30:45',
            url: '#',
            sentiment: 'positive'
          },
          {
            id: 4,
            title: 'Energy Stocks Under Pressure as Oil Prices Fall',
            source: 'CNBC',
            timestamp: '2025-03-12 01:15:33',
            url: '#',
            sentiment: 'negative'
          }
        ]
      };
      
      setMarketData(data);
      setIsLoading(false);
    };
    
    fetchData();
  }, []);
  
  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4 text-gray-600 dark:text-gray-300">Loading market data...</p>
        </div>
      </div>
    );
  }
  
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Market Dashboard</h1>
      
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <div className="lg:col-span-3">
          <MarketSummary data={marketData.marketSummary} />
        </div>
        <div className="lg:col-span-1 space-y-6">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
            <h2 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Best Performer Today</h2>
            <StockCard stock={marketData.bestPerforming} showPrediction={true} />
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
            <h2 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Market Time</h2>
            <p className="text-gray-600 dark:text-gray-300">{marketData.marketSummary.timestamp} UTC</p>
            <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">Market status: <span className="text-green-500">Open</span></p>
          </div>
        </div>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
          <h2 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Top Gainers</h2>
          <TopMovers stocks={marketData.topGainers} type="gainers" />
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
          <h2 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Top Losers</h2>
          <TopMovers stocks={marketData.topLosers} type="losers" />
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
          <h2 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Most Watched</h2>
          <TrendingStocks stocks={marketData.mostWatched} />
        </div>
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <h2 className="text-lg font-semibold mb-4 text-gray-900 dark:text-white">Top AI Predictions</h2>
        <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">
          Price predictions for the next 3 months based on our XAI model with explanation capabilities.
        </p>
        <PredictionHighlights predictions={marketData.topPredictions} />
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white">Recent News</h2>
          <Link to="/news" className="text-blue-600 hover:text-blue-500 text-sm font-medium">
            View all
          </Link>
        </div>
        <RecentNews news={marketData.recentNews} />
      </div>
    </div>
  );
};

export default Dashboard;