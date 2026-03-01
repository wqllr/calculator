#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一个简单的Python Hello World程序 - 含计算功能
"""

def main():
    """主函数"""
    print("=" * 40)
    print("Hello World! 🌍")
    print("欢迎来到Python编程世界！✨")
    print("=" * 40)
    
    # 调用计算器功能
    calculator()

def calculator():
    """简单计算器"""
    print("\n🔢 欢迎使用简易计算器！")
    print("支持的运算：加(+)、减(-)、乘(*)、除(/)")
    print("输入 'q' 退出计算器\n")
    
    while True:
        try:
            user_input = input("请输入计算式（如 5 + 3）: ").strip()
            
            if user_input.lower() == 'q':
                print("👋 计算器已退出！")
                break
            
            # 解析输入
            import re
            # 匹配数字和运算符
            pattern = r'^(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+\.?\d*)$'
            match = re.match(pattern, user_input)
            
            if not match:
                print("⚠️  输入格式错误！请输入如：5 + 3 或 10 * 2")
                continue
            
            num1 = float(match.group(1))
            op = match.group(2)
            num2 = float(match.group(3))
            
            # 计算结果
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("⚠️  错误：除数不能为0！")
                    continue
                result = num1 / num2
            else:
                print("⚠️  不支持的运算符！")
                continue
            
            # 输出结果
            # 如果结果是整数，去掉小数部分
            if result == int(result):
                result = int(result)
            print(f"✅ 结果：{num1} {op} {num2} = {result} 🎉\n")
            
        except ValueError:
            print("⚠️  请输入有效的数字和运算符！")
        except Exception as e:
            print(f"⚠️  发生错误：{e}")

if __name__ == "__main__":
    main()