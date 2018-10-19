import argparse
from datetime import datetime
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

from app import app

parser = argparse.ArgumentParser(description='Report on Twilio stats for call-in app')
parser.add_argument('sdate', 
  nargs=3,
  type=int,
  help='Campaign start date in the format M D YYYY, where M D and Y are integers')
parser.add_argument('edate', 
  nargs=3,
  type=int,
  help='Campaign end date in the format M D YYYY, where M D and Y are integers')
parser.add_argument('--duration', 
  type=int, 
  help='Minimum duration, in seconds. Used to count how many calls were longer than the amount provided. Defaults to 10.')
parser.add_argument('--delete',
  action='store_true',
  help='Deletes all call records for the time frame provided. ***No further reports can be run on the data set after running the program with this flag.***')
args = parser.parse_args()

try:
    twilio_client = Client(app.config['TWILIO_ACCOUNT_SID'],
                           app.config['TWILIO_AUTH_TOKEN'])
except Exception as e:
    msg = 'Missing configuration variable: {0}'.format(e)
    print(jsonify({'error': msg}))

start = datetime(args.sdate[2], args.sdate[0], args.sdate[1])
end = datetime(args.edate[2], args.edate[0], args.edate[1])
calls_list = twilio_client.calls.list(
                         start_time_after=start,
                         start_time_before=end,
                         status='completed')
 
def count_calls(call_length=10):
  total_calls = []
  actual_calls = []
  
  if args.duration:
    call_length = args.duration
  for call in calls_list:
    # print(call.direction)
    if call.direction == 'outbound-dial':
      total_calls.append(call)
      if int(call.duration) > call_length:
        actual_calls.append(int(call.duration))
  print('Total completed calls between', str(start), ' and ', str(end), ': ', len(total_calls))
  print('Calls longer than ', call_length, ' seconds: ', len(actual_calls))

def delete_calls():
  if args.delete:
    print('Deleting all calls...')
    for call in calls_list:
      call.delete()

count_calls()
delete_calls()

