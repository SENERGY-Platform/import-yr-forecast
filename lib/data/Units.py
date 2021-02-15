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


class Units(object):

    def __init__(self,
                 air_pressure_at_sea_level: str,
                 air_temperature: str,
                 air_temperature_max: str,
                 air_temperature_min: str,
                 cloud_area_fraction: str,
                 cloud_area_fraction_high: str,
                 cloud_area_fraction_low: str,
                 cloud_area_fraction_medium: str,
                 dew_point_temperature: str,
                 fog_area_fraction: str,
                 precipitation_amount: str,
                 precipitation_amount_max: str,
                 precipitation_amount_min: str,
                 probability_of_precipitation: str,
                 probability_of_thunder: str,
                 relative_humidity: str,
                 ultraviolet_index_clear_sky: str,
                 wind_from_direction: str,
                 wind_speed: str,
                 wind_speed_of_gust: str):
        self.air_pressure_at_sea_level = air_pressure_at_sea_level
        self.air_temperature = air_temperature
        self.air_temperature_max = air_temperature_max
        self.air_temperature_min = air_temperature_min
        self.cloud_area_fraction = cloud_area_fraction
        self.cloud_area_fraction_high = cloud_area_fraction_high
        self.cloud_area_fraction_low = cloud_area_fraction_low
        self.cloud_area_fraction_medium = cloud_area_fraction_medium
        self.dew_point_temperature = dew_point_temperature
        self.fog_area_fraction = fog_area_fraction
        self.precipitation_amount = precipitation_amount
        self.precipitation_amount_max = precipitation_amount_max
        self.precipitation_amount_min = precipitation_amount_min
        self.probability_of_precipitation = probability_of_precipitation
        self.probability_of_thunder = probability_of_thunder
        self.relative_humidity = relative_humidity
        self.ultraviolet_index_clear_sky = ultraviolet_index_clear_sky
        self.wind_from_direction = wind_from_direction
        self.wind_speed = wind_speed
        self.wind_speed_of_gust = wind_speed_of_gust

    def dict(self) -> dict:
        d = {
            "air_pressure_at_sea_level": self.air_pressure_at_sea_level,
            "air_temperature": self.air_temperature,
            "air_temperature_max": self.air_temperature_max,
            "air_temperature_min": self.air_temperature_min,
            "cloud_area_fraction": self.cloud_area_fraction,
            "cloud_area_fraction_high": self.cloud_area_fraction_high,
            "cloud_area_fraction_low": self.cloud_area_fraction_low,
            "cloud_area_fraction_medium": self.cloud_area_fraction_medium,
            "dew_point_temperature": self.dew_point_temperature,
            "fog_area_fraction": self.fog_area_fraction,
            "precipitation_amount": self.precipitation_amount,
            "precipitation_amount_max": self.precipitation_amount_max,
            "precipitation_amount_min": self.precipitation_amount_min,
            "probability_of_precipitation": self.probability_of_precipitation,
            "probability_of_thunder": self.probability_of_thunder,
            "relative_humidity": self.relative_humidity,
            "ultraviolet_index_clear_sky": self.ultraviolet_index_clear_sky,
            "wind_from_direction": self.wind_from_direction,
            "wind_speed": self.wind_speed,
            "wind_speed_of_gust": self.wind_speed_of_gust,
        }
        return d
