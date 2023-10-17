from city_functions import format_city_country

def test_city_country():
    formated_string = format_city_country('santiago', 'chile')
    assert formated_string == 'Santiago, Chile'