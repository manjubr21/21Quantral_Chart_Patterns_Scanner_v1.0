# 21Quantral Chart Patterns Scanner v1.0

> **Professional AI-Powered Chart Pattern Detection & Market Scanning Platform for the Indian Stock Market**

---

## Version

**Version:** 1.0.0

**Status:** Development

**Author:** Manjunatha Ramachandra & ChatGPT

---

# Vision

21Quantral Chart Patterns Scanner is a professional-grade Python application designed to scan the entire NSE stock universe and identify high-probability technical chart patterns across multiple timeframes.

The objective is not merely to detect chart patterns but to build a complete market intelligence platform capable of:

- Detecting chart patterns
- Ranking opportunities
- Multi-timeframe analysis
- Historical pattern database
- Performance analytics
- Automated alerts
- Professional dashboard
- Strategy backtesting

The project is intentionally designed with a modular architecture so new scanners, indicators and strategies can be added without modifying the core application.

---

# Primary Objectives

- Scan every NSE listed stock
- Detect multiple chart patterns
- Multi-timeframe analysis
- Timestamp every signal
- Rank opportunities
- Historical signal database
- Pattern performance analysis
- Dashboard visualization
- Strategy backtesting
- Professional logging
- Highly extensible plugin architecture

---

# Planned Features

## Data Sources

- Yahoo Finance (Free)
- mStock API
- NSE Bhavcopy
- Future data providers

---

## Timeframes

- 15 Minute
- 30 Minute
- Hourly
- Daily
- Weekly
- Monthly

---

## Indicators

- EMA
- SMA
- RSI
- ATR
- ADX
- MACD
- Bollinger Bands
- Supertrend
- Relative Strength
- Volume Analysis

---

## Chart Patterns

### Continuation

- Volatility Contraction Pattern (VCP)
- Flag & Pole
- Pennant
- Rectangle
- Ascending Triangle
- Descending Triangle
- Symmetrical Triangle
- Channel

### Reversal

- Cup & Handle
- Reverse Head & Shoulders
- Double Bottom
- Double Top
- Rounded Bottom
- Falling Wedge
- Rising Wedge

---

## Scanner Features

- Whole NSE scanning
- Multi-threaded processing
- Confidence scoring
- Signal ranking
- Historical logging
- Timestamp generation
- Watchlist scanning
- Sector scanning

---

## Dashboard

Planned using Streamlit.

Features include:

- Live Scanner
- Pattern Filters
- Charts
- Watchlists
- Historical Signals
- Pattern Statistics
- Portfolio View
- Settings

---

## Alerts

- Telegram
- Email
- Desktop Notification
- WhatsApp (future)
- Google Sheets (future)

---

# Project Architecture

```
21Quantral/
│
├── src/
│   ├── alerts/
│   ├── backtesting/
│   ├── config/
│   ├── core/
│   ├── dashboard/
│   ├── data/
│   ├── database/
│   ├── indicators/
│   ├── patterns/
│   ├── plugins/
│   ├── ranking/
│   ├── reports/
│   ├── scanners/
│   └── utils/
│
├── tests/
├── docs/
├── logs/
├── exports/
├── scripts/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# Development Principles

The project follows these engineering principles:

- Modular Architecture
- Object-Oriented Design
- Type Hinting
- SOLID Principles
- Plugin-based Pattern Detection
- Centralized Configuration
- Comprehensive Logging
- Unit Testing
- Clean Code
- Maintainability
- Scalability

---

# Plugin Philosophy

Every chart pattern will be implemented as an independent module.

Example:

```
patterns/

vcp.py
flag.py
cup_handle.py
double_bottom.py
triangle.py
```

The scanner engine should automatically discover available pattern modules without requiring modifications to the scanner itself.

---

# Planned Development Roadmap

## Phase 1

Foundation

- Project structure
- Logging
- Configuration
- Database
- Yahoo Finance integration
- Symbol loader

---

## Phase 2

Indicator Engine

- EMA
- RSI
- ATR
- ADX
- MACD
- Supertrend

---

## Phase 3

Pattern Engine

- VCP
- Flag
- Cup & Handle
- Reverse Head & Shoulders
- Double Bottom
- Double Top
- Triangle
- Rectangle

---

## Phase 4

Market Scanner

- Whole NSE
- Multi-timeframe
- Ranking Engine
- Confidence Score

---

## Phase 5

Alerts

- Telegram
- Email
- Dashboard
- Reports

---

## Phase 6

Backtesting

- Historical database
- Performance statistics
- Pattern analytics

---

# Coding Standards

- Python 3.12+
- PEP 8 compliant
- Ruff for linting
- Black for formatting
- Type hints throughout
- Docstrings for all public classes and methods
- Logging instead of print statements
- Configuration-driven behavior

---

# Current Version

```
Version : 1.0.0

Status  : Under Development

Completed

☑ README

☐ Requirements

☐ Project Structure

☐ Logging

☐ Database

☐ Yahoo Finance Engine

☐ Symbol Loader

☐ Indicators

☐ Pattern Engine

☐ Scanner

☐ Dashboard

☐ Alerts

☐ Reports

☐ Backtesting
```

---

# Disclaimer

This software is intended solely for educational and research purposes.

Users are responsible for validating all generated signals before placing trades.

No guarantee of profitability is implied.

---

# Acknowledgements

Development by:

**Manjunatha Ramachandra**

with the assistance of

**OpenAI ChatGPT**

---

## 21Quantral

**Scan. Analyze. Rank. Trade.**