import simulator
import json
from datetime import datetime


def callback_func(ch, method, properties, body):
    """
    Callback function for every msg in the rabbit mq
    This method take the timestamp and generate simulated PV
    and write into a csv file
    """
    received_msg = json.loads(body)
    received_msg['timestamp'] = datetime.fromtimestamp(received_msg['timestamp'])
    print("Msg received {}".format(received_msg))

    time_data = received_msg['timestamp']
    # Serialize the timestamp to generate simulated PV
    time_serialized = time_data.hour + time_data.minute/60 + time_data.second/60/60 + time_data.microsecond/60/60/60

    # Get the simulated PV
    pv_simulated = simulator.simulate(time_serialized)

    # Format the output
    print("x={} y={}".format(time_serialized, pv_simulated))

    # Write the data into csv file
    with open('pv_results.csv', 'a+') as record_file:
        record_file.write('{},{},{},{}\n'.format(received_msg['timestamp'], received_msg['power_value'],
                                                 pv_simulated, pv_simulated+received_msg['power_value']))

    # Acknowledgement
    ch.basic_ack(delivery_tag=method.delivery_tag)
