# Country Info SOAP Demo

This is a simple Python script that demonstrates how to use a public SOAP API to retrieve information about a country using its ISO code.

It uses the [CountryInfoService](http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL), a public SOAP web service.

## Requirements

- Python 3.x
- `zeep` SOAP client

Install dependencies using pip:

```bash
pip install zeep
```

## Usage

Run the script:

```bash
python3 country_info.py
```

You will be prompted to enter an ISO country code (e.g. `NL` for Netherlands, `US` for the United States). The script will return:

- The full name of the country
- Its capital city
- Its currency (name and code)

## Example Output

```
Enter an ISO country code (e.g. NL, BE, US): NL
Country code: NL
Full name: Netherlands
Capital city: Amsterdam
Currency: Euro (EUR)
```
