def format_city_country(city, country, language, population):
    # Return a formatted string in the form 'City, Country'.
    if population:
        print("with population")
        return f"{city.title()}, {country.title()}, language,{language.title()}, population {population.title()}"
    else:
        print("no population")
        return f"{city.title()}, {country.title()},language,{language.title()}"

print(format_city_country("santiago", "chile","spanish","300"))

print(format_city_country("paris", "france","french", "700"))

print(format_city_country("tokyo", "japan", "japanese","100"))

