with open("input.txt") as f:
    pairs = f.read().splitlines()
    overlaps = 0
    
    for pair in pairs:
        elf1, elf2 = pair.split(",")
        elf1_begin, elf1_end = elf1.split("-")
        elf2_begin, elf2_end = elf2.split("-")
        elf1_begin = int(elf1_begin)
        elf1_end = int(elf1_end)
        elf2_begin = int(elf2_begin)
        elf2_end = int(elf2_end)
        if elf1_end >= elf2_begin and elf1_begin <= elf2_end:
            overlaps+=1
    
    print(overlaps)
        