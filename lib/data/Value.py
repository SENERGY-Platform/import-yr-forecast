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


from lib.data.Units import Units


class Value(object):

    def __init__(self,
                 forecasted_for: str,
                 instant_air_pressure_at_sea_level: float,
                 instant_air_temperature: float,
                 instant_cloud_area_fraction: float,
                 instant_cloud_area_fraction_high: float,
                 instant_cloud_area_fraction_low: float,
                 instant_cloud_area_fraction_medium: float,
                 instant_dew_point_temperature: float,
                 instant_fog_area_fraction: float,
                 instant_relative_humidity: float,
                 instant_ultraviolet_index_clear_sky: float,
                 instant_wind_from_direction: float,
                 instant_wind_speed: float,
                 instant_wind_speed_of_gust: float,
                 v12_hours_probability_of_precipitation: float,
                 v1_hours_precipitation_amount: float,
                 v1_hours_precipitation_amount_max: float,
                 v1_hours_precipitation_amount_min: float,
                 v1_hours_probability_of_precipitation: float,
                 v1_hours_probability_of_thunder: float,
                 v6_hours_air_temperature_max: float,
                 v6_hours_air_temperature_min: float,
                 v6_hours_precipitation_amount: float,
                 v6_hours_precipitation_amount_max: float,
                 v6_hours_precipitation_amount_min: float,
                 v6_hours_probability_of_precipitation: float):
        self.forecasted_for = forecasted_for
        self.instant_air_pressure_at_sea_level = instant_air_pressure_at_sea_level
        self.instant_air_temperature = instant_air_temperature
        self.instant_cloud_area_fraction = instant_cloud_area_fraction
        self.instant_cloud_area_fraction_high = instant_cloud_area_fraction_high
        self.instant_cloud_area_fraction_low = instant_cloud_area_fraction_low
        self.instant_cloud_area_fraction_medium = instant_cloud_area_fraction_medium
        self.instant_dew_point_temperature = instant_dew_point_temperature
        self.instant_fog_area_fraction = instant_fog_area_fraction
        self.instant_relative_humidity = instant_relative_humidity
        self.instant_ultraviolet_index_clear_sky = instant_ultraviolet_index_clear_sky
        self.instant_wind_from_direction = instant_wind_from_direction
        self.instant_wind_speed = instant_wind_speed
        self.instant_wind_speed_of_gust = instant_wind_speed_of_gust
        self.v12_hours_probability_of_precipitation = v12_hours_probability_of_precipitation
        self.v1_hours_precipitation_amount = v1_hours_precipitation_amount
        self.v1_hours_precipitation_amount_max = v1_hours_precipitation_amount_max
        self.v1_hours_precipitation_amount_min = v1_hours_precipitation_amount_min
        self.v1_hours_probability_of_precipitation = v1_hours_probability_of_precipitation
        self.v1_hours_probability_of_thunder = v1_hours_probability_of_thunder
        self.v6_hours_air_temperature_max = v6_hours_air_temperature_max
        self.v6_hours_air_temperature_min = v6_hours_air_temperature_min
        self.v6_hours_precipitation_amount = v6_hours_precipitation_amount
        self.v6_hours_precipitation_amount_max = v6_hours_precipitation_amount_max
        self.v6_hours_precipitation_amount_min = v6_hours_precipitation_amount_min
        self.v6_hours_probability_of_precipitation = v6_hours_probability_of_precipitation

    def dict(self, units: Units) -> dict:
        d = {
            "forecasted_for": self.forecasted_for,
            "instant_air_pressure_at_sea_level": self.instant_air_pressure_at_sea_level,
            "instant_air_temperature": self.instant_air_temperature,
            "instant_cloud_area_fraction": self.instant_cloud_area_fraction,
            "instant_cloud_area_fraction_high": self.instant_cloud_area_fraction_high,
            "instant_cloud_area_fraction_low": self.instant_cloud_area_fraction_low,
            "instant_cloud_area_fraction_medium": self.instant_cloud_area_fraction_medium,
            "instant_dew_point_temperature": self.instant_dew_point_temperature,
            "instant_fog_area_fraction": self.instant_fog_area_fraction,
            "instant_relative_humidity": self.instant_relative_humidity,
            "instant_ultraviolet_index_clear_sky": self.instant_ultraviolet_index_clear_sky,
            "instant_wind_from_direction": self.instant_wind_from_direction,
            "instant_wind_speed": self.instant_wind_speed,
            "instant_wind_speed_of_gust": self.instant_wind_speed_of_gust,
            "12_hours_probability_of_precipitation": self.v12_hours_probability_of_precipitation,
            "1_hours_precipitation_amount": self.v1_hours_precipitation_amount,
            "1_hours_precipitation_amount_max": self.v1_hours_precipitation_amount_max,
            "1_hours_precipitation_amount_min": self.v1_hours_precipitation_amount_min,
            "1_hours_probability_of_precipitation": self.v1_hours_probability_of_precipitation,
            "1_hours_probability_of_thunder": self.v1_hours_probability_of_thunder,
            "6_hours_air_temperature_max": self.v6_hours_air_temperature_max,
            "6_hours_air_temperature_min": self.v6_hours_air_temperature_min,
            "6_hours_precipitation_amount": self.v6_hours_precipitation_amount,
            "6_hours_precipitation_amount_max": self.v6_hours_precipitation_amount_max,
            "6_hours_precipitation_amount_min": self.v6_hours_precipitation_amount_min,
            "6_hours_probability_of_precipitation": self.v6_hours_probability_of_precipitation,
            "units": units.dict(),
        }
        return d
