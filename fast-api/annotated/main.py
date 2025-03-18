from typing import Annotated

def process_value(
	value: Annotated[int, "範囲: 0 <= value <= 100"]
) -> None:
    if 0 <= value <= 100:
        print("受け取った値は範囲内です。: {value}")
    else:
        raise ValueError("範囲外の値です。受け取った値: {value}")
    
# 呼び出し

process_value(50)

try:
    process_value(150)
except ValueError as e:
    print(e)