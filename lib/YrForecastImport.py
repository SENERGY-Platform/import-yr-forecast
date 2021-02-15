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

import sched
import json
from datetime import timedelta

from import_lib.import_lib import get_logger, ImportLib

from lib.data.YrForecastDataFetcher import get_data

logger = get_logger(__name__)
slice_size = timedelta(days=30)


class YrForecastImport:
    def __init__(self, lib: ImportLib, scheduler: sched.scheduler):
        self.__lib = lib
        self.__scheduler = scheduler
        self.__lat = self.__lib.get_config("lat", 51.34)
        self.__long = self.__lib.get_config("long", 12.38)
        self.__max_forecasts = self.__lib.get_config("max_forecasts", 1)
        self.__altitude = self.__lib.get_config("altitude", -1)
        if self.__altitude == -1:
            self.__altitude = None

        self.__last_modified = None
        self.import_current()

    def import_current(self):
        self.__last_modified, expires, units, values = get_data(self.__last_modified, self.__lat, self.__long,
                                                                self.__altitude, self.__max_forecasts)
        for t, v in values:
            self.__lib.put(t, v.dict(units))
            logger.debug(json.dumps(v.dict(units)))
        logger.info("Imported " + str(len(values)) + " values")
        logger.info("Scheduling next run for " + str(expires))
        self.__scheduler.enterabs(expires.timestamp(), 1, self.import_current)
