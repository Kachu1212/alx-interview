# 0x05. N Queens

This project is to test readiness for technical interviews.

## File Descriptions
### Mandatory
1. [0-nqueens.py](./0-nqueens.py) - a script that solves the N-Queen problem.

   - Usage: `nqueens N`
	 - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
   - where N must be an integer greater or equal to `4`
	 - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
	 - If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
   - The program should print every possible solution to the problem
	 - One solution per line
	 - Format: see example
	 - You don’t have to print the solutions in a specific order 
	
   **Execution Example**
   ```
   Niyi@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
   [[0, 1], [1, 3], [2, 0], [3, 2]]
   [[0, 2], [1, 0], [2, 3], [3, 1]]
   Niyi@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
   [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
   [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
   [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
   [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
   Niyi@ubuntu:~/0x08. N Queens$
   ```

## The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
![](https://camo.githubusercontent.com/3b060d7a1bf5dc1874c642546f5281dd85773fd6ad6e3a4f445b48afa41861e8/687474703a2f2f692e696d6775722e636f6d2f4e4c41464949742e676966)
