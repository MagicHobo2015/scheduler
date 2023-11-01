from data_processor import PersonDataProcessor

# Define the input file path
input_file = 'input.txt'

# Create an instance of the data_processor.py class
data_processor = PersonDataProcessor(input_file)

# Get the processed data
person_data = data_processor.get_person_data()

# Call the filter_strays method to filter the schedules for each person
data_processor.filter_strays()

meeting_duration = 30  # Change this to your desired meeting duration


free_time = data_processor.calculate_free_time_intervals_for_all(meeting_duration)

# PRINTS FREE TIME INTERVALS FOR ALL
# for person_schedule_key, intervals in free_time.items():
#         person_name = person_schedule_key.replace("_Schedule", '')
#         print(f"Free Time Intervals for {person_name}:")
#
#         for interval in intervals:
#                 print(f"  - {interval[0]} to {interval[1]}")
#
#         print()

# for interval in free_time:
#         print(f"{interval[0]} - {interval[1]}")



# PRINTS FILTERED SCHEDULE
# for key, value in person_data.items():
#     if key.endswith('_Schedule'):
#         person_name = key.replace('_Schedule', '')  # Extract the person's name
#         print(f"{person_name}'s Filtered Schedule:")
#         for event in value:
#             print(f"    {event[0]} - {event[1]}")














# PRINTS SCHEDULE OF EVERYONE
# for key, value in person_data.items():
#     if '_Schedule' in key:
#         print(f"{key}:", value)
#     elif '_DailyAct' in key:
#         print(f"{key}:", value)
#     elif key == 'min_duration_of_meeting':
#         print("Minimum Duration of Meeting:", value)

