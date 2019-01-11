# prototype for a web page. Everything seems to work
# we'll download a file, then many files

import urllib.request
import pandas as pd
import json

# strings to build url
baseurl = "https://api.usa.gov/crime/fbi/sapi/api/"
add_api = "?api_key=bZdxxBmYk8kaCWmBbjnT35zO1OgjKumQ8b2xfzYg"
data_type = "summarized/agencies/"
final_param = "/offenses"

agency_df = pd.read_csv("agencies_trimmed.csv", index_col=0)

# choose your agency
target_agency = "Indiana University: Bloomington"

target_df = agency_df[agency_df.agency_name == target_agency]
agency_ori = target_df.iloc[0]["ori"]

# gets agency data
urllib.request.urlretrieve(baseurl + data_type + agency_ori + final_param + add_api, agency_ori + ".json")

new_file = open(agency_ori + ".json","r")
new_str = new_file.read()
print(new_str[:100])
new_file.close()
# resources
# https://github.com/fbi-cde/crime-data-frontend/blob/master/README.md
# https://github.com/fbi-cde/crime-data-api/blob/master/README.md
# https://api.data.gov/signup/
# https://ucr.fbi.gov/nibrs/nibrs-user-manual  List of offense codes starts page 16
# https://ucr.fbi.gov/fingerprints_biometrics/iafis/state_cntry2000.pdf List of state abbreviations starts page 2
# https://crime-data-explorer.fr.cloud.gov/api#!/offender45controller/getStateOffenderCountsUsingGET
# another tool https://www.ucrdatatool.gov/Search/Crime/Local/RunCrimeJurisbyJurisLarge.cfm

