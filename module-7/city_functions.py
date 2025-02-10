def format_city_country(city, country, population=None, language=None):
    """Return a string of the form City, Country - population xxx, Language."""
    # Check if both population and language are provided
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    # Check if only population is provided
    elif population:
        return f"{city}, {country} - population {population}"
    # Check if only language is provided
    elif language:
        return f"{city}, {country}, {language}"
    # If neither population nor language is provided
    else:
        return f"{city}, {country}"

# Example calls to the function with different combinations of parameters
print(format_city_country("Santiago", "Chile"))
print(format_city_country("New York", "USA", 120000000))
print(format_city_country("Tokyo", "Japan", 13929000, "Japanese"))