#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python图形界面计算器 - 使用tkinter
"""

import tkinter as tk
from tkinter import messagebox
import math

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Python计算器")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # 设置主题色
        self.bg_color = "#2c3e50"
        self.btn_color = "#34495e"
        self.accent_color = "#667eea"
        self.text_color = "#ecf0f1"
        
        self.root.configure(bg=self.bg_color)
        
        # 表达式变量
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # 创建界面
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        """创建显示区域"""
        # 显示框
        input_frame = tk.Frame(self.root, bg=self.bg_color, bd=0)
        input_frame.pack(side=tk.TOP, pady=20)
        
        input_field = tk.Entry(
            input_frame,
            font=('arial', 28, 'bold'),
            textvariable=self.input_text,
            width=18,
            bg="#ecf0f1",
            fg="#2c3e50",
            bd=0,
            justify=tk.RIGHT
        )
        input_field.pack(ipady=15)
        
    def create_buttons(self):
        """创建按钮区域"""
        # 按钮配置
        buttons = [
            ('C', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3),
        ]
        
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack()
        
        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            
            # 设置按钮样式
            if text in ['C', '⌫']:
                bg = "#e74c3c"  # 红色
                fg = "white"
            elif text in ['=', '+', '-', '×', '÷', '%']:
                bg = self.accent_color  # 紫色
                fg = "white"
            elif text == '.':
                bg = self.btn_color
                fg = self.text_color
            else:
                bg = self.btn_color
                fg = self.text_color
            
            btn_widget = tk.Button(
                btn_frame,
                text=text,
                width=8 if colspan == 1 else 18,
                height=2,
                font=('arial', 18, 'bold'),
                bg=bg,
                fg=fg,
                bd=0,
                cursor='hand2',
                command=lambda t=text: self.on_button_click(t)
            )
            btn_widget.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
            
    def on_button_click(self, char):
        """按钮点击事件"""
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == '=':
            self.calculate()
        elif char == '×':
            self.expression += "*"
            self.input_text.set(self.expression)
        elif char == '÷':
            self.expression += "/"
            self.input_text.set(self.expression)
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)
            
    def calculate(self):
        """计算结果"""
        try:
            # 安全评估表达式
            result = eval(self.expression)
            
            # 处理浮点数
            if isinstance(result, float):
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 10)
            
            self.expression = str(result)
            self.input_text.set(self.expression)
        except ZeroDivisionError:
            self.input_text.set("错误: 除数为0")
            self.expression = ""
        except Exception as e:
            self.input_text.set("错误")
            self.expression = ""

def main():
    """主函数"""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()