# main.py
# 期权策略选择器UI界面 / Option Strategy Selector UI

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from strategy_selector import StrategySelector

class OptionStrategyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("期权策略选择器 / Option Strategy Selector")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # 初始化语言设置 / Initialize language setting
        self.language = "cn"  # 默认使用中文 / Default to Chinese
        
        # 初始化策略选择器 / Initialize strategy selector
        self.strategy_selector = StrategySelector(self.language)
        self.questions = self.strategy_selector.get_questions()
        
        # 用户回答 / User answers
        self.answers = {}
        
        # 当前问题索引 / Current question index
        self.current_question_index = 0
        
        # 创建UI组件 / Create UI components
        self.create_widgets()
        
        # 显示第一个问题 / Show the first question
        self.show_current_question()
    
    def create_widgets(self):
        # 标题框架 / Title frame
        title_frame = tk.Frame(self.root, bg="#2c3e50", padx=10, pady=10)
        title_frame.pack(fill=tk.X)
        
        # 语言切换按钮 / Language switch button
        self.lang_button = tk.Button(title_frame, 
                                  text="EN/中", 
                                  font=("Arial", 10), 
                                  command=self.toggle_language,
                                  bg="#34495e",
                                  fg="white",
                                  width=5)
        self.lang_button.pack(side=tk.RIGHT, padx=10)
        
        # 标题文本 / Title text
        self.title_texts = {
            "cn": "美股期权策略选择器",
            "en": "US Stock Option Strategy Selector"
        }
        
        # 副标题文本 / Subtitle text
        self.subtitle_texts = {
            "cn": "根据您的市场观点推荐适合的期权策略",
            "en": "Recommending suitable option strategies based on your market view"
        }
        
        self.title_label = tk.Label(title_frame, 
                              text=self.title_texts[self.language], 
                              font=("Arial", 18, "bold"), 
                              fg="white", 
                              bg="#2c3e50")
        self.title_label.pack()
        
        self.subtitle_label = tk.Label(title_frame, 
                                text=self.subtitle_texts[self.language], 
                                font=("Arial", 12), 
                                fg="#ecf0f1", 
                                bg="#2c3e50")
        self.subtitle_label.pack(pady=5)
        
        # 标的输入框架 / Symbol input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=10)
        input_frame.pack(fill=tk.X)
        
        # 标的输入标签文本 / Symbol input label text
        self.symbol_label_texts = {
            "cn": "请输入美股标的代码:",
            "en": "Enter US stock symbol:"
        }
        
        self.symbol_label = tk.Label(input_frame, 
                              text=self.symbol_label_texts[self.language], 
                              font=("Arial", 12), 
                              bg="#f0f0f0")
        self.symbol_label.pack(side=tk.LEFT, padx=5)
        
        self.symbol_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.symbol_entry.pack(side=tk.LEFT, padx=5)
        self.symbol_entry.insert(0, "NVDA")  # 默认值 / Default value
        
        # 问题框架 / Question frame
        # 问题框架标题文本 / Question frame title text
        self.question_frame_texts = {
            "cn": "市场观点",
            "en": "Market View"
        }
        
        self.question_frame = tk.LabelFrame(self.root, 
                                         text=self.question_frame_texts[self.language], 
                                         font=("Arial", 12, "bold"), 
                                         bg="#f0f0f0", 
                                         padx=20, 
                                         pady=15)
        self.question_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # 问题标签
        self.question_label = tk.Label(self.question_frame, 
                                    font=("Arial", 12), 
                                    wraplength=800, 
                                    justify=tk.LEFT, 
                                    bg="#f0f0f0")
        self.question_label.pack(anchor=tk.W, pady=5)
        
        # 选项框架
        self.options_frame = tk.Frame(self.question_frame, bg="#f0f0f0")
        self.options_frame.pack(fill=tk.X, pady=5)
        
        # 导航按钮框架 / Navigation button frame
        nav_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=10)
        nav_frame.pack(fill=tk.X)
        
        # 按钮文本 / Button texts
        self.button_texts = {
            "cn": {"prev": "上一步", "next": "下一步", "get_recommendation": "获取推荐", "restart": "重新开始"},
            "en": {"prev": "Previous", "next": "Next", "get_recommendation": "Get Recommendation", "restart": "Restart"}
        }
        
        self.prev_button = tk.Button(nav_frame, 
                                   text=self.button_texts[self.language]["prev"], 
                                   font=("Arial", 11), 
                                   command=self.prev_question, 
                                   state=tk.DISABLED,
                                   padx=10)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(nav_frame, 
                                   text=self.button_texts[self.language]["next"], 
                                   font=("Arial", 11), 
                                   command=self.next_question, 
                                   padx=10)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        # 结果框架 / Result frame
        # 结果框架标题文本 / Result frame title text
        self.result_frame_texts = {
            "cn": "推荐策略",
            "en": "Recommended Strategies"
        }
        
        self.result_frame = tk.LabelFrame(self.root, 
                                       text=self.result_frame_texts[self.language], 
                                       font=("Arial", 12, "bold"), 
                                       bg="#f0f0f0", 
                                       padx=20, 
                                       pady=15)
        # 初始不显示结果框架 / Initially don't show result frame
        
        # 重置按钮 / Reset button
        self.reset_button = tk.Button(nav_frame, 
                                    text=self.button_texts[self.language]["restart"], 
                                    font=("Arial", 11), 
                                    command=self.reset_app, 
                                    padx=10)
        self.reset_button.pack(side=tk.RIGHT, padx=5)
    
    def toggle_language(self):
        # 切换语言 / Toggle language
        self.language = "en" if self.language == "cn" else "cn"
        
        # 更新策略选择器语言 / Update strategy selector language
        self.strategy_selector.set_language(self.language)
        
        # 更新问题列表 / Update question list
        self.questions = self.strategy_selector.get_questions()
        
        # 更新UI文本 / Update UI texts
        self.title_label.config(text=self.title_texts[self.language])
        self.subtitle_label.config(text=self.subtitle_texts[self.language])
        self.symbol_label.config(text=self.symbol_label_texts[self.language])
        self.question_frame.config(text=self.question_frame_texts[self.language])
        self.result_frame.config(text=self.result_frame_texts[self.language])
        
        # 更新按钮文本 / Update button texts
        self.prev_button.config(text=self.button_texts[self.language]["prev"])
        self.reset_button.config(text=self.button_texts[self.language]["restart"])
        
        # 更新下一步按钮文本 / Update next button text
        if self.current_question_index == len(self.questions) - 1:
            self.next_button.config(text=self.button_texts[self.language]["get_recommendation"])
        else:
            self.next_button.config(text=self.button_texts[self.language]["next"])
        
        # 刷新当前问题 / Refresh current question
        self.show_current_question()
    
    def show_current_question(self):
        # 清空选项框架 / Clear options frame
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # 获取当前问题 / Get current question
        question = self.questions[self.current_question_index]
        
        # 设置问题文本 / Set question text
        self.question_label.config(text=question['text'])
        
        # 创建单选按钮变量 / Create radio button variable
        self.option_var = tk.StringVar()
        
        # 如果之前已回答过此问题，设置默认值 / If this question has been answered before, set default value
        if question['id'] in self.answers:
            self.option_var.set(self.answers[question['id']])
        
        # 添加选项 / Add options
        for option in question['options']:
            rb = tk.Radiobutton(self.options_frame, 
                              text=option['text'], 
                              variable=self.option_var, 
                              value=option['value'], 
                              font=("Arial", 11), 
                              bg="#f0f0f0",
                              padx=10,
                              pady=5)
            rb.pack(anchor=tk.W)
        
        # 更新导航按钮状态 / Update navigation button state
        if self.current_question_index == 0:
            self.prev_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL)
        
        if self.current_question_index == len(self.questions) - 1:
            self.next_button.config(text=self.button_texts[self.language]["get_recommendation"])
        else:
            self.next_button.config(text=self.button_texts[self.language]["next"])
    
    def next_question(self):
        # 获取当前问题
        question = self.questions[self.current_question_index]
        
        # 检查是否已选择选项
        if not self.option_var.get():
            messagebox.showwarning("提示", "请选择一个选项")
            return
        
        # 保存回答
        self.answers[question['id']] = self.option_var.get()
        
        # 如果是最后一个问题，显示结果
        if self.current_question_index == len(self.questions) - 1:
            self.show_results()
        else:
            # 否则，显示下一个问题
            self.current_question_index += 1
            self.show_current_question()
    
    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_current_question()
    
    def show_results(self):
        # 获取标的代码 / Get symbol code
        symbol = self.symbol_entry.get().upper()
        if not symbol:
            # 警告消息文本 / Warning message text
            warning_texts = {
                "cn": "请输入标的代码",
                "en": "Please enter a stock symbol"
            }
            messagebox.showwarning("提示 / Tip", warning_texts[self.language])
            return
        
        # 隐藏问题框架 / Hide question frame
        self.question_frame.pack_forget()
        
        # 显示结果框架 / Show result frame
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # 清空结果框架 / Clear result frame
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        # 获取推荐策略
        recommended_strategies = self.strategy_selector.select_strategies(self.answers)
        
        # 显示标的信息 / Show symbol information
        # 标的标签文本 / Symbol label text
        symbol_texts = {
            "cn": f"标的: {symbol}",
            "en": f"Symbol: {symbol}"
        }
        
        symbol_label = tk.Label(self.result_frame, 
                              text=symbol_texts[self.language], 
                              font=("Arial", 14, "bold"), 
                              bg="#f0f0f0")
        symbol_label.pack(anchor=tk.W, pady=5)
        
        # 显示市场观点摘要 / Show market view summary
        view_frame = tk.Frame(self.result_frame, bg="#e1e1e1", padx=15, pady=10)
        view_frame.pack(fill=tk.X, pady=10)
        
        # 市场观点标题文本 / Market view title text
        view_title_texts = {
            "cn": "您的市场观点:",
            "en": "Your Market View:"
        }
        
        view_title = tk.Label(view_frame, 
                            text=view_title_texts[self.language], 
                            font=("Arial", 12, "bold"), 
                            bg="#e1e1e1")
        view_title.pack(anchor=tk.W)
        
        # 市场观点映射 / Market view mapping
        market_view_map = {
            'cn': {
                'bullish': '看涨',
                'bearish': '看跌',
                'neutral': '中性',
                'uncertain': '不确定'
            },
            'en': {
                'bullish': 'Bullish',
                'bearish': 'Bearish',
                'neutral': 'Neutral',
                'uncertain': 'Uncertain'
            }
        }
        
        price_movement_map = {
            'cn': {
                'small': '小幅度变动',
                'moderate': '中等幅度变动',
                'large': '大幅度变动'
            },
            'en': {
                'small': 'Small movement',
                'moderate': 'Moderate movement',
                'large': 'Large movement'
            }
        }
        
        volatility_map = {
            'cn': {
                'increase': '上升',
                'decrease': '下降',
                'stable': '稳定',
                'unknown': '不确定'
            },
            'en': {
                'increase': 'Increasing',
                'decrease': 'Decreasing',
                'stable': 'Stable',
                'unknown': 'Uncertain'
            }
        }
        
        risk_map = {
            'cn': {
                'low': '低',
                'medium': '中等',
                'high': '高'
            },
            'en': {
                'low': 'Low',
                'medium': 'Medium',
                'high': 'High'
            }
        }
        
        time_map = {
            'cn': {
                'short': '短期',
                'medium': '中期',
                'long': '长期'
            },
            'en': {
                'short': 'Short-term',
                'medium': 'Medium-term',
                'long': 'Long-term'
            }
        }
        
        # 视图标签文本 / View label texts
        view_label_texts = {
            'cn': {
                'market': '市场方向',
                'price': '价格变动',
                'volatility': '波动率预期',
                'risk': '风险承受',
                'time': '时间周期'
            },
            'en': {
                'market': 'Market Direction',
                'price': 'Price Movement',
                'volatility': 'Volatility Expectation',
                'risk': 'Risk Tolerance',
                'time': 'Time Horizon'
            }
        }
        
        # 显示用户选择的观点 / Show user's selected views
        not_selected_text = {"cn": "未选择", "en": "Not selected"}
        
        view_text = f"{view_label_texts[self.language]['market']}: {market_view_map[self.language].get(self.answers.get('market_view', ''), not_selected_text[self.language])}\n"
        view_text += f"{view_label_texts[self.language]['price']}: {price_movement_map[self.language].get(self.answers.get('price_movement', ''), not_selected_text[self.language])}\n"
        view_text += f"{view_label_texts[self.language]['volatility']}: {volatility_map[self.language].get(self.answers.get('volatility_view', ''), not_selected_text[self.language])}\n"
        view_text += f"{view_label_texts[self.language]['risk']}: {risk_map[self.language].get(self.answers.get('risk_tolerance', ''), not_selected_text[self.language])}\n"
        view_text += f"{view_label_texts[self.language]['time']}: {time_map[self.language].get(self.answers.get('time_horizon', ''), not_selected_text[self.language])}"
        
        view_summary = tk.Label(view_frame, 
                              text=view_text, 
                              font=("Arial", 11), 
                              justify=tk.LEFT, 
                              bg="#e1e1e1")
        view_summary.pack(anchor=tk.W, pady=5)
        
        # 显示推荐策略数量 / Show recommended strategy count
        strategy_count_texts = {
            "cn": f"推荐策略 ({len(recommended_strategies)}):",
            "en": f"Recommended Strategies ({len(recommended_strategies)}):"
        }
        
        strategy_count_label = tk.Label(self.result_frame, 
                                     text=strategy_count_texts[self.language], 
                                     font=("Arial", 12, "bold"), 
                                     bg="#f0f0f0")
        strategy_count_label.pack(anchor=tk.W, pady=5)
        
        # 创建策略展示框架
        strategies_canvas = tk.Canvas(self.result_frame, bg="#f0f0f0")
        strategies_canvas.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(strategies_canvas, orient="vertical", command=strategies_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        strategies_canvas.configure(yscrollcommand=scrollbar.set)
        strategies_canvas.bind('<Configure>', lambda e: strategies_canvas.configure(scrollregion=strategies_canvas.bbox("all")))
        
        # 创建内部框架用于放置策略卡片
        strategies_frame = tk.Frame(strategies_canvas, bg="#f0f0f0")
        strategies_canvas.create_window((0, 0), window=strategies_frame, anchor="nw")
        
        # 显示推荐策略
        if recommended_strategies:
            for i, strategy in enumerate(recommended_strategies):
                # 创建策略卡片
                strategy_card = tk.Frame(strategies_frame, 
                                       bg="white", 
                                       padx=15, 
                                       pady=15, 
                                       relief=tk.RAISED, 
                                       borderwidth=1)
                strategy_card.pack(fill=tk.X, pady=10, padx=5)
                
                # 策略名称
                strategy_name = tk.Label(strategy_card, 
                                       text=strategy['name'], 
                                       font=("Arial", 13, "bold"), 
                                       bg="white")
                strategy_name.pack(anchor=tk.W)
                
                # 策略描述
                description = tk.Label(strategy_card, 
                                     text=strategy['description'], 
                                     font=("Arial", 11), 
                                     wraplength=750, 
                                     justify=tk.LEFT, 
                                     bg="white")
                description.pack(anchor=tk.W, pady=5)
                
                # 策略详情
                details_frame = tk.Frame(strategy_card, bg="white")
                details_frame.pack(fill=tk.X, pady=5)
                
                # 策略详情标签文本 / Strategy detail label texts
                detail_label_texts = {
                    "cn": {
                        "risk": "风险水平",
                        "profit": "盈利潜力",
                        "best_for": "最适合",
                        "iv": "波动率偏好"
                    },
                    "en": {
                        "risk": "Risk Level",
                        "profit": "Profit Potential",
                        "best_for": "Best For",
                        "iv": "IV Preference"
                    }
                }
                
                # 风险水平 / Risk level
                risk_label = tk.Label(details_frame, 
                                    text=f"{detail_label_texts[self.language]['risk']}: {strategy['risk_level']}", 
                                    font=("Arial", 10), 
                                    bg="white")
                risk_label.pack(anchor=tk.W)
                
                # 盈利潜力 / Profit potential
                profit_label = tk.Label(details_frame, 
                                      text=f"{detail_label_texts[self.language]['profit']}: {strategy['profit_potential']}", 
                                      font=("Arial", 10), 
                                      bg="white")
                profit_label.pack(anchor=tk.W)
                
                # 最适合情况 / Best for
                best_for_label = tk.Label(details_frame, 
                                        text=f"{detail_label_texts[self.language]['best_for']}: {strategy['best_for']}", 
                                        font=("Arial", 10), 
                                        bg="white")
                best_for_label.pack(anchor=tk.W)
                
                # 波动率偏好 / IV preference
                iv_label = tk.Label(details_frame, 
                                  text=f"{detail_label_texts[self.language]['iv']}: {strategy['iv_preference']}", 
                                  font=("Arial", 10), 
                                  bg="white")
                iv_label.pack(anchor=tk.W)
        else:
            # 如果没有推荐策略 / If no strategies are recommended
            no_strategy_texts = {
                "cn": "没有找到符合您市场观点的策略，请尝试调整您的选择。",
                "en": "No strategies found matching your market view. Please try adjusting your selections."
            }
            
            no_strategy_label = tk.Label(strategies_frame, 
                                     text=no_strategy_texts[self.language], 
                                     font=("Arial", 12), 
                                     bg="#f0f0f0")
            no_strategy_label.pack(pady=20)
        
        # 更新导航按钮 / Update navigation buttons
        self.next_button.config(text=self.button_texts[self.language]["restart"], command=self.reset_app)
    
    def reset_app(self):
        # 重置所有状态
        self.answers = {}
        self.current_question_index = 0
        
        # 隐藏结果框架
        if self.result_frame.winfo_manager():
            self.result_frame.pack_forget()
        
        # 显示问题框架
        self.question_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # 重置导航按钮
        self.next_button.config(text="下一步", command=self.next_question)
        
        # 显示第一个问题
        self.show_current_question()

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = OptionStrategyApp(root)
    root.mainloop()