def parse(*, filename, splitter, filterer, parser):
    directory = "inputs/"
    with open(directory + filename, "r") as f:
        file_contents = f.read()
    splits = splitter(file_contents)
    filtered_split = filter(filterer, splits)
    return list(map(parser, filtered_split))


def line_splitter(text):
    return text.split("\n")


def str_reverse(text):
    return text[::-1]
