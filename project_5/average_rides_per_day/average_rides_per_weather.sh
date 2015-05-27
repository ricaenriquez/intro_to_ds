#! /bin/bash

cat turnstile_data_master_with_weather.csv | python average_rides_per_weather_mapper.py | sort | python average_rides_per_weather_reducer.py
