# Open the text file
with open('input.txt', 'r') as my_file:
    data = my_file.read()

# Variables
person1_Schedule = []
person1_DailyAct = []
person2_Schedule = []
person2_DailyAct = []

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
        elif name == 'person1_DailyAct':
            person1_DailyAct = value
        elif name == 'person2_Schedule':
            person2_Schedule = value
        elif name == 'person2_DailyAct':
            person2_DailyAct = value

# Access the schedules and daily activities for person1 and person2

