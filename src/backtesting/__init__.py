"""Backtesting utilities for Agent.

Modules:
- strategies: Trading strategy classes for Backtrader
- engine: Cerebro setup and run helpers
- data: Loading signals/market data for backtests
- plotting: Chart generation helpers
- reporting: Markdown report generation
"""

from .engine import DEFAULT_CASH, DEFAULT_COMMISSION, create_cerebro, run_backtest
from .strategies import AgentStrategy, BuyAndHoldStrategy

__all__ = [
    "DEFAULT_CASH",
    "DEFAULT_COMMISSION",
    "create_cerebro",
    "run_backtest",
    "AgentStrategy",
    "BuyAndHoldStrategy",
]

