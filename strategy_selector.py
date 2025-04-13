# strategy_selector.py
# 期权策略选择器逻辑 / Option Strategy Selector Logic

class StrategySelector:
    def __init__(self, language='cn'):  # 默认使用中文
        # 设置语言，'cn'为中文，'en'为英文
        self.language = language
        # 初始化期权策略库
        self.strategies_cn = {
            # 看涨策略
            'bullish': [
                {
                    'name': '买入看涨期权 (Long Call)',
                    'description': '购买看涨期权合约，获得以特定价格买入标的资产的权利。',
                    'risk_level': '有限风险（最大损失为支付的期权费）',
                    'profit_potential': '无限',
                    'best_for': '预期标的资产价格大幅上涨',
                    'iv_preference': '低波动率更好（期权费更便宜）'
                },
                {
                    'name': '牛市价差 (Bull Call Spread)',
                    'description': '买入较低执行价的看涨期权，同时卖出较高执行价的看涨期权。',
                    'risk_level': '有限风险（最大损失为两个期权的净成本）',
                    'profit_potential': '有限（两个执行价之间的差额减去净成本）',
                    'best_for': '预期标的资产价格适度上涨',
                    'iv_preference': '中性'
                },
                {
                    'name': '卖出看跌期权 (Short Put)',
                    'description': '卖出看跌期权合约，承担以特定价格买入标的资产的义务。',
                    'risk_level': '高风险（最大损失接近标的资产全部价值）',
                    'profit_potential': '有限（收取的期权费）',
                    'best_for': '预期标的资产价格稳定或小幅上涨',
                    'iv_preference': '高波动率更好（收取更多期权费）'
                },
                {
                    'name': '保护性看涨期权 (Covered Call)',
                    'description': '持有标的资产的同时，卖出该资产的看涨期权。',
                    'risk_level': '中等风险（最大损失为标的资产价值减去收取的期权费）',
                    'profit_potential': '有限（收取的期权费加上可能的资产升值）',
                    'best_for': '预期标的资产价格稳定或小幅上涨',
                    'iv_preference': '高波动率更好（收取更多期权费）'
                }
            ],
            
            # 看跌策略
            'bearish': [
                {
                    'name': '买入看跌期权 (Long Put)',
                    'description': '购买看跌期权合约，获得以特定价格卖出标的资产的权利。',
                    'risk_level': '有限风险（最大损失为支付的期权费）',
                    'profit_potential': '很高（最大为执行价减去期权费）',
                    'best_for': '预期标的资产价格大幅下跌',
                    'iv_preference': '低波动率更好（期权费更便宜）'
                },
                {
                    'name': '熊市价差 (Bear Put Spread)',
                    'description': '买入较高执行价的看跌期权，同时卖出较低执行价的看跌期权。',
                    'risk_level': '有限风险（最大损失为两个期权的净成本）',
                    'profit_potential': '有限（两个执行价之间的差额减去净成本）',
                    'best_for': '预期标的资产价格适度下跌',
                    'iv_preference': '中性'
                },
                {
                    'name': '卖出看涨期权 (Short Call)',
                    'description': '卖出看涨期权合约，承担以特定价格卖出标的资产的义务。',
                    'risk_level': '无限风险（理论上标的资产价格可无限上涨）',
                    'profit_potential': '有限（收取的期权费）',
                    'best_for': '预期标的资产价格稳定或下跌',
                    'iv_preference': '高波动率更好（收取更多期权费）'
                },
                {
                    'name': '保护性看跌期权 (Protective Put)',
                    'description': '持有标的资产的同时，购买该资产的看跌期权作为保险。',
                    'risk_level': '有限风险（最大损失为支付的期权费加上资产可能的小幅贬值）',
                    'profit_potential': '无限（减去期权费的成本）',
                    'best_for': '希望对现有持仓进行保护，防范下跌风险',
                    'iv_preference': '低波动率更好（期权费更便宜）'
                }
            ],
            
            # 中性策略
            'neutral': [
                {
                    'name': '跨式组合 (Straddle)',
                    'description': '同时买入相同执行价格和到期日的看涨和看跌期权。',
                    'risk_level': '有限风险（最大损失为支付的总期权费）',
                    'profit_potential': '无限（标的资产价格大幅波动时）',
                    'best_for': '预期标的资产价格将大幅波动，但不确定方向',
                    'iv_preference': '低波动率买入更好（期权费更便宜）'
                },
                {
                    'name': '宽跨式组合 (Strangle)',
                    'description': '同时买入不同执行价格（看跌低于看涨）但相同到期日的看涨和看跌期权。',
                    'risk_level': '有限风险（最大损失为支付的总期权费）',
                    'profit_potential': '无限（标的资产价格大幅波动时）',
                    'best_for': '预期标的资产价格将大幅波动，但不确定方向，且成本意识较强',
                    'iv_preference': '低波动率买入更好（期权费更便宜）'
                },
                {
                    'name': '蝶式价差 (Butterfly Spread)',
                    'description': '结合牛市和熊市价差策略，买入一个低执行价看涨期权，卖出两个中间执行价看涨期权，再买入一个高执行价看涨期权。',
                    'risk_level': '有限风险（最大损失为净期权费）',
                    'profit_potential': '有限（最大利润在中间执行价时）',
                    'best_for': '预期标的资产价格将在特定范围内波动',
                    'iv_preference': '低波动率更好'
                },
                {
                    'name': '铁鹰 (Iron Condor)',
                    'description': '卖出一个看跌价差和一个看涨价差，形成一个价格区间。',
                    'risk_level': '有限风险（最大损失为两个价差之间的差额减去净收入）',
                    'profit_potential': '有限（净收取的期权费）',
                    'best_for': '预期标的资产价格将在特定范围内波动',
                    'iv_preference': '高波动率卖出更好（收取更多期权费）'
                }
            ],
            
            # 波动率策略
            'volatility': [
                {
                    'name': '买入跨式/宽跨式 (Long Straddle/Strangle)',
                    'description': '同时买入看涨和看跌期权，押注波动率上升。',
                    'risk_level': '有限风险（最大损失为支付的总期权费）',
                    'profit_potential': '无限（标的资产价格大幅波动时）',
                    'best_for': '预期波动率将上升，价格将大幅波动',
                    'iv_preference': '当前波动率低，预期上升'
                },
                {
                    'name': '卖出跨式/宽跨式 (Short Straddle/Strangle)',
                    'description': '同时卖出看涨和看跌期权，押注波动率下降。',
                    'risk_level': '无限风险（标的资产价格大幅波动时）',
                    'profit_potential': '有限（收取的总期权费）',
                    'best_for': '预期波动率将下降，价格将在一定范围内波动',
                    'iv_preference': '当前波动率高，预期下降'
                },
                {
                    'name': '日历价差 (Calendar Spread)',
                    'description': '卖出近期期权，同时买入远期期权（相同执行价）。',
                    'risk_level': '有限风险（最大损失为净期权费）',
                    'profit_potential': '有限',
                    'best_for': '预期短期内波动较小，长期波动较大',
                    'iv_preference': '近期期权波动率高于远期期权'
                }
            ]
        }
        
        # 英文版期权策略库
        self.strategies_en = {
            # Bullish Strategies
            'bullish': [
                {
                    'name': 'Long Call',
                    'description': 'Purchase a call option contract, gaining the right to buy the underlying asset at a specific price.',
                    'risk_level': 'Limited risk (maximum loss is the premium paid)',
                    'profit_potential': 'Unlimited',
                    'best_for': 'Expecting significant upward price movement in the underlying asset',
                    'iv_preference': 'Lower volatility is better (cheaper premium)'
                },
                {
                    'name': 'Bull Call Spread',
                    'description': 'Buy a call option with a lower strike price and sell a call option with a higher strike price.',
                    'risk_level': 'Limited risk (maximum loss is the net cost of the two options)',
                    'profit_potential': 'Limited (difference between the two strike prices minus the net cost)',
                    'best_for': 'Expecting moderate upward price movement in the underlying asset',
                    'iv_preference': 'Neutral'
                },
                {
                    'name': 'Short Put',
                    'description': 'Sell a put option contract, taking on the obligation to buy the underlying asset at a specific price.',
                    'risk_level': 'High risk (maximum loss approaches the full value of the underlying asset)',
                    'profit_potential': 'Limited (the premium received)',
                    'best_for': 'Expecting stable or slightly rising prices in the underlying asset',
                    'iv_preference': 'Higher volatility is better (receive more premium)'
                },
                {
                    'name': 'Covered Call',
                    'description': 'Hold the underlying asset while selling a call option on that asset.',
                    'risk_level': 'Medium risk (maximum loss is the value of the underlying asset minus the premium received)',
                    'profit_potential': 'Limited (premium received plus potential asset appreciation)',
                    'best_for': 'Expecting stable or slightly rising prices in the underlying asset',
                    'iv_preference': 'Higher volatility is better (receive more premium)'
                }
            ],
            
            # Bearish Strategies
            'bearish': [
                {
                    'name': 'Long Put',
                    'description': 'Purchase a put option contract, gaining the right to sell the underlying asset at a specific price.',
                    'risk_level': 'Limited risk (maximum loss is the premium paid)',
                    'profit_potential': 'Very high (maximum is the strike price minus the premium)',
                    'best_for': 'Expecting significant downward price movement in the underlying asset',
                    'iv_preference': 'Lower volatility is better (cheaper premium)'
                },
                {
                    'name': 'Bear Put Spread',
                    'description': 'Buy a put option with a higher strike price and sell a put option with a lower strike price.',
                    'risk_level': 'Limited risk (maximum loss is the net cost of the two options)',
                    'profit_potential': 'Limited (difference between the two strike prices minus the net cost)',
                    'best_for': 'Expecting moderate downward price movement in the underlying asset',
                    'iv_preference': 'Neutral'
                },
                {
                    'name': 'Short Call',
                    'description': 'Sell a call option contract, taking on the obligation to sell the underlying asset at a specific price.',
                    'risk_level': 'Unlimited risk (theoretically, the price of the underlying asset can rise infinitely)',
                    'profit_potential': 'Limited (the premium received)',
                    'best_for': 'Expecting stable or falling prices in the underlying asset',
                    'iv_preference': 'Higher volatility is better (receive more premium)'
                },
                {
                    'name': 'Protective Put',
                    'description': 'Hold the underlying asset while purchasing a put option on that asset as insurance.',
                    'risk_level': 'Limited risk (maximum loss is the premium paid plus potential minor depreciation of the asset)',
                    'profit_potential': 'Unlimited (minus the cost of the premium)',
                    'best_for': 'Wanting to protect existing positions against downside risk',
                    'iv_preference': 'Lower volatility is better (cheaper premium)'
                }
            ],
            
            # Neutral Strategies
            'neutral': [
                {
                    'name': 'Straddle',
                    'description': 'Simultaneously buy call and put options with the same strike price and expiration date.',
                    'risk_level': 'Limited risk (maximum loss is the total premium paid)',
                    'profit_potential': 'Unlimited (when the price of the underlying asset moves significantly)',
                    'best_for': 'Expecting significant price movement but uncertain about direction',
                    'iv_preference': 'Lower volatility is better for buying (cheaper premium)'
                },
                {
                    'name': 'Strangle',
                    'description': 'Simultaneously buy call and put options with different strike prices (put lower than call) but the same expiration date.',
                    'risk_level': 'Limited risk (maximum loss is the total premium paid)',
                    'profit_potential': 'Unlimited (when the price of the underlying asset moves significantly)',
                    'best_for': 'Expecting significant price movement but uncertain about direction, with stronger cost consciousness',
                    'iv_preference': 'Lower volatility is better for buying (cheaper premium)'
                },
                {
                    'name': 'Butterfly Spread',
                    'description': 'Combine bull and bear spread strategies: buy a call with a low strike price, sell two calls with a middle strike price, and buy another call with a high strike price.',
                    'risk_level': 'Limited risk (maximum loss is the net premium)',
                    'profit_potential': 'Limited (maximum profit occurs at the middle strike price)',
                    'best_for': 'Expecting the price of the underlying asset to fluctuate within a specific range',
                    'iv_preference': 'Lower volatility is better'
                },
                {
                    'name': 'Iron Condor',
                    'description': 'Sell a put spread and a call spread, creating a price range.',
                    'risk_level': 'Limited risk (maximum loss is the difference between the two spreads minus the net income)',
                    'profit_potential': 'Limited (the net premium received)',
                    'best_for': 'Expecting the price of the underlying asset to fluctuate within a specific range',
                    'iv_preference': 'Higher volatility is better for selling (receive more premium)'
                }
            ],
            
            # Volatility Strategies
            'volatility': [
                {
                    'name': 'Long Straddle/Strangle',
                    'description': 'Simultaneously buy call and put options, betting on volatility increase.',
                    'risk_level': 'Limited risk (maximum loss is the total premium paid)',
                    'profit_potential': 'Unlimited (when the price of the underlying asset moves significantly)',
                    'best_for': 'Expecting volatility to increase, prices to move significantly',
                    'iv_preference': 'Current volatility is low, expected to increase'
                },
                {
                    'name': 'Short Straddle/Strangle',
                    'description': 'Simultaneously sell call and put options, betting on volatility decrease.',
                    'risk_level': 'Unlimited risk (when the price of the underlying asset moves significantly)',
                    'profit_potential': 'Limited (the total premium received)',
                    'best_for': 'Expecting volatility to decrease, prices to move within a certain range',
                    'iv_preference': 'Current volatility is high, expected to decrease'
                },
                {
                    'name': 'Calendar Spread',
                    'description': 'Sell a near-term option while buying a longer-term option (same strike price).',
                    'risk_level': 'Limited risk (maximum loss is the net premium)',
                    'profit_potential': 'Limited',
                    'best_for': 'Expecting low volatility in the short term, higher volatility in the long term',
                    'iv_preference': 'Near-term option volatility higher than longer-term option'
                }
            ]
        }
        
        # 定义中文问题和选项
        self.questions_cn = [
            {
                'id': 'market_view',
                'text': '您对标的资产价格走势的看法是？',
                'options': [
                    {'value': 'bullish', 'text': '看涨 - 我认为价格会上涨'},
                    {'value': 'bearish', 'text': '看跌 - 我认为价格会下跌'},
                    {'value': 'neutral', 'text': '中性 - 我认为价格会在一定范围内波动'},
                    {'value': 'uncertain', 'text': '不确定 - 我不确定价格走向'}
                ]
            },
            {
                'id': 'price_movement',
                'text': '您预期价格变动的幅度是？',
                'options': [
                    {'value': 'small', 'text': '小幅度变动 (5%以内)'},
                    {'value': 'moderate', 'text': '中等幅度变动 (5%-15%)'},
                    {'value': 'large', 'text': '大幅度变动 (15%以上)'}
                ]
            },
            {
                'id': 'volatility_view',
                'text': '您对未来波动率的看法是？',
                'options': [
                    {'value': 'increase', 'text': '波动率将上升'},
                    {'value': 'decrease', 'text': '波动率将下降'},
                    {'value': 'stable', 'text': '波动率将保持稳定'},
                    {'value': 'unknown', 'text': '不确定'}
                ]
            },
            {
                'id': 'risk_tolerance',
                'text': '您的风险承受能力是？',
                'options': [
                    {'value': 'low', 'text': '低 - 我希望风险有限'},
                    {'value': 'medium', 'text': '中等 - 我能接受一定风险'},
                    {'value': 'high', 'text': '高 - 我能接受较大风险以追求更高回报'}
                ]
            },
            {
                'id': 'time_horizon',
                'text': '您的投资时间周期是？',
                'options': [
                    {'value': 'short', 'text': '短期 (1个月以内)'},
                    {'value': 'medium', 'text': '中期 (1-3个月)'},
                    {'value': 'long', 'text': '长期 (3个月以上)'}
                ]
            }
        ]
    
        # 定义英文问题和选项
        self.questions_en = [
            {
                'id': 'market_view',
                'text': 'What is your view on the price trend of the underlying asset?',
                'options': [
                    {'value': 'bullish', 'text': 'Bullish - I think the price will rise'},
                    {'value': 'bearish', 'text': 'Bearish - I think the price will fall'},
                    {'value': 'neutral', 'text': 'Neutral - I think the price will fluctuate within a range'},
                    {'value': 'uncertain', 'text': 'Uncertain - I am not sure about the price direction'}
                ]
            },
            {
                'id': 'price_movement',
                'text': 'What magnitude of price movement do you expect?',
                'options': [
                    {'value': 'small', 'text': 'Small movement (within 5%)'},
                    {'value': 'moderate', 'text': 'Moderate movement (5%-15%)'},
                    {'value': 'large', 'text': 'Large movement (above 15%)'}
                ]
            },
            {
                'id': 'volatility_view',
                'text': 'What is your view on future volatility?',
                'options': [
                    {'value': 'increase', 'text': 'Volatility will increase'},
                    {'value': 'decrease', 'text': 'Volatility will decrease'},
                    {'value': 'stable', 'text': 'Volatility will remain stable'},
                    {'value': 'unknown', 'text': 'Uncertain'}
                ]
            },
            {
                'id': 'risk_tolerance',
                'text': 'What is your risk tolerance?',
                'options': [
                    {'value': 'low', 'text': 'Low - I prefer limited risk'},
                    {'value': 'medium', 'text': 'Medium - I can accept some risk'},
                    {'value': 'high', 'text': 'High - I can accept higher risk for potentially higher returns'}
                ]
            },
            {
                'id': 'time_horizon',
                'text': 'What is your investment time horizon?',
                'options': [
                    {'value': 'short', 'text': 'Short-term (within 1 month)'},
                    {'value': 'medium', 'text': 'Medium-term (1-3 months)'},
                    {'value': 'long', 'text': 'Long-term (more than 3 months)'}
                ]
            }
        ]
    
    def set_language(self, language):
        """设置语言 / Set language"""
        if language in ['cn', 'en']:
            self.language = language
    
    def get_language(self):
        """获取当前语言 / Get current language"""
        return self.language
    
    def select_strategies(self, answers):
        """根据用户回答选择合适的期权策略 / Select appropriate option strategies based on user answers"""
        # 根据当前语言选择策略库
        strategies = self.strategies_cn if self.language == 'cn' else self.strategies_en
        recommended_strategies = []
        
        # 基于市场观点的初步筛选
        if answers['market_view'] == 'bullish':
            candidate_strategies = strategies['bullish']
            
            # 根据价格变动幅度进一步筛选
            if answers['price_movement'] == 'large':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['买入看涨期权 (Long Call)']:
                        recommended_strategies.append(strategy)
            elif answers['price_movement'] == 'moderate':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['牛市价差 (Bull Call Spread)', '保护性看涨期权 (Covered Call)']:
                        recommended_strategies.append(strategy)
            elif answers['price_movement'] == 'small':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['卖出看跌期权 (Short Put)', '保护性看涨期权 (Covered Call)']:
                        recommended_strategies.append(strategy)
        
        elif answers['market_view'] == 'bearish':
            candidate_strategies = strategies['bearish']
            
            # 根据价格变动幅度进一步筛选
            if answers['price_movement'] == 'large':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['买入看跌期权 (Long Put)']:
                        recommended_strategies.append(strategy)
            elif answers['price_movement'] == 'moderate':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['熊市价差 (Bear Put Spread)']:
                        recommended_strategies.append(strategy)
            elif answers['price_movement'] == 'small':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['卖出看涨期权 (Short Call)']:
                        recommended_strategies.append(strategy)
        
        elif answers['market_view'] == 'neutral':
            candidate_strategies = strategies['neutral']
            
            # 根据波动率看法进一步筛选
            if answers['volatility_view'] == 'stable':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['铁鹰 (Iron Condor)', '蝶式价差 (Butterfly Spread)']:
                        recommended_strategies.append(strategy)
            else:
                # 如果不确定波动率或预期波动率变化，推荐更保守的中性策略
                for strategy in candidate_strategies:
                    if strategy['name'] in ['铁鹰 (Iron Condor)']:
                        recommended_strategies.append(strategy)
        
        elif answers['market_view'] == 'uncertain':
            # 如果不确定市场方向，考虑波动率策略
            candidate_strategies = strategies['volatility']
            
            if answers['volatility_view'] == 'increase':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['买入跨式/宽跨式 (Long Straddle/Strangle)']:
                        recommended_strategies.append(strategy)
            elif answers['volatility_view'] == 'decrease':
                for strategy in candidate_strategies:
                    if strategy['name'] in ['卖出跨式/宽跨式 (Short Straddle/Strangle)']:
                        recommended_strategies.append(strategy)
            else:
                for strategy in candidate_strategies:
                    if strategy['name'] in ['日历价差 (Calendar Spread)']:
                        recommended_strategies.append(strategy)
        
        # 如果没有找到策略，返回一个默认的保守策略
        if not recommended_strategies:
            # 根据风险承受能力推荐默认策略
            if answers['risk_tolerance'] == 'low':
                for strategy in strategies['neutral']:
                    strategy_name = 'Iron Condor' if self.language == 'en' else '铁鹰 (Iron Condor)'
                    if strategy['name'] == strategy_name:
                        recommended_strategies.append(strategy)
            elif answers['risk_tolerance'] == 'medium':
                for strategy in strategies['bullish']:
                    strategy_name = 'Bull Call Spread' if self.language == 'en' else '牛市价差 (Bull Call Spread)'
                    if strategy['name'] == strategy_name:
                        recommended_strategies.append(strategy)
            else:  # high risk tolerance
                for strategy in strategies['volatility']:
                    strategy_name = 'Long Straddle/Strangle' if self.language == 'en' else '买入跨式/宽跨式 (Long Straddle/Strangle)'
                    if strategy['name'] == strategy_name:
                        recommended_strategies.append(strategy)
        
        return recommended_strategies
    
    def get_questions(self):
        """返回问题列表 / Return the list of questions"""
        # 根据当前语言返回相应的问题列表
        return self.questions_cn if self.language == 'cn' else self.questions_en