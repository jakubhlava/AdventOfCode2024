import operator
from itertools import product

with open("input.txt", "r") as f:
    equations = [[int(e.split(": ")[0]), [int(o) for o in e.split(": ")[1].split()]] for e in f.read().splitlines()]

def concat_op(a, b):
    return int(str(a) + str(b))

def get_calibration_result_for_equation(equation, variants):
    for variant in variants:
        op = variant.pop(0)
        result = op(equation[1][0], equation[1][1])
        for num in equation[1][2:]:
            op = variant.pop(0)
            result = op(result, num)
        if result == equation[0]:
            return equation[0]
    return 0


total = 0
total_p2 = 0
for eq in equations:
    operator_variants = list(list(comb) for comb in product([operator.add, operator.mul], repeat=len(eq[1])-1))
    total += get_calibration_result_for_equation(eq, operator_variants)
    operator_variants_p2 = list(list(comb) for comb in product([operator.add, operator.mul, concat_op], repeat=len(eq[1])-1))
    total_p2 += get_calibration_result_for_equation(eq, operator_variants_p2)

print("Part 1:", total)
print("Part 2:", total_p2)