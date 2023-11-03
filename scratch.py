class Scheduler():
    # TODO: make this parse the data
    def __init__(self) -> None:
        self.schedules = []
        self.dailyAct = [[0, "0"], [2359, "23:59"]]
        self.results = []
        self.caseNumber = 1
        
    def parseData(self, file_name: str ) -> list:
        # THIS SECTION -------------- ALL ABOUT PARSING VARIABLES ------------------- VARS INCOMING
        # look at each line.
        for line in open('input.txt').read().splitlines():
            # This section is all about
            # seperate name from value.
            name, value = line.split('=')
            # get just the usefull part of the name
            garbage, name = name.split('_')
            # evaluate the value
            value = eval(value)

        # END VARIABLE PARSING SECTION-------------------------------------------- END VARS INCOMING

        # VARIABLE NAME EVAL HAPPENS HERE ---------------------------------------- NAME EVALUATION
            if name == 'Schedule ':
                # ----------------------- Combine all the incoming schedules ----------------
                for timeBlock in value:
                    # unpack for readability
                    start, end = timeBlock
                    # add the schedules to the master list, keep the string so No need to convert back.
                    self.schedules.append([[self.timeToInt(start), self.timeToInt(end)], [start, end]])

            # -------------------------------- END SCHEDULE SECTION --------------------------
            elif name == "DailyAct ":
            # -------------------------------- DAILY ACTIVITY -------------------------------
                # unpack for readability.
                start, end = value

                start = [self.timeToInt(start), start]
                end = [self.timeToInt(end), end]
                # only need latest start time, and earliest end time.
                self.dailyAct[0] = (lambda x, y : x if x[0] > y[0] else y)(start, self.dailyAct[0])
                self.dailyAct[1] = (lambda x, y : x if x[1] < y[1] else y)(end, self.dailyAct[1] )
            # -------------------------------- END DAILY ACTIVITY --------------------------------
            elif name == "duration ":
            # -------------------------------- DURATION - THE WORK HORSE. EACH CASE ENDS HERE ----     
                # duration is special because it seperates test cases.
                    # when you get here, everything needed to finish is in memory.
                results = []
                # meeting length
                duration = int(value/60 * 100)
                # now we have them all, sort them.
                self.schedules.sort()
                # Hours where everyone is working.
                start, end = self.dailyAct
                # look at all the schedules
                for index in range(0, len(self.schedules) - 1):

                    if self.schedules[index][0][1] < start[0] and self.schedules[index+1][0][0] - start[0] > 0:
                        results.append([self.dailyAct[0], self.schedules[index + 1][1][0]])

                    if self.schedules[index + 1][0][0] - self.schedules[index][0][1] >= duration:
                        results.append([self.schedules[index][1][1], self.schedules[index + 1][1][0]])
                if self.schedules[-1][0][-1] - self.dailyAct[0][0] > 0:
                    results.append([self.schedules[-1][1][-1], self.dailyAct[1][1]])
                # Reset everything.
                self.schedules = []
                self.dailyAct = [[0, "0"], [2359, "23:59"]]
                print("-" * 74)
                print(f'Results For test Case {self.caseNumber}:\t\t\t\t\t\t \n\n {results} \n')
                self.caseNumber += 1

        # END VARIABLE NAME EVAL ------------------------------------------------- END NAME EVALUATION


    def timeToInt(self, time: str) -> int:
        hr, mn = time.split(':')
        return int(int(hr) * 100 + int(mn) / 60 * 100)

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

# time to int
# def timeToInt(time: str) -> int:
#     return filter(lambda h, m : int(h) * 100 + int(m) / 60 * 100, (time.split(':'))).__next__()