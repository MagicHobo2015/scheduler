#*****************************************************************************#
#   Authors: Joshua Land, Phu Lam                                             #
#                                                                             #
#   Description: a scheduler to help find meeting times for n people.         #
#                                                                             #
#*****************************************************************************#


"""A class to satisfy an assignment for CPSC 335.

    Scheduler Class Helps find common times for n people.
"""
import datetime as T


class Scheduler():
    # TODO: make this parse the data
    def __init__(self) -> None:
        self.schedules = []
        self.dailyAct = [[0, "0"], [2359, "23:59"]]
        self.results = []
        self.caseNumber = 1

    def parseData(self, file_name: str ) -> set:
        """ Parses data from a text file, for use with scheduler.
        
        Parses the data from a txt file with n persons schedule,
        DailyAct, and a meeting_duration.
        """

        try:
            # Open file
            with open(file_name, 'r') as my_file:
                # read file  ----------------------------> there is a loop here! TODO: make use of this loop
                data = my_file.read().splitlines()
    
        # catch file not found
        except FileNotFoundError as error:
            print(f'An error was encountered:\t {error} \n the most likely cause is missing input file')

        # catch bad permissions
        except PermissionError as error:
            print(f'An error was encountered:\t {error} \n the most likely cause is incorrect permissions on the input file')

        # close file
        my_file.close()
    
        # since we have to look at everything at least once ( O(n) ),
        # I want to do as much here as possible.
        
        for line in data:
            
            # extract variables
            var_name, var_value = line.split('=')
            # trash will be like person1, person2 ... not needed.
            trash, var_name = var_name.split('_')
            # make the string(s) into variables.
            var_value = eval(var_value)
            
            # deal with each variable, duration is the break point per case.
            
            if var_name == 'Schedule ':
                # ----------------------- Combine all the incoming schedules ----------------
                for timeBlock in var_value:
                    # unpack for readability
                    start, end = timeBlock
                    # add the schedules to the master list, keep the string so No need to convert back.
                    self.schedules.append([[self.timeToInt(start), self.timeToInt(end)], [start, end]])

            elif var_name == 'DailyAct ':
                # unpack for readability.
                start, end = var_value
            
                # This is to keep the string and still have an int to compare.
                start = [self.timeToInt(start), start]
                end = [self.timeToInt(end), end]
                
                # only need latest start time, and earliest end time.
                self.dailyAct[0] = (lambda x, y : x if x[0] > y[0] else y)(start, self.dailyAct[0])
                self.dailyAct[1] = (lambda x, y : x if x[1] < y[1] else y)(end, self.dailyAct[1] )

            elif var_name == 'duration ':
                # meeting length from time to int.
                duration = int(var_value/60 * 100)
                
                # Resets everything and displays results.
                self.matchScheduels(duration)


    # int from time.   Cost = 2
    def timeToInt(self, time: str) -> int:
        hr, min = time.split(':')
        return int(int(hr) * 100 + int(min) / 60 * 100)


    def matchScheduels(self, duration: int) -> set:
        """Brings all the data together and gives us an appropriately formated result. """
        
        # makes it clear where the gaps are.
        results = []
        self.schedules.sort()
        # everyone works during these times.
        start, end = self.dailyAct

                # look at all the schedules
        for index in range(0, len(self.schedules) - 1):

            if self.schedules[index][0][1] < start[0] and self.schedules[index+1][0][0] - start[0] > 0:
                results.append([self.dailyAct[0], self.schedules[index + 1][1][0]])

            if self.schedules[index + 1][0][0] - self.schedules[index][0][1] >= duration:
                results.append([self.schedules[index][1][1], self.schedules[index + 1][1][0]])
        if self.schedules[-1][0][-1] - self.dailyAct[0][0] > 0:
            results.append([self.schedules[-1][1][-1], self.dailyAct[1][1]])
        
        self.displayResults(results)
        
        

    def displayResults(self, results: list) -> None:
        """A function to give results that are formated better """
        
                # Reset everything.
        self.schedules = []
        self.dailyAct = [[0, "0"], [2359, "23:59"]]
        
        print(f'Results For test Case {self.caseNumber}:\n\n {results} \n')
        print("-" * 80)
        with open('output.txt', 'a') as f:
            f.write(f'Results For test Case {self.caseNumber}:\n\n {results} \n')
            f.write("-" * 80)
            f.close()
            
        self.caseNumber += 1

# Driver Code
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