def capital_indexes(string):
    return [i for i, c in enumerate(string) if c.isupper()]
capital_indexes("hellO")