# Currency Exchange Tracker

A lightweight tool for tracking currency exchange rates and visualizing currency movements over time. Use it to fetch up-to-date exchange rates, compare currencies, and monitor changes so you can make informed decisions.

> Simple, clear, and extendable — suitable as a learning project, demo, or as the foundation for a production dashboard.

## Features
- Fetches live currency exchange rates from a configurable provider (e.g. ExchangeRate API, Fixer, OpenExchangeRates).
- Compare a base currency to one or many target currencies.
- Historical lookup (if supported by the chosen API) and simple trend visualization.
- Configurable polling to refresh rates automatically.
- Clean, minimal UI and/or API-first design so it can be integrated into other systems.

## Built with
This repository is intentionally implementation-agnostic. Typical stacks that work well:
- Frontend: React / Vue / Svelte (optional)
- Backend / API: Node.js (Express) or Python (Flask/FastAPI)
- Data source: Public exchange-rate APIs (requires an API key for most providers)

Replace the placeholders below with the actual stack used in this repository.

## Quickstart (Local Development)
These instructions assume the repo uses Node.js for the server and a JS frontend. Adjust commands to match your project's stack.

1. Clone the repo
   ```bash
   git clone https://github.com/AayushBadoni18/Currency-Exchange-Tracker.git
   cd Currency-Exchange-Tracker
   ```

2. Install dependencies
   - For Node.js (backend)
     ```bash
     cd server
     npm install
     ```
   - For frontend (if present)
     ```bash
     cd ../client
     npm install
     ```

3. Create a .env file
   Copy the example env and fill in your API credentials and configuration:
   ```bash
   cp .env.example .env
   ```
   Example environment variables:
   ```
   EXCHANGE_API_KEY=your_api_key_here
   EXCHANGE_API_URL=https://api.exchangerate.host
   BASE_CURRENCY=USD
   PORT=3000
   POLL_INTERVAL_SECONDS=300
   ```

4. Run the application
   - Start backend:
     ```bash
     cd server
     npm start
     ```
   - Start frontend (if present):
     ```bash
     cd ../client
     npm start
     ```

5. Open the app
   Visit http://localhost:3000 (or your configured PORT) in your browser.

If your project uses Python, use:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export EXCHANGE_API_KEY=your_api_key_here
python app.py
```

## Configuration
- EXCHANGE_API_URL: Base URL of the exchange rate provider.
- EXCHANGE_API_KEY: API key for the provider (if required).
- BASE_CURRENCY: The default currency to compare others against (e.g., USD).
- POLL_INTERVAL_SECONDS: How often to refresh rates (in seconds).

Check the project's configuration file or `.env.example` for exact variable names and additional options.

## Usage
- Use the UI to select a base currency and targets to compare.
- Use the API endpoints (if available) to fetch current rates:
  - GET /api/rates?base=USD&symbols=EUR,GBP
  - GET /api/rates/history?base=USD&symbols=EUR&start=2025-01-01&end=2025-01-10

Adjust endpoint paths to match the actual implementation in this repository.

## Testing
- Unit tests (if any): run `npm test` or `pytest` depending on the stack.
- Linting: `npm run lint` or `flake8` as configured.

## Deployment
- Build frontend (if present): `npm run build` (in `client`).
- Host backend on your platform of choice (Heroku, Vercel [serverless], Render, DigitalOcean).
- Ensure environment variables, secrets and API keys are configured on the host.

## Extending / Ideas
- Add user accounts and watchlists.
- Push notifications when a currency crosses a threshold.
- More advanced charting and analytics (rolling averages, volatility indicators).
- Caching layer to minimize API calls and reduce costs.
- Support multiple providers with automatic failover.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to your branch and open a Pull Request

Please include tests and update documentation where appropriate.

## License
This project is provided under the MIT License. See the LICENSE file for details.

## Contact
Maintainer: AayushBadoni18  
If you have questions or suggestions, open an issue or submit a pull request.
