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
        self.number_of_people = None
        self.list_of_schedules = {}
        pass

    def parseData(self, file_name: str ) -> set:
        """ Parses data from a text file, for use with scheduler.

        Parses the data from a txt file with n persons schedule,
        DailyAct, and a min_duration_of_meeting. 
        """

        try:
            # Open file
            with open(file_name, 'r') as my_file:
                # read file
                data = my_file.read().splitlines()
                self.number_of_people = (len(data) - 1) // 2
        # catch file not found
        except FileNotFoundError as error:
            print(f'An error was encountered:\t {error} \n the most likely cause is missing input file')
        # catch bad permissions
        except PermissionError as error:
            print(f'An error was encountered:\t {error} \n the most likely cause is incorrect permissions on the input file')

        # close file
        my_file.close()
    
        # make data into actuall arrays.

        for index in range(self.number_of_people):
            person, schedule = data[index*2].split('=')
            garbage, activeTime = data[index*2 + 1].split('=')
            self.list_of_schedules[person] = {schedule, activeTime}
        for person in self.list_of_schedules:
            for schedule in self.list_of_schedules[person]:
                print(schedule)
                

def main() -> int:
    inFileName = 'input.txt'
    # create a scheduler
    scheduler = Scheduler()

    # this pulls data from the file
    scheduler.parseData(inFileName)

    # just habit from c++
    return 0

# if this file gets called as main then, run main.
if __name__ == "__main__":
    main()