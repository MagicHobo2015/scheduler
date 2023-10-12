#*****************************************************************************#
#   Authors: Joshua Land, Phu Lam                                             #
#                                                                             #
#   Description: a scheduler to help find meeting times for n people.         #
#                                                                             #
#*****************************************************************************#

"""A class to satisfy an assignment for CPSC 335.

    Scheduler Class Helps find common times for n people.
"""
class Scheduler():
    # TODO: make this parse the data
    def __init__(self) -> None:
        pass


    def parseData( file_name: str ) -> set:
        """ Parses data from a text file, for use with scheduler.
        
        Parses the data from a txt file with n persons schedule,
        DailyAct, and a min_duration_of_meeting. 
        """
        try:
            # Open file
            with open(file_name, 'r') as my_file:
                # read file
                data = my_file.read()
        # catch file not found
        except FileNotFoundError as error:
            print(f'An error was encountered:\t {error} \n the most likely 
                  cause is missing input file')
        # catch bad permissions
        except PermissionError as error:
            print(f'An error was encountered:\t {error} \n the most likely
                  cause is incorrect permissions on the input file')
            
        # close file
        my_file.close()
        
        # here data is the input file.
        
def main() -> int:
    inFileName = 'input.txt'
    # create a scheduler
    scheduler = Scheduler() 

    # this pulls data from the file
    scheduler.parseData(inFileName)
    
    # just habbit from c++
    return 0

# if this file gets called as main then, run main.
if __name__ == "__main__":
    main()
# # Variables
# person1_Schedule = []
# person1_DailyAct = []
# person2_Schedule = []
# person2_DailyAct = []

# # Split the data '7:00'
# lines = data.split('\n')

# # Process each data
# for line in lines:
#     if line:
        
#       # Split the line into name and value
#         name, value = [part.strip() for part in line.split('=')]
        
#         # Evaluate the value as a Python expression
#         value = eval(value)

#         # Assign the value to the corresponding variable
#         if name == 'person1_Schedule':
#             person1_Schedule = value
#         elif name == 'person1_DailyAct':
#             person1_DailyAct = value
#         elif name == 'person2_Schedule':
#             person2_Schedule = value
#         elif name == 'person2_DailyAct':
#             person2_DailyAct = value

# # Access the schedules and daily activities for person1 and person2

