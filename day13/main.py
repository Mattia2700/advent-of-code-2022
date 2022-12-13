import ast
import itertools
import functools

def right_order(pair_1: int | list, pair_2: int| list) -> bool:
    # if isinstance(pair_1, list) and isinstance(pair_2, list):
    #     while len(pair_1) != len(pair_2):
    #         if len(pair_1) < len(pair_2):
    #             # print(pair_1, pair_2, end=" ")
    #             pair_1.append(int(-sys.maxsize))
    #             # print(pair_1, pair_2)
    #         elif len(pair_1) > len(pair_2):
    #             # print(pair_1, pair_2, end=" ")
    #             pair_2.append(int(-sys.maxsize))
    #             # print(pair_1, pair_2)

    for l,r in itertools.zip_longest(pair_1, pair_2):

        if l is None and r is not None:
            return True
        elif l is not None and r is None:
            return False

        if isinstance(l, int) and isinstance(r, int):
            if l > r:
                return False
            elif l < r:
                return True
        
        elif isinstance(l, list) and isinstance(r, list):
            res = right_order(l, r)
            if res is not None:
                return res
            else:
                continue
        
        elif isinstance(l, int) and isinstance(r, list):
            return right_order([l], r)
        
        elif isinstance(l, list) and isinstance(r, int):
            return right_order(l, [r])

def compare(pair_1, pair_2) -> int:
    if pair_1 == pair_2:
        return 0
    elif right_order(pair_1, pair_2):
        return -1
    else:
        return 1

with open("input.txt") as f:
    lines = f.read().splitlines()

    elements = []
    pairs_sum = 0

    for index, line in enumerate(lines):
    #     match index % 3:
    #         case 0:
    #             pair_1 = ast.literal_eval(line)
    #         case 1:
    #             pair_2 = ast.literal_eval(line)
    #         case 2:
    #             if right_order(pair_1, pair_2):
    #                 pairs_sum += 1+(index//3)
    #             # print(f"Index {1+(index//3)}:", right_order(pair_1, pair_2))

    # print(pairs_sum)
        if line != "":
            elements.append(ast.literal_eval(line))
    
    elements.append([[2]])
    elements.append([[6]])

    elements.sort(key=functools.cmp_to_key(compare))

    decoder_begin = 1+elements.index([[2]])
    decoder_end = 1+elements.index([[6]])

    print(decoder_begin*decoder_end)
