def backup(file):
    with open(file) as f:
        with open("save.py", "w") as f1:
            for line in f:
                f1.write(line)