const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = {
  /**
   * Call the /test/ping endpoint
   */
  async ping() {
    const response = await fetch(`${API_URL}/test/ping`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  },

  /**
   * Call the /health endpoint
   */
  async health() {
    const response = await fetch(`${API_URL}/health`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  },

  /**
   * Call the /minimal/ingest endpoint
   * @param {string} text - The text to ingest
   */
  async minimalIngest(text) {
    const response = await fetch(`${API_URL}/minimal/ingest`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  },

  /**
   * Call the /pipeline/run endpoint
   * @param {string} text - The text to process
   */
  async pipelineRun(text) {
    const response = await fetch(`${API_URL}/pipeline/run`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  },
};
