def task(str):
    for ind, value in enumerate(str):
        if value == "0":
            return ind

print(task("111111111110000000000000000"))