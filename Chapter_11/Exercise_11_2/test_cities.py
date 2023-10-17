from city_functions import format_city_country

def test_city_country_with_population():
    formated_string = format_city_country(
        'santiago', 'chile', population=5000000
        )
    assert formated_string == 'Santiago, Chile - population 5000000'

def test_city_country_without_population():
    formated_string = format_city_country('santiago', 'chile')
    assert formated_string == 'Santiago, Chile'