# py3-debug
类级注解，自动为所有方法增加文件信息，类名，方法名，参数名信息，以支持回调链路追踪

![show](https://github.com/Talbot3/py3-debug/blob/main/截屏2025-06-21%2018.43.54.png)
## pypi详情
https://pypi.org/project/py3-debug/

## 安装
```bash
pip install py3-debug
```
## 使用
```python
import debug
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
```
