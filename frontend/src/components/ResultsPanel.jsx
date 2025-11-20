import { useState } from 'react';

export function ResultsPanel({ results, error, loading }) {
  const [expandedSections, setExpandedSections] = useState({
    event_packet: true,
    qa_packet: true,
    storage_record: true,
  });

  const toggleSection = (section) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  if (loading) {
    return (
      <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
        <div className="flex items-center justify-center space-x-3">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
          <p className="text-gray-300">Processing...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-900/20 rounded-lg p-6 border border-red-700">
        <h3 className="text-red-400 font-semibold mb-2 flex items-center">
          <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
          </svg>
          Error
        </h3>
        <p className="text-red-300">{error}</p>
      </div>
    );
  }

  if (!results) {
    return (
      <div className="bg-gray-800 rounded-lg p-6 border border-gray-700 text-center">
        <p className="text-gray-400">No results yet. Enter text and select an endpoint to get started.</p>
      </div>
    );
  }

  const renderSection = (title, data, key) => {
    if (!data) return null;

    const isExpanded = expandedSections[key];

    return (
      <div className="mb-4 last:mb-0">
        <button
          onClick={() => toggleSection(key)}
          className="w-full flex items-center justify-between p-3 bg-gray-700 hover:bg-gray-650 rounded-lg transition-colors"
        >
          <h4 className="font-semibold text-blue-400">{title}</h4>
          <svg
            className={`w-5 h-5 transform transition-transform ${isExpanded ? 'rotate-180' : ''}`}
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path fillRule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" />
          </svg>
        </button>
        {isExpanded && (
          <div className="mt-2 p-4 bg-gray-750 rounded-lg">
            <pre className="text-sm text-gray-300 overflow-x-auto whitespace-pre-wrap break-words">
              {JSON.stringify(data, null, 2)}
            </pre>
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
      <h3 className="text-xl font-bold mb-4 text-gray-100">Results</h3>

      {results.event_packet && renderSection('Event Packet', results.event_packet, 'event_packet')}
      {results.qa_packet && renderSection('QA Packet', results.qa_packet, 'qa_packet')}
      {results.storage_record && renderSection('Storage Record', results.storage_record, 'storage_record')}

      {/* For responses that don't have the standard structure, show raw JSON */}
      {!results.event_packet && !results.qa_packet && !results.storage_record && (
        <div className="p-4 bg-gray-750 rounded-lg">
          <pre className="text-sm text-gray-300 overflow-x-auto whitespace-pre-wrap break-words">
            {JSON.stringify(results, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
