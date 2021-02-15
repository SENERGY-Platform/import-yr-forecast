#  Copyright 2021 InfAI (CC SES)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from datetime import datetime, timedelta
from typing import Tuple, List, Optional

import requests
from import_lib.import_lib import get_logger

from lib.data.Units import Units
from lib.data.Value import Value
from lib.util import datetime_to_http, http_to_datetime, extract

MET_BASE_URL = "https://api.met.no"
MET_FORECAST_URL = MET_BASE_URL + "/weatherapi/locationforecast/2.0/complete"

user_agent = "SenergyYrForecastImport github.com/SENERGY-Platform/import-yr-forecast"
logger = get_logger(__name__)


def get_data(if_modified_since: Optional[datetime], lat: float, long: float, altitude: Optional[int],
             max_forecasts: int) -> Tuple[datetime, datetime, Optional[Units], List[Tuple[datetime, Value]]]:
    '''
    :param if_modified_since: Previously returned Last-Modified
    :param lat: Latitude
    :param long: Longitude
    :param altitude: Altitude
    :param max_forecasts:
    :return: Last-Modified, Expires, Units, Forecasts
    '''
    lat = round(lat, 4)
    long = round(long, 4)

    headers = {'User-Agent': user_agent}  # required by MET ToS
    if if_modified_since is not None:
        headers["If-Modified-Since"] = datetime_to_http(if_modified_since)

    url = MET_FORECAST_URL + "?lat=" + str(lat) + "&lon=" + str(long)
    if altitude is not None:
        url += "&altitude=" + str(altitude)
    r = requests.get(url, headers=headers)
    if not r.ok:
        raise RuntimeError("Error contacting MET Api")
    last_modified = http_to_datetime(r.headers["Last-Modified"])
    expires = http_to_datetime(r.headers["Expires"]) + timedelta(seconds=1)
    if r.status_code == 304:
        logger.info("Data unmodified (HTTP 304)")
        return last_modified, expires, None, []

    j = r.json()
    if "properties" not in j or "meta" not in j["properties"] or "units" not in j["properties"]["meta"]:
        raise RuntimeError("Error: Invalid MET Response")
    api_units = j["properties"]["meta"]["units"]
    units = Units(
        air_pressure_at_sea_level=extract(api_units, "air_pressure_at_sea_level"),
        air_temperature=extract(api_units, "air_temperature"),
        air_temperature_max=extract(api_units, "air_temperature_max"),
        air_temperature_min=extract(api_units, "air_temperature_min"),
        cloud_area_fraction=extract(api_units, "cloud_area_fraction"),
        cloud_area_fraction_high=extract(api_units, "cloud_area_fraction_high"),
        cloud_area_fraction_low=extract(api_units, "cloud_area_fraction_low"),
        cloud_area_fraction_medium=extract(api_units, "cloud_area_fraction_medium"),
        dew_point_temperature=extract(api_units, "dew_point_temperature"),
        fog_area_fraction=extract(api_units, "fog_area_fraction"),
        precipitation_amount=extract(api_units, "precipitation_amount"),
        precipitation_amount_max=extract(api_units, "precipitation_amount_max"),
        precipitation_amount_min=extract(api_units, "precipitation_amount_min"),
        probability_of_precipitation=extract(api_units, "probability_of_precipitation"),
        probability_of_thunder=extract(api_units, "probability_of_thunder"),
        relative_humidity=extract(api_units, "relative_humidity"),
        ultraviolet_index_clear_sky=extract(api_units, "ultraviolet_index_clear_sky"),
        wind_from_direction=extract(api_units, "wind_from_direction"),
        wind_speed=extract(api_units, "wind_speed"),
        wind_speed_of_gust=extract(api_units, "wind_speed_of_gust")
    )
    values: List[Tuple[datetime, Value]] = []
    if "properties" not in j or "timeseries" not in j["properties"]:
        raise RuntimeError("Error: Invalid MET Response")

    for forecast in j["properties"]["timeseries"]:
        values.append((last_modified, Value(
            forecasted_for=forecast["time"],
            instant_air_pressure_at_sea_level=extract(forecast, "data.instant.details.air_pressure_at_sea_level"),
            instant_air_temperature=extract(forecast, "data.instant.details.air_temperature"),
            instant_cloud_area_fraction=extract(forecast, "data.instant.details.cloud_area_fraction"),
            instant_cloud_area_fraction_high=extract(forecast, "data.instant.details.cloud_area_fraction_high"),
            instant_cloud_area_fraction_low=extract(forecast, "data.instant.details.cloud_area_fraction_low"),
            instant_cloud_area_fraction_medium=extract(forecast, "data.instant.details.cloud_area_fraction_medium"),
            instant_dew_point_temperature=extract(forecast, "data.instant.details.dew_point_temperature"),
            instant_fog_area_fraction=extract(forecast, "data.instant.details.fog_area_fraction"),
            instant_relative_humidity=extract(forecast, "data.instant.details.relative_humidity"),
            instant_ultraviolet_index_clear_sky=extract(forecast, "data.instant.details.ultraviolet_index_clear_sky"),
            instant_wind_from_direction=extract(forecast, "data.instant.details.wind_from_direction"),
            instant_wind_speed=extract(forecast, "data.instant.details.wind_speed"),
            instant_wind_speed_of_gust=extract(forecast, "data.instant.details.wind_speed_of_gust"),
            v12_hours_probability_of_precipitation=extract(forecast,
                                                           "data.next_12_hours.details.probability_of_precipitation"),
            v1_hours_precipitation_amount=extract(forecast, "data.next_1_hours.details.precipitation_amount"),
            v1_hours_precipitation_amount_max=extract(forecast, "data.next_1_hours.details.precipitation_amount_max"),
            v1_hours_precipitation_amount_min=extract(forecast, "data.next_1_hours.details.precipitation_amount_min"),
            v1_hours_probability_of_precipitation=extract(forecast,
                                                          "data.next_1_hours.details.probability_of_precipitation"),
            v1_hours_probability_of_thunder=extract(forecast, "data.next_1_hours.details.probability_of_thunder"),
            v6_hours_air_temperature_max=extract(forecast, "data.next_1_hours.details.air_temperature_max"),
            v6_hours_air_temperature_min=extract(forecast, "data.next_6_hours.details.air_temperature_min"),
            v6_hours_precipitation_amount=extract(forecast, "data.next_6_hours.details.precipitation_amount"),
            v6_hours_precipitation_amount_max=extract(forecast, "data.next_6_hours.details.precipitation_amount_max"),
            v6_hours_precipitation_amount_min=extract(forecast, "data.next_6_hours.details.precipitation_amount_min"),
            v6_hours_probability_of_precipitation=extract(forecast,
                                                          "data.next_6_hours.details.probability_of_precipitation")
        )))
        if len(values) == max_forecasts:
            return last_modified, expires, units, values
    return last_modified, expires, units, values
