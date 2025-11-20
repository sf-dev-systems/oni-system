import { useState } from 'react';
import { api } from './services/api';
import { ResultsPanel } from './components/ResultsPanel';

function App() {
  const [inputText, setInputText] = useState('');
  const [selectedEndpoint, setSelectedEndpoint] = useState('minimalIngest');
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const endpoints = [
    { value: 'minimalIngest', label: '/minimal/ingest', requiresText: true },
    { value: 'pipelineRun', label: '/pipeline/run', requiresText: true },
    { value: 'ping', label: '/test/ping', requiresText: false },
    { value: 'health', label: '/health', requiresText: false },
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResults(null);
    setLoading(true);

    try {
      const endpoint = endpoints.find(ep => ep.value === selectedEndpoint);

      if (endpoint.requiresText && !inputText.trim()) {
        throw new Error('Please enter some text');
      }

      let response;
      switch (selectedEndpoint) {
        case 'minimalIngest':
          response = await api.minimalIngest(inputText);
          break;
        case 'pipelineRun':
          response = await api.pipelineRun(inputText);
          break;
        case 'ping':
          response = await api.ping();
          break;
        case 'health':
          response = await api.health();
          break;
        default:
          throw new Error('Invalid endpoint selected');
      }

      setResults(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const currentEndpoint = endpoints.find(ep => ep.value === selectedEndpoint);

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-blue-400 mb-2">ONI System</h1>
          <p className="text-gray-400">FastAPI Backend Interface</p>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Input Panel */}
          <div className="bg-gray-800 rounded-lg p-6 border border-gray-700 h-fit">
            <h2 className="text-2xl font-semibold mb-4 text-gray-100">Input</h2>

            <form onSubmit={handleSubmit} className="space-y-4">
              {/* Endpoint Selection */}
              <div>
                <label htmlFor="endpoint" className="block text-sm font-medium text-gray-300 mb-2">
                  Select Endpoint
                </label>
                <select
                  id="endpoint"
                  value={selectedEndpoint}
                  onChange={(e) => setSelectedEndpoint(e.target.value)}
                  className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100"
                >
                  {endpoints.map(endpoint => (
                    <option key={endpoint.value} value={endpoint.value}>
                      {endpoint.label}
                    </option>
                  ))}
                </select>
              </div>

              {/* Text Input */}
              {currentEndpoint?.requiresText && (
                <div>
                  <label htmlFor="text-input" className="block text-sm font-medium text-gray-300 mb-2">
                    Input Text
                  </label>
                  <textarea
                    id="text-input"
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    placeholder="Enter text to process..."
                    rows={8}
                    className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100 placeholder-gray-500 resize-y"
                  />
                </div>
              )}

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className="w-full px-6 py-3 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-800"
              >
                {loading ? 'Processing...' : 'Send'}
              </button>
            </form>

            {/* API Info */}
            <div className="mt-6 pt-6 border-t border-gray-700">
              <p className="text-sm text-gray-400">
                <span className="font-semibold">Backend URL:</span>{' '}
                {import.meta.env.VITE_API_URL || 'http://localhost:8000'}
              </p>
            </div>
          </div>

          {/* Results Panel */}
          <div>
            <ResultsPanel results={results} error={error} loading={loading} />
          </div>
        </div>

        {/* Footer */}
        <div className="mt-12 text-center text-gray-500 text-sm">
          <p>ONI System • Chrono • VERA • Baymax • Dispatcher</p>
        </div>
      </div>
    </div>
  );
}

export default App;
