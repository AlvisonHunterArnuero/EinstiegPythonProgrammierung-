# Download and install pip install countryinfo

from countryinfo import CountryInfo

country_name = input("Enter Country: ")

country = CountryInfo(country_name)

print("Native Name: ", country.native_name())
print("Capital: ", country.capital())
print("Provinces: ", country.provinces())
print("Population: ", country.population())
print("Demonym: ", country.demonym())
print("Currency: ", country.currencies())
print("Languages: ", country.languages())
print("Region: ", country.region())
print("Sub Region: ", country.subregion())
print("TimeZone: ", country.timezones())
print("Calling Codes: ", country.calling_codes())


