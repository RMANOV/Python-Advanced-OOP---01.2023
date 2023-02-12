# Negative vs Positive
# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"

def negative_vs_positive(numbers):
    negative_sum = 0
    positive_sum = 0
    for number in numbers:
        if number < 0:
            negative_sum += number
        else:
            positive_sum += number
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

def main():
    numbers = [int(x) for x in input().split()]
    negative_vs_positive(numbers)
    
if __name__ == "__main__":
    main()