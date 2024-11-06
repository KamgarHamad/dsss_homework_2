import random


def generate_random_number(min_value: int, max_value: int) -> int:
    """
    Generate a random integer within the given range.

    Args:
        min_value (int): Minimum value of the range.
        max_value (int): Maximum value of the range.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_operator() -> str:
    """
    Randomly select a mathematical operator.

    Returns:
        str: One of the strings '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(number1: int, number2: int, operator: str) -> tuple[str, int]:
    """
    Create a math problem and calculate the correct answer.

    Args:
        number1 (int): First number in the math problem.
        number2 (int): Second number in the math problem.
        operator (str): Operator for the math problem ('+', '-', '*').

    Returns:
        tuple: The math problem as a string and the correct answer as an integer.
    """
    problem_string = f"{number1} {operator} {number2}"

    if operator == '+':
        answer_of_operation = number1 + number2
    elif operator == '-':
        answer_of_operation = number1 - number2
    else:
        answer_of_operation = number1 * number2

    return problem_string, answer_of_operation

def math_quiz():
    """
    Conduct a math quiz game where the user answers randomly generated math problems.
    """
    # Initialize the score and total number of questions
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate the math game, by generating random numbers and select a mathematical operator
        number1 = generate_random_number(1, 10)
        number2 = generate_random_number(1, 5)
        operator = choose_operator()
        # Create the math problem and calculate the correct answer
        problem, answer = create_math_problem(number1, number2, operator)
        # Print the math problem
        print(f"\nQuestion: {problem}")

        # Error handling to make sure that the user input is valid
        try:
            # Ask user for answer
            user_answer = int(input("Your answer: "))
            # Check if answer is correct
            if user_answer == answer:
                print("Correct! You earned a point.")
                # Add 1 to the score for the correct answer
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    # Print the final game score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
