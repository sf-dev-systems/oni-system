# ONI System Frontend

React + Vite + TailwindCSS frontend for the ONI System backend.

## Features

- Clean, minimal dark mode UI
- Call backend endpoints:
  - `/minimal/ingest` - Process text through minimal pipeline
  - `/pipeline/run` - Run full pipeline (Chrono → VERA → Oni)
  - `/test/ping` - Test endpoint
  - `/health` - Health check
- Display JSON responses in readable, collapsible sections
- Real-time loading states and error handling

## Setup

### 1. Install dependencies

```bash
cd frontend
npm install
```

### 2. Configure backend URL

Edit `.env` file and set your backend URL (ngrok or localhost):

```env
VITE_API_URL=https://your-ngrok-url.ngrok.io
```

Or for local development:

```env
VITE_API_URL=http://localhost:8000
```

### 3. Run development server

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   └── ResultsPanel.jsx      # Displays API responses
│   ├── services/
│   │   └── api.js                # API service layer
│   ├── App.jsx                   # Main application component
│   ├── index.css                 # TailwindCSS styles
│   └── main.jsx                  # Application entry point
├── .env                          # Environment configuration
├── tailwind.config.js            # TailwindCSS configuration
└── vite.config.js                # Vite configuration
```

## Usage

1. Select an endpoint from the dropdown
2. Enter text (if required by the endpoint)
3. Click "Send" to call the backend
4. View the response in the results panel
5. Click on section headers to expand/collapse JSON data

## Development

### Build for production

```bash
npm run build
```

### Preview production build

```bash
npm run preview
```

## Notes

- The frontend uses TailwindCSS for styling with a dark theme
- All API calls go through the centralized `api.js` service
- CORS must be configured on the backend to allow frontend requests
- The results panel automatically formats responses with `event_packet`, `qa_packet`, and `storage_record` sections
