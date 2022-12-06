with open("input.txt") as f:
    counter = 14
    times = 0
    # read 4 characters at a time
    string = f.read(14)
    while len(string) == 14:
        # print(string)
        charset = set(string)
        # print(charset)
        if len(charset) == 14:
            break
        counter += 1
        # go back 3 characters and read 4 characters at a time
        f.seek(f.tell() - 13)
        string = f.read(14)
    print(counter)
            

