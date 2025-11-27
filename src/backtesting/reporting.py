from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, Any


def generate_markdown_report(all_results: Dict[str, Dict[str, Any]], report_path: Path) -> None:
    """Generate a markdown report with a metrics table for each stock/strategy."""
    lines = []
    lines.append("# Agent Multi-Stock Backtest Results")
    lines.append(f"\n*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

    lines.append("\n## Performance Metrics")
    lines.append("\n| Stock | Strategy | Final Value | Return % | Volatility % | Sharpe | Max DD % | Trades |")
    lines.append("|-------|----------|-------------|----------|--------------|--------|----------|--------|")

    for symbol in sorted(all_results.keys()):
        agent = all_results[symbol]["agent"]
        buyhold = all_results[symbol]["buyhold"]
        lines.append(
            f"| {symbol} | Agent | ${agent['Final Value']:,.0f} | {agent['Cumulative Return [%]']:+.2f}% | "
            f"{agent['Annual Volatility [%]']:.2f}% | {agent['Sharpe Ratio']:.3f} | {agent['Max Drawdown [%]']:.2f}% | {agent['Total Trades']} |"
        )
        lines.append(
            f"| {symbol} | Buy & Hold | ${buyhold['Final Value']:,.0f} | {buyhold['Cumulative Return [%]']:+.2f}% | "
            f"{buyhold['Annual Volatility [%]']:.2f}% | {buyhold['Sharpe Ratio']:.3f} | {buyhold['Max Drawdown [%]']:.2f}% | {buyhold['Total Trades']} |"
        )
        lines.append("| | | | | | | | |")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")

