import re
from functools import reduce

class Monkey:
    def __init__(self, index: int, items: list, update: list, divisibility: list) -> "Monkey":
        self.index = index
        self.update = update
        self.items = items
        self.divisibility = divisibility[index]
        self.parsed = 0
        self.supermodulo = None

    def compite_supermodulo(self, divisibility: list):
        self.supermodulo = reduce(lambda x,y: x*y, divisibility)


    def assign_true_false(self, true: "Monkey", false: "Monkey") -> None:
        self.true = true
        self.false = false

    def add_item(self, item: int) -> None:
        self.items.append(item)
    
    def print_items(self):
        print(f"Monkey {self.index} has {self.items}")
    
    def get_parsed(self):
        return self.parsed

    def do_round(self):
        for item in self.items:
            self.parsed += 1
            new_item = self.compute(item, self.update[0], self.update[1])
            new_item %= self.supermodulo
            if self.is_divisible(new_item, self.divisibility):
                self.true.add_item(new_item)
                # print(f"Monkey {self.index} throws {new_item} to monkey {self.true.index}")
            else:
                self.false.add_item(new_item)
                # print(f"Monkey {self.index} throws {new_item} to monkey {self.false.index}")
        self.items = []

    def is_divisible(self, item: int, divisibility: int) -> bool:
        if (item) % divisibility == 0:
            return True
        else:
            return False

    def compute(self, old: int, operation: str, factor):
        # check if factor can be converted to int
        if operation == "+":
            if factor.isnumeric():
                return int(old) + int(factor)
        else:
            if factor.isnumeric():
                return int(old) * int(factor)
            else:
                return int(old) * int(old)

with open("input.txt") as f:
    lines = f.read().splitlines()
    monkeys = []
    monkey = None
    op = None
    test = []
    items = []
    true = []
    false = []
    for index, line in enumerate(lines):
        match(index%7):
            case 0:
                monkey = int(line.split(" ")[1][0])
            case 1:
                values = line.split(" ")[4:]
                items = []
                for value in values:
                    items.append(int(re.sub(r"[^0-9]", "", value)))
            case 2:
                op = line.split(" ")[6:]
            case 3:
                test.append(int(re.findall(r"Test: divisible by (\d+)", line).pop()))
            case 4:
                true.append(int(re.findall(r"If true: throw to monkey (\d+)", line).pop()))
            case 5:
                false.append(int(re.findall(r"If false: throw to monkey (\d+)", line).pop()))
            case 6:
                monkeys.append(Monkey(monkey, items, op, test))
    
    for i,(t,f) in enumerate(zip(true, false)):
        monkeys[i].assign_true_false(monkeys[t], monkeys[f])
        monkeys[i].compite_supermodulo(test)
    
    for i in range(10000):
        for monkey in monkeys:
            monkey.do_round()
        
        # if i % 100 == 0:
        #     print(f"Round {i} done")
            # for monkey in monkeys:
                # print(f"Monkey {monkey.index} parsed {monkey.get_parsed()} items")

    parsed_items = []

    for monkey in monkeys:
        parsed_items.append(monkey.get_parsed())

    parsed_items = sorted(parsed_items, reverse=True)
    print(parsed_items[0]*parsed_items[1])