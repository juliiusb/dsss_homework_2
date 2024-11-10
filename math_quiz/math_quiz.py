import random


def random_int(min_value, max_value):
    """
    Random integer in the range of two given limits.

    Parameters:
        min_value (int): The minimum value for the range.
        max_value (int): The maximum value for the range.
    
    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(int(min_value), int(max_value)) # random int with range


def random_operator():
    """
    Random operator from addition, subtraction, and multiplication.

    Returns:
        str: operator
    """
    return random.choice(['+', '-', '*']) # random choice of operators


def calculate(number1, number2, operator):
    """
    Calculates the outcome of a problem given two numbers and an operator that is either +,- or *.
    
    Parameters:
        number1 (int): The first number in the operation.
        number2 (int): The second number in the operation.
        operator (str): The operator, either '+', '-', or '*'.

    Returns:
        tuple: A tuple containing the problem as a string and the answer as an integer.
    """
    problem = f"{number1} {operator} {number2}" # problem as a string
    if operator == '+': answer = number1 + number2 # addition case
    elif operator == '-': answer = number1 - number2 # subtraction case
    else: answer = number1 * number2 # multiplication case
    return problem, answer

def math_quiz():
    """
    Starts the math quiz for a fixed number of problems and prints the score.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(total_questions)): 
        # iterates through the number of problems
        number1 = random_int(1, 10) # generate random number 1
        number2 = random_int(1, 5.5) # generate random number 2
        operator = random_operator() # generate random operator

        problem, answer = calculate(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        # Error handling for user input
        while True:
            try:
                useranswer = int(input("Your answer: "))
                if useranswer == answer:
                    print("Correct! You earned a point.")
                    score += 1
                else:
                    print(f"Wrong answer. The correct answer is {answer}.")
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
