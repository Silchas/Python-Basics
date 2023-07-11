# Grade Analyzer
## A program that prints out the average, highest and lowest grades from a list of tuples
### Details
<p>The grade analyzer program takes two parameters; student grades and operations.</br>
The program uses the if-else loop to iterate through the list of tuples following the operations.</br>
The average operation starts with initiating the total=0 and the increments the total with the total += student[1]. The student[1] is used to pick the grades in each tuple as they appear after the students name and then the total is divided by the len of student grades.</br>
The highest grade operation starts with declaring the highest variable and storing the first tuple and the iterating through the tuples.</br>
The iteration stores the grade it encounter that is higher than the previous one and finally assigns that grade to the highest variable. A similar approach is used to find the lowest grade.</br>
The program returns a value error should an operation not defined be run.</p>
