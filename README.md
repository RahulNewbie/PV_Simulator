Requirements:

This application is using pika and numpy library. pika is used for rabbit mq server
and numpy is used for pv simulation.

please install this two library using pip

Installation:

This application has two components
a) Meter: This component is responsible for putting msgs in broker(Rabbitmq)
b) Simulator: This component is responsible for reading msgs from Rabbitmq and make pv simulation using the msg.
Then it adds this value with the meter value and output the result in a csv file

please keep Rabbitmq up and running before running the application

Application will run in two steps
1. Go to the meter folder and run meter.py
python meter.py

2. Open another tab and go to the simulator folder and run
python simulator.py

result will be stored in pv_result.csv in the simulator folder

