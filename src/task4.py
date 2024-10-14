def reverse_dict(src: dict) -> dict:
    new = dict()

    for key, value in src.items():
        if new.get(value) is None:
            new[value] = key
        else:
            if type(new.get(value)) == tuple:
                new[value] = (*new[value], key)
            else:
                new[value] = (new[value], key)

    return new
