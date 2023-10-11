# scheduler

*Project* *1*: *Implementing* Algorithm*
*Fall* *2023*   *CPSC* *335.01* - *Algorithm* *Engineering*
*Instructor: Divyansh Mohan Rao* 

##Abstract
Develop a pseudocode for an algorithm; analyze your pseudocode mathematically; implement the code for the algorithm of your choice; test your implementation; and describe your results.
The Problem:  Matching Group Schedules
The group schedule matching takes two or more arrays as input. The arrays represent slots that are already booked and the login/logout time of group members. It outputs an array containing intervals of time when all members are available for a meeting for a minimum duration expected.

Mathematical notation of the problem.
Hint: you will be good even if you don’t understand  mathematical notations of the problem.
Group Schedule Problem 
input: arrays m of related elements comprising the time intervals and an array d, representing the daily active periods of all members. . U is a global set of all arrays. The problem can be represented as: 
U= i=1nmi
output: a set of HashMap, r,  such that r⊆ U


The group schedule matching takes the following inputs: 
Busy_Schedule: An array list that represents the person's existing schedule (they can’t plan any other engagement during these hours) 
Hint: Array may be 2D or maybe a list, ArrayList.
Working_period: Daily working periods of group members. (login, logout) 
Just two entries [login, logout]
Duration of the meeting It outputs a list of list containing intervals of time when all members are available for a meeting for the minimum duration of the meeting required.


An analogy for the question:
Assume you and your group members provide your schedules and daily availability. The goal is to find a time slot when all of you are free for a meeting, considering the provided schedules and the minimum duration required for the meeting.


Sample Input
Enter person1_Schedule =[[ ‘7:00’, ’8:30’],  [’12:00’, ’13:00’],  [’16:00’, ’18:00’]]
person1_DailyAct = [‘9:00’, ’19:00’]

Enter person2_Schedule = [[ ‘9:00’, ’10:30’],  [’12:20’, ’13:30’],  [’14:00’, ’15:00’], [’16:00’, ’17:00’ ]]
person2_DailyAct = [‘9:00’, ’18: 30’]

Enter duration_of_meeting =30

Sample output 
[[’10:30’, ’12:00’], [’15:00’, ’16:00’], [’18:00’, ’18:30’]]

Implementation
Have following files 
1. Project1_starter.py or project1_starter.cpp that defines functions for the algorithm described above. You will need to develop and write the functions. Describe how to run your program in the ReadMe file 
2. Input.txt containing the sample input files. Use these sample files to run your program to see whether your algorithm implementations work correctly. Have a new line character separating the sample test cases (10) At least 2 must be edge cases.
 3. Output.txt – load the sample test case result to output.txt

To Do
Create a Readme file and include your name(s) and email address(es). The Readme file should also contain instructions on how to run your program. 
Study the sample input and output above. Write your own complete and clear code for an algorithm to solve this problem. 
Analyze your code for the algorithm mathematically and prove its efficiency class. 
Implement your algorithm using either Python or C++. 
Run your code using different data inputs

Finally, produce a brief written project report in PDF format. Your report should include the following:

Your names, CSUF email address(es), and an indication that the submission is for project 1. 
A screenshot showing the output of your code for a minimum of 10 test cases defined by yourself. At least 2 must be edge cases.
Link to your github repo. Keep it private until due date. Make it public after due date(No code commits allowed post due date, any code change after due date will not be considered for grading)
A brief proof argument for the time complexity of your algorithm, including step-counts

Mathematical Analysis
Analyze your algorithm mathematically. You should prove a specific big-O efficiency class for the algorithm. The analysis should be routine, similar to the ones we have done in class and in the textbook. The algorithm’s efficiency class will be one of On, On2, On3, or On4.

Can we do better? What changes do you think can be made to your algorithm to increase its time complexity/efficiency?  Will an increase in n change the complexity class? n is the number of persons in the group.
Grading Rubric
The suggested grading rubric is below.

Algorithm design and implementation = 50 points, divided as follows:
Clear and complete code (full points for Optimal solution O(n),  -5 points for O(n^2) and -10 for brute force solution) = 20 points 
Complete and clear README.md file = 3 points 
Successful compilation = 15 points 
Produces accurate result = 12 points
 Analysis = 50 points, divided as follows 
Mathematical analysis and proof, including step count =22 
Report document presentation = 20 points 
Screenshot = 5 points
Comments on possible improvements = 3

Ensure your submissions are your own works. Your submissions will be checked for similarities using a software.
Submitting your code
Submit your project as a zip folder with the following format <team_member1_member2>.zip to the Project 1 link on Canvas. It allows for multiple submissions. 
Include the following files in the zip folder: 
Readme
Input.txt 
Project1_starter.py or project1_starter.cpp 
Output.txt
Deadline
The project deadline is Friday, October 27, 11:59 pm on Canvas.
