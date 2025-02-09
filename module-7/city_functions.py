# city_functions.py

def format_city_country(city, country):
    "Return a formatted string in the form 'City, Country'."
    return f"{city.title()}, {country.title()}"

print(format_city_country("santiago", "chile"))
print(format_city_country("paris", "france"))
print(format_city_country("tokyo", "japan"))
