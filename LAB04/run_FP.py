import question1
import question2
import question3
import sys

def run_question1():
    question1.main()

def run_question2():
    question2.main()

def run_question3():
    question3.main()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 run_FP.py [1|2|3]")
        sys.exit(1)
    question_number = sys.argv[1]
    if question_number == '1':
        run_question1()
    elif question_number == '2':
        run_question2()
    elif question_number == '3':
        run_question3()
    else:
        print("Invalid argument. Use 1 for question 1, 2 for question 2, and 3 for question 3.")
        sys.exit(1)
