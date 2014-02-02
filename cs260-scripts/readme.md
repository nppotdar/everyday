Script Info:

Background:
At Drexel, my next task as a TA was to take up the CS 260 Data Structures course grading & hold office hours.
While the office hours were interesting, grading quickly became monotonous and annoying.

Analyzing the time-consuming operations, I enum'ed the following:
1. Context switch bw file to be graded and text doc to be opened
2. Context switch bw terminal and file to be opened
3. Occasional non-uniformity in the file-naming scheme of the submissions
4. Uneven questions definitely of different weightages in terms of marks

Workflow:
Script browses through all folders named by the username, checks whether a file going by the assignment name exists or not.
If it doesn't, script prompts each file name and asks the user regarding it.

User prompted to input grade of question one by one on a scale of 3:  

0 - nothing done
1 - in the right direction, but so wrong!
2 - substantial work done towards solving the question
3 - right with everything, minor errors ignored

according to the weightage & maximum marks, these grades are multiplied by a multiplicity factor.
In case grade is less than 3, the user is prompted to add comments as to where the student has been inadequate in answering. 
Keeping this operation in terminal saves considerably on context switch time, thus the user could keep halfscreen windows of pdf and terminal for the grading operations. 

The review file is then generated. On finishing the grading operation, the students can be mailed their respective grades by the additional python script attached.

Future ideas which I may implement if found time to:
LaTeX integration of the review