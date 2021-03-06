Author: Darcy Knox  
COSC326 S1 2020  
Etude 3  
Arithmetic  

This program takes in 2 lines of input. The first line being a set of numbers, the second line being a target number, and a letter N or L which determines the order of operations to apply (normal/bedmas, or left to right). The program determines whether or not the list of numbers, in the given order, can result in the target value by using only addition or multiplication in any permutation upon the numbers. If it is possible, the output will return the order letter, the target number, and the expression that evaluates to the target number.

This program was originally written in Python, but due to inefficient performance, was rewritten in Java.  

Compile using the command:  
javac Arithmetic.java  

To input from a file, use the command:  
java Arithmetic < filename.txt  

To input from the command line, use the command:  
java Arithmetic  


Test cases used:

1 2 3 4  
10 L  
1 2 3  
5 L  
1 2 3 4  
6 L  
1 2 3 4  
12 L  
4 2 3 1  
19 L  
1 2 3 4 5 6  
71 L  
1 2 3 4  
36 L  
1 2 3 4 5 1 2 3 4 5  
100 L  
1 2 3 4  
25 N  
1 2 3 4  
100 N  
1 2 3 4  
14 N  
1 2 3 4 5  
62 N  
1 3 5 7 9  
79 N  
2 3 4 5  
19 N  
5 6 7 8 9  
123 N  
5 3 7 9 1 4 7 1 5 9 4 5 2 2 3 3 4 9 6 9 2 4 5 2 3 4 5 1 7 8 9 3 4 3 4 5 8 8 2 3  
694 N  
5 3 7 9 1 4 7 1 5 9 4 5 2 2 3 3 4 9 6 9 2 4 5 2 3 4 5 1 7 8  
180 N  
5 3 7 9 1 4 7 1 5 9 4 5 2 2 3 3 4 9 6 9 2 4 5 2 3 4 5 1 7  
131 N  
5 3 7 9 1 4 7 1 5 9 4 5 2 2 3 3 4 9 6 9 2 4 5 2 3 4 5 1 7 8 9  
189 N  
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2  
84 L  
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2  
1048576 L  
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2  
131072 N  
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2  
262144 N  
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2  
168 N  


Output produced:

L 10 1 + 2 + 3 + 4  
L 5 1 * 2 + 3  
L 6 impossible  
L 12 impossible  
L 19 4 + 2 * 3 + 1  
L 71 1 + 2 * 3 + 4 * 5 + 6  
L 36 1 + 2 * 3 * 4  
L 100 impossible  
N 25 1 + 2 * 3 * 4  
N 100 impossible  
N 14 1 * 2 + 3 * 4  
N 62 1 * 2 + 3 * 4 * 5  
N 79 1 + 3 * 5 + 7 * 9  
N 19 2 + 3 * 4 + 5  
N 123 impossible  
N 694 5 + 3 + 7 + 9 + 1 + 4 + 7 + 1 + 5 + 9 + 4 + 5 + 2 + 2 + 3 + 3 + 4 + 9 + 6 + 9 + 2 + 4 + 5 + 2 + 3 + 4 + 5 + 1 + 7 * 8 + 9 + 3 * 4 + 3 * 4 * 5 * 8 + 8 + 2 + 3  
N 180 5 + 3 + 7 + 9 + 1 + 4 + 7 + 1 + 5 + 9 + 4 + 5 + 2 + 2 + 3 + 3 + 4 + 9 + 6 + 9 + 2 + 4 + 5 + 2 + 3 + 4 + 5 + 1 + 7 * 8  
N 131 5 + 3 + 7 + 9 + 1 + 4 + 7 + 1 + 5 + 9 + 4 + 5 + 2 + 2 + 3 + 3 + 4 + 9 + 6 + 9 + 2 + 4 + 5 + 2 + 3 + 4 + 5 + 1 + 7  
N 189 5 + 3 + 7 + 9 + 1 + 4 + 7 + 1 + 5 + 9 + 4 + 5 + 2 + 2 + 3 + 3 + 4 + 9 + 6 + 9 + 2 + 4 + 5 + 2 + 3 + 4 + 5 + 1 + 7 * 8 + 9  
L 84 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2  
L 1048576 2 + 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2  
N 131072 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2  
N 262144 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2  
N 168 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2  
