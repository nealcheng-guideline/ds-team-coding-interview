from decimal import Decimal
from question1 import to_decimal
from question2 import main

# part 1
for _input in (None, "0", 0, 0.0):
    answer = to_decimal(_input)
    assert answer == Decimal(0)
    assert isinstance(answer, Decimal)

# extra credit: handling string floats "41.96"
    # assert to_decimal("0.0") == Decimal(0)

# part 2
llm_answer = main()
assert isinstance(llm_answer, str)
print("Gemini Response:\n")
print(llm_answer)
