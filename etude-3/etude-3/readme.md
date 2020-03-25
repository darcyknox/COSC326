Author: Darcy Knox
COSC326 S1 2020
Etude 3
Arithmetic

Written in Python 3.7.6

To input from a file, use the command:
python3 Arithmetic.py < filename.txt

To input from the command line, use the command:
python3 Arithmetic.py

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
5 6 7 8 9
123 N
5 3 7 9 1 4 7 1 5 9 4 5 2 2 3 3 4 9 6 9 2 4 5 2 3 4 5 1 7 8 9 3 4 3 4 5 8 8 2 3
694 N

Output produced:

L 10 1 + 2 + 3 + 4
L 5 1 * 2 + 3
L 6 Impossible
L 12 Impossible
L 19 4 + 2 * 3 + 1
L 71 1 + 2 * 3 + 4 * 5 + 6
L 36 1 + 2 * 3 * 4
L 100 Impossible
N 25 1 + 2 * 3 * 4
N 100 Impossible
N 14 1 * 2 + 3 * 4
N 62 1 * 2 + 3 * 4 * 5
N 123 Impossible
N 694 5 + 3 + 7 + 9 + 1 + 4 + 7 + 1 + 5 + 9 + 4 + 5 + 2 + 2 + 3 + 3 + 4 + 9 + 6 + 9 + 2 + 4 + 5 + 2 + 3 + 4 + 5 + 1 + 7 * 8 + 9 + 3 * 4 + 3 * 4 * 5 * 8 + 8 + 2 + 3
