''' Functions are o en used to validate input. Write afunction that accepts a single
 integer as a parameter and returns Trueif the integer is in the range 0 to 100
 (inclusive), or False otherwise. Write a short program to test the function.'''

#function to check if a number is in the range 0 10 100
def check_range (num):
    return 0 <= num <= 100

#test the function
print (" Testing the function ")

#list of numbers
test_num = [-10, 0, 50, 100, 105]

#check each number and print whether it's in the range or not
for number in test_num:
    print(f" Is {number} in the range 0-100? {check_range(number)}")