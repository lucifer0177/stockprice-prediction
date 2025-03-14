import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { LightningBoltIcon, ArrowSmUpIcon } from '@heroicons/react/solid';

const StockPrediction = ({ prediction }) => {
  // Prepare chart data for confidence display
  const confidenceChartData = {
    labels: ['Confidence', 'Uncertainty'],
    datasets: [
      {
        data: [prediction.confidence, 100 - prediction.confidence],
        backgroundColor: ['#3b82f6', '#e5e7eb'],
        borderWidth: 0,
        cutout: '70%'
      }
    ]
  };
  
  const confidenceOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        enabled: false
      }
    }
  };
  
  // Generate colors based on impact
  const getImpactColor = (impact) => {
    switch(impact) {
      case 'positive':
        return 'bg-green-100 dark:bg-green-800/30 text-green-800 dark:text-green-300';
      case 'negative':
        return 'bg-red-100 dark:bg-red-800/30 text-red-800 dark:text-red-300';
      case 'neutral':
      default:
        return 'bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-300';
    }
  };
  
  return (
    <div className="space-y-6">
      <div className="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4 flex items-start">
        <LightningBoltIcon className="h-6 w-6 text-blue-500 dark:text-blue-400 mr-3" />
        <div>
          <h3 className="text-lg font-medium text-gray-900 dark:text-white">AI Price Prediction</h3>
          <p className="mt-1 text-sm text-gray-600 dark:text-gray-300">
            StockPredictAI uses machine learning and XAI techniques to analyze market patterns, fundamentals, and sentiment to forecast stock prices. This prediction is for informational purposes only and should not be the sole basis for any investment decision.
          </p>
        </div>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="col-span-2 bg-white dark:bg-gray-800 rounded-lg shadow p-4">
          <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">Prediction Explanation</h3>
          
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500 dark:text-gray-400">Current Price</p>
                <p className="text-xl font-bold text-gray-900 dark:text-white">${prediction.currentPrice.toFixed(2)}</p>
              </div>
              <div className="text-2xl font-bold text-gray-400 dark:text-gray-500">→</div>
              <div className="text-right">
                <p className="text-sm text-gray-500 dark:text-gray-400">Predicted Price ({prediction.timeframe})</p>
                <div className="flex items-center justify-end">
                  <p className="text-xl font-bold text-blue-600 dark:text-blue-400">${prediction.predictedPrice.toFixed(2)}</p>
                  <div className="flex items-center ml-2 text-sm text-green-600">
                    <ArrowSmUpIcon className="h-4 w-4 mr-1" />
                    <span>+{prediction.percentChange.toFixed(2)}%</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div>
              <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">Factors Influencing Prediction</h4>
              <div className="space-y-3">
                {prediction.factors.map((factor, index) => (
                  <div key={index} className="bg-gray-50 dark:bg-gray-700/50 rounded-md p-3">
                    <div className="flex justify-between items-center mb-1">
                      <div className="flex items-center">
                        <span className="text-sm font-medium text-gray-900 dark:text-white">{factor.name}</span>
                        <span className={`ml-2 px-2 py-0.5 text-xs rounded-full ${getImpactColor(factor.impact)}`}>
                          {factor.impact.charAt(0).toUpperCase() + factor.impact.slice(1)}
                        </span>
                      </div>
                      <span className="text-xs text-gray-500 dark:text-gray-400">Weight: {factor.weight}%</span>
                    </div>
                    <p className="text-xs text-gray-600 dark:text-gray-300">{factor.description}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4 flex flex-col items-center">
          <h3 className="text-lg font-medium text-gray-900 dark:text-white self-start mb-4">Confidence Level</h3>
          
          <div className="relative w-44 h-44">
            <Doughnut data={confidenceChartData} options={confidenceOptions} />
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="text-center">
                <div className="text-3xl font-bold text-gray-900 dark:text-white">{prediction.confidence}%</div>
                <div className="text-xs text-gray-500 dark:text-gray-400">Confidence</div>
              </div>
            </div>
          </div>
          
          <div className="mt-6 bg-blue-50 dark:bg-blue-900/20 p-3 rounded-md w-full">
            <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">Recommendation</h4>
            <div className="flex justify-center">
              <span className="px-4 py-1 text-sm font-semibold rounded-full bg-green-100 dark:bg-green-800/30 text-green-800 dark:text-green-300">
                {prediction.recommendation}
              </span>
            </div>
          </div>
          
          <div className="mt-4 text-center text-xs text-gray-500 dark:text-gray-400">
            <p>Last updated: 2025-03-12 05:53:48 UTC</p>
            <p className="mt-1">By user: lucifer0177continue</p>
          </div>
        </div>
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
        <h3 className="text-lg font-medium text-gray-900 dark:text-white mb-4">Understanding XAI in Stock Predictions</h3>
        
        <div className="space-y-4 text-sm text-gray-600 dark:text-gray-300">
          <p>
            Explainable AI (XAI) makes machine learning predictions transparent by revealing the factors that influenced the forecast. Unlike black-box models, our XAI system provides clear reasoning behind each prediction.
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
            <div className="bg-gray-50 dark:bg-gray-700/50 p-3 rounded-md">
              <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">Technical Analysis</h4>
              <p className="text-xs">Identifies patterns in price and volume data, evaluates momentum indicators, and analyzes support/resistance levels.</p>
            </div>
            <div className="bg-gray-50 dark:bg-gray-700/50 p-3 rounded-md">
              <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">Fundamental Analysis</h4>
              <p className="text-xs">Examines financial statements, earnings reports, P/E ratios, and compares metrics to industry benchmarks.</p>
            </div>
            <div className="bg-gray-50 dark:bg-gray-700/50 p-3 rounded-md">
              <h4 className="text-sm font-medium text-gray-900 dark:text-white mb-2">Sentiment Analysis</h4>
              <p className="text-xs">Processes news articles, social media, analyst reports, and market sentiment to gauge public perception.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StockPrediction;