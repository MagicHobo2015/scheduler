# Open the text file
with open('input.txt', 'r') as my_file:
    data = my_file.read()

# Variables (lists of string time)
person1_Schedule = []
person1_DailyAct = []
person2_Schedule = []
person2_DailyAct = []
person3_Schedule = []
person3_DailtAct = []
# global min_duration_of_meeting

# Split the data '7:00'
lines = data.split('\n')

# Process each data
for line in lines:
    if line:

        # Split the line into name and value
        name, value = [part.strip() for part in line.split('=')]

        # Evaluate the value as a Python expression
        value = eval(value)

        # Assign the value to the corresponding variable
        if name == 'person1_Schedule':
            person1_Schedule = value
        elif name == 'min_duration_of_meeting':
            min_duration_of_meeting = value
        elif name == 'person1_DailyAct':
            person1_DailyAct = value
        elif name == 'person2_Schedule':
            person2_Schedule = value
        elif name == 'person2_DailyAct':
            person2_DailyAct = value
        elif name == 'person3_Schedule':
            person3_Schedule = value
        elif name == 'person3_DailyAct':
            person3_DailyAct = value


# Access the schedules and daily activities for person1 and person2

# Convert time string
def time_to_minutes(time_str):
    # converted to minutes
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_time(minutes):
    hours, mins = divmod(minutes, 60)
    return f'{hours:02}:{mins:02}'

def filter_strays(schedule, daily_activity):
    filtered_time = []

    range1 = time_to_minutes(daily_activity[0])
    range2 = time_to_minutes(daily_activity[1])

    for event in schedule:
        event_start = time_to_minutes(event[0])
        event_end = time_to_minutes(event[1])

        # Check if the event entirely falls outside the daily activity range
        if event_end <= range1 or event_start >= range2:
            continue  # Skip

        # Adjust the start time if it starts before the daily activity range
        if event_start < range1:
            event_start = range1

        filtered_time.append([minutes_to_time(event_start), minutes_to_time(event_end)])

    return filtered_time


def calculate_free_time_intervals(schedule, daily_activity, meeting_duration):

    # Free time
    schedule_gaps = []

    # Convert time strings to minutes
    start_time_minutes = time_to_minutes(daily_activity[0])  # 9:00/540
    end_time_minutes = time_to_minutes(daily_activity[1])  # 19:00/1140

    # Starts at daily act range 9:00/540
    free_gap_start = start_time_minutes

    # Iterate through list time
    for event in schedule:

        # Convert list [12:00, 13:00] time to minutes
        event_start = time_to_minutes(event[0])
        event_end = time_to_minutes(event[1])

        # Check if there's a gap, so 9 and 12 yes? append 9:00, 9:30 += in meeting_duration interval
        while free_gap_start + meeting_duration <= event_start:
            schedule_gaps.append([minutes_to_time(free_gap_start), minutes_to_time(free_gap_start + meeting_duration)])
            free_gap_start += meeting_duration

        # Update tracker to end of each event, and then loop to find gap
        free_gap_start = max(free_gap_start, event_end)

    # Check if there are gaps at the end of the daily activity
    while free_gap_start + meeting_duration <= end_time_minutes:
        schedule_gaps.append([minutes_to_time(free_gap_start), minutes_to_time(free_gap_start + meeting_duration)])
        free_gap_start += meeting_duration

    return schedule_gaps


def find_matching_meeting_times(schedule1, schedule2):
    matching_time_slots = []

    for interval1 in schedule1:
        for interval2 in schedule2:
            start1, end1 = interval1
            start2, end2 = interval2

            # Check if the intervals overlap
            if start1 < end2 and start2 < end1:
                # Calculate the overlapping time slot
                overlap_start = max(start1, start2)
                overlap_end = min(end1, end2)
                matching_time_slots.append([overlap_start, overlap_end])

    return matching_time_slots

filtered_person1_Schedule = filter_strays(person1_Schedule, person1_DailyAct)
filtered_person2_Schedule = filter_strays(person2_Schedule, person2_DailyAct)

available_time_person1 = calculate_free_time_intervals(filtered_person1_Schedule, person1_DailyAct, min_duration_of_meeting)
available_time_person2 = calculate_free_time_intervals(filtered_person2_Schedule, person2_DailyAct, min_duration_of_meeting)

matching_times = find_matching_meeting_times(available_time_person1, available_time_person2)

for gap in matching_times:
    print(gap)
