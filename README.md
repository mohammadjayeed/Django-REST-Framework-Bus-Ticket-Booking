## Language

- Python v3.10.5

## Framework

- Django v4.1.1
- Djangorestframework v3.14.0

## Database

- SQLite


## API Reference

|ACTIONS|HTTP METHODS|ENDPOINTS|
|-----------------|---|--------------|
|GET PASSENGERS' LIST|GET|/api/passengers|
|GET BUS SCHEDULE LIST| GET |/api/bus-schedule-chart|
|RESERVE SEATS|POST|/api/reserve/|

### note : for now, mostly ModelViewSet has been used for the sake of ease of use, subject to change if the app is further developed

## Features

- passengers endpoint shows passenger list (readonly)
- bus schedule chart shows all the bus schedule along with number of seats booked for each bus scheduled
- bus listing gets removed from the chart once reservation reaches the limit 35 ( assuming each has 35 available seats )
- reserve end points create reservation by taking passenger details and bus travel id ( the id that is auto generated during object creation has been assumed as travel id)
