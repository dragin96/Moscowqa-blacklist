# User Blacklist Service with Hexagonal Architecture

This project implements a user blacklist service using the Hexagonal Architecture pattern. It combines FastAPI for the REST API and aiogram for Telegram bot integration. The service is designed to be modular and extensible.

## Requirements
- Python 3.8+

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/user-blacklist-service.git
   cd user-blacklist-service
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://user:password@localhost/blacklist
   TELEGRAM_API_TOKEN=your_telegram_bot_token_here
   ```

5. **Run database migrations**:
   Make sure PostgreSQL is running, then apply migrations if needed (or create the necessary tables as defined in `SQLAlchemy` models).

6. **Start the application**:
   ```bash
   python main.py
   ```