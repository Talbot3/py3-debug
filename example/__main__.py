from debug import debug
# 使用示例
@debug
class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.add(1, 2))
    print(calculator.sub(1, 2))
