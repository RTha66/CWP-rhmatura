def famous_births(historical_figures):
    sort = sorted(historical_figures.values(), key=lambda person: person["date_of_birth"])

    for kon in sort:
        name = kon["name"]
        dob = kon["date_of_birth"]
        print(f"{name} is a great scientist born in {dob}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)