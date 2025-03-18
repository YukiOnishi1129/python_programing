from typing import List

# 整数型の型ヒント
def add(num1: int, num2: int) -> str:
    result:str = '足し算結果=>'
    return result + str(num1 + num2)


# 文字列型の型ヒント
def greet(name: str) -> str:
    return 'Hello ' + name

# 浮動小数展
def divide(dividend: float, divisor: float) -> float:
    return dividend / divisor

# リスト型
# 古い書き方
def get_first_three_elements(elements: List[int]) -> List[int]:
	return elements[:3]

# 辞書型
# 古い書き方
from typing import Dict
def get_value(dictionary: Dict[str, int], key: str) -> int:
	return dictionary[key]

# リスト
# 新しい書き方
def process_items(items: list[str]) -> None:
    for item in items:
        print(item)
        
# 辞書
# 新しい書き方
def count_characters(word_list: list[str]) -> dict[str, int]:
    count_map: dict[str, int] = {}
    for word in word_list:
        count_map[word] = len(word)
    return count_map

# 呼び出し
result_add = add(10, 20)
print(result_add)

greeting = greet('Python')
print(greeting)

result_divide = divide(10.0, 2.0)
print("割り算の結果=>", result_divide)

elements = get_first_three_elements([1, 2, 3, 4, 5])
print("最初から値を3個取り出す=>", elements)

value = get_value({'a': 1, 'b': 2, 'c': 3}, 'b')
print("キーワード「b」に対する値は=>", value)


process_items(['apple', 'banana', 'cherry'])

character_counts = count_characters(['apple', 'banana', 'cherry'])
print("文字に対する文字数は=>", character_counts)
