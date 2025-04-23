from zeep import Client

# WSDL for the Country Info SOAP service
wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl=wsdl)

def get_country_info(iso_code):
    name = client.service.CountryName(iso_code)
    capital = client.service.CapitalCity(iso_code)
    currency = client.service.CountryCurrency(iso_code)

    print(f"Country code: {iso_code}")
    print(f"Full name: {name}")
    print(f"Capital city: {capital}")
    print(f"Currency: {currency.sName} ({currency.sISOCode})")

if __name__ == "__main__":
    code = input("Enter an ISO country code (e.g. NL, BE, US): ").strip().upper()
    try:
        get_country_info(code)
    except Exception as e:
        print(f"Error: {e}")

