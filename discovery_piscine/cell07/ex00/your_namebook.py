def array_of_name(name_dict):
    full_name = []
    for first_name, last_name in name_dict.items():
        cap_first = first_name.capitalize()
        cap_last = last_name.capitalize()
        full_name.append(f"{cap_first} {cap_last}")
    return full_name

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_name(persons))