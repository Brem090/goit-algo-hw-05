import timeit

def time_algorithm(algo, text, substring, globals):
    stmt = f'{algo}("""{text}""", """{substring}""")'
    return timeit.timeit(stmt, globals=globals, number=1000)
