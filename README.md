## **LAB 07**


## **SUBMISSION INSTRUCTIONS**

- [x] 0.) Submit | python file using the naming convention below (replace JaneDoe with your first and last name respectively):
	* e JaneDoe7.py
	
	
## **QUESTION**

- [ ] 1.) Write a program that contains the recursive functions below (please note for all the functions, you must use recursion and not loops or built in Python functions):
	- [ ] a.) def power(x, y): This function should recursively compute the power of a number (x represents the number and y represents the power to which its being raised assume y will always be a positive integer) e.g.,
 		* print(power(2, 3))	# 2^3 = 8
 		* print(power(-2, 3))	# -2^3 = -8
 		* print(power(1, 5))	# 1^5 = 1
	- [ ] b.) def cat_ears(n): If every cat has 2 ears, this function should recursively compute the total number of ears based off the number of cats (n represents the total number of cats) e.g.
		* print(cat_ears(0)) # 0 - 0 cats have 0 ears in total
		* print(cat_ears(l)) # 2  1 cat has 2 ears in total
		* print(cat_ears(2)) # 4- 2 cats have 4 ears in total
	- [ ] c.) def alien_ears(n): We have aliens standing in a line, numbered l, 2, The odd aliens (l , 3, . . . ) have 3 ears. The even aliens (2, 4, . . . ) have 2 ears. This function should return the total number of alien ears (n represents the total number of aliens) e.g.,
 		* print(alien_ears(l)) # 3 - (alien I has 3 ears) 
 		* print(alien_ears(2)) # 5 - (alien I has 3 ears, alien 2 has 2 ears)

## Please note:

- [ ] 2.) For the power function, you should only deal with positive powers (0 is not a positive number).
- [ ] 3.) For the cat ears function, account for 0 cats.
- [ ] 4.) For the alien_ears function, there is no position 0 (this should be factored in selecting your base case).
- [ ] 5.) Your Python file only needs to have the 3 functions. The 3 functions should return values (not print them).
- [ ] 6.) The print statements I provided are to help you test ifyour functions work. You are not required to have them in your Python file.
