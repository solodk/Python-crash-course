def format_city_country(city, country, population=False):
    answer = f"{city.title()}, {country.title()}"
    if population:
        answer += f" - population {population}"
    return answer
