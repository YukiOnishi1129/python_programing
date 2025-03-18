def parse_input(value: int | str) -> str:
    if isinstance(value, int):
        return f"値は整数型です => {value}"
    elif isinstance(value, str):
        return f"値は文字列型です => {value}"
    raise ValueError("引数が整数型/文字列型ではありません")
    
    
# 呼び出し
print(parse_input(100))
print(parse_input("Python"))

try:
    print(parse_input(100.0))
except ValueError as e:
    print(e)