def line_splitter(text):
    return text.split("\n")


def empty_line_filter(line):
    return line is not None and len(line) > 0


def str_reverse(text):
    return text[::-1]


def parse(*, filename, splitter=line_splitter, filterer=empty_line_filter, parser):
    directory = "../inputs/"
    with open(directory + filename, "r") as f:
        file_contents = f.read()
    splits = splitter(file_contents)
    filtered_split = filter(filterer, splits)
    return map(parser, filtered_split)
