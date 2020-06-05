# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for file_name in queries:
        if file_name not in cache:
            cache[file_name] = file_name

    for path in files:
        if "/" in path:
            file_name = path.split("/")[-1]
            if file_name in cache:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
