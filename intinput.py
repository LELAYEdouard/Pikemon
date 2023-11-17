def intinput(sen: str):
    y = True
    while y:
        try:
            x = int(input(sen))
        except ValueError:
            print("Could you at least give me an actual number?")
            continue
        y = False
    return x