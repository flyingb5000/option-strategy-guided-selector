# 期权策略引导选择器 / Option Strategy Guided Selector

这是一个交互式的期权策略选择工具，帮助投资者根据对美股标的的市场观点选择合适的期权策略。

This is an interactive option strategy selection tool that helps investors choose appropriate option strategies based on their market views of US stock targets.

## 功能特点 / Features

- 通过简单的问答引导用户明确自己的市场观点
- 根据用户对市场方向、价格变动幅度、波动率预期等因素的看法推荐策略
- 提供详细的策略说明，包括风险水平、盈利潜力、适用场景等信息
- 美观直观的用户界面，易于操作
- 支持中英文双语界面，可随时切换

- Guide users to clarify their market views through simple Q&A
- Recommend strategies based on user's views on market direction, price movement magnitude, volatility expectations, etc.
- Provide detailed strategy descriptions, including risk level, profit potential, applicable scenarios, etc.
- Beautiful and intuitive user interface, easy to operate
- Support bilingual interface in Chinese and English, switchable at any time

## 包含的期权策略 / Included Option Strategies

- **看涨策略**：买入看涨期权、牛市价差、卖出看跌期权、保护性看涨期权等
- **看跌策略**：买入看跌期权、熊市价差、卖出看涨期权、保护性看跌期权等
- **中性策略**：跨式组合、宽跨式组合、蝶式价差、铁鹰等
- **波动率策略**：买入/卖出跨式组合、日历价差等

- **Bullish Strategies**: Long Call, Bull Call Spread, Short Put, Covered Call, etc.
- **Bearish Strategies**: Long Put, Bear Put Spread, Short Call, Protective Put, etc.
- **Neutral Strategies**: Straddle, Strangle, Butterfly Spread, Iron Condor, etc.
- **Volatility Strategies**: Long/Short Straddle/Strangle, Calendar Spread, etc.

## 使用方法 / How to Use

1. 确保已安装Python 3.6或更高版本
2. 安装必要的依赖：`pip install tkinter`（大多数Python安装已包含tkinter）
3. 运行主程序：`python main.py`
4. 在界面中输入美股标的代码（默认为NVDA）
5. 回答关于市场观点的问题
6. 查看推荐的期权策略
7. 可随时点击界面右上角的"EN/中"按钮切换语言

1. Ensure Python 3.6 or higher is installed
2. Install necessary dependencies: `pip install tkinter` (most Python installations already include tkinter)
3. Run the main program: `python main.py`
4. Enter the US stock symbol in the interface (default is NVDA)
5. Answer questions about your market view
6. View recommended option strategies
7. Click the "EN/中" button in the upper right corner to switch languages at any time

## 文件说明 / File Description

- `main.py` - 主程序和用户界面 / Main program and user interface
- `strategy_selector.py` - 策略选择逻辑 / Strategy selection logic
- `期权策略1.png` 和 `option strategy cheat sheet.jpeg` - 期权策略参考图 / Option strategy reference images

## 注意事项 / Disclaimer

本工具仅供教育和参考目的使用，不构成投资建议。在实际交易中，请结合自身风险承受能力和市场情况做出决策。

This tool is for educational and reference purposes only and does not constitute investment advice. In actual trading, please make decisions based on your own risk tolerance and market conditions.