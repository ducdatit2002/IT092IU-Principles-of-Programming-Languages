# QUESTION 02
users = [
    {'name': 'Alice', 'age': 30, 'score': 85},
    {'name': 'Bob', 'age': 25, 'score': 95},
    {'name': 'Charlie', 'age': 35, 'score': 70},
]

from functools import reduce

# Define the compose function
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

# Filter by minimum age
def filter_by_min_age(min_age):
    def inner(users):
        result = list(filter(lambda user: user['age'] >= min_age, users))
        print(f"After filtering by minimum age {min_age}: {result}")
        return result
    return inner

# Format name
def format_name(style):
    def inner(users):
        if style == 'uppercase':
            result = list(map(lambda user: {**user, 'name': user['name'].upper()}, users))
        elif style == 'lowercase':
            result = list(map(lambda user: {**user, 'name': user['name'].lower()}, users))
        else:
            result = users
        print(f"After formatting names to {style}: {result}")
        return result
    return inner

# Calculate score
def calculate_score(criteria):
    def inner(users):
        if criteria == 'double':
            result = list(map(lambda user: {**user, 'score': user['score'] * 2}, users))
        else:
            result = users
        print(f"After calculating scores with criteria {criteria}: {result}")
        return result
    return inner

def main():
    # Data processing pipeline
    pipeline = compose(
        filter_by_min_age(30),
        format_name('uppercase'),
        calculate_score('double')
    )

    processed_users = pipeline(users)
    print("Final processed users:", processed_users)

if __name__ == "__main__":
    main()


