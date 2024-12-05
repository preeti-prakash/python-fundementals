def provide_weather_advisory(temperature):
    status=''
    if temperature < 0:
        status = "It's freezing! Wear a heavy coat."
    elif temperature > 0 and temperature < 10:
        status="It's cold! Bundle up."
    elif temperature > 11 and temperature < 20:
        status="It's cool! A light jacket will do."
    elif temperature > 20:
        status= "It's warm! Enjoy the day."
    return status

print(provide_weather_advisory(15))  # Output: "It's cool! A light jacket will do."