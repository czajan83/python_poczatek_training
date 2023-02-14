import geopy


def main():
    address_1 = "Waniliowa 13, 55-080 Kąty Wrocławskie"
    address_2 = "Waniliowa 15, 55-080 Kąty Wrocławskie"
    geolocator = geopy.Nominatim(user_agent="webinar-agent")
    address_code_1 = geolocator.geocode(address_1)
    address_code_2 = geolocator.geocode(address_2)
    print(address_code_1.latitude - address_code_2.latitude)
    print(address_code_1.longitude - address_code_2.longitude)


if __name__ == "__main__":
    main()
