"""I've decided to expand on this exercise.

IMPORTANT: as of writing this (2023-09-29) hyperskill unit test
    uses some older version of Python that doesn't have
    things like positional only arguments and function parameter
    annotations.
    It causes this file to raise SyntaxError.

Instead of a user writing a function for themselves, lets say
the app developer wants a public API for users to select
from the list by user-specified criteria.

In that scenario DEFAULT_LIST would be
just for testing during development.
"""
DEFAULT_LIST = [{"name": "Julia", "gender": "female", "age": 29,
                 "hobbies": ["jogging", "music"], "city": "Hamburg"},
                {"name": "Sasha", "gender": "male", "age": 18,
                 "hobbies": ["rock music", "art"], "city": "Berlin"},
                {"name": "Maria", "gender": "female", "age": 35,
                 "hobbies": ["art"], "city": "Berlin"},
                {"name": "Daniel", "gender": "non-conforming", "age": 50,
                 "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                {"name": "John", "gender": "male", "age": 41,
                 "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]


def select_dates(potential_dates) -> str:
    """Hyperskill task solution."""
    selected: list = [date['name'] for date in potential_dates
                      if date['age'] > 30
                      and date['city'] == 'Berlin'
                      and 'art' in date['hobbies']]

    return ', '.join(selected)


def extended_select(potential_dates: list[dict], /,
                    *, city: str = None,
                    age_range: tuple[int, int] = None,
                    genders: set[str] = None,
                    hobbies: set[str] = None) -> str:
    """Return a string containing names of potential dates,
    separated by ', '.

    potential_dates is a list of dictionaries containing
    data of registered users.

    Has four optional arguments which serve as filters for
    selection and must be specified as keyword arguments.

    city is a string representing the only allowed city,
    the default value is None (any city).

    genders is a set of strings representing allowed genders,
    the default value is None (any gender).

    age_range is a tuple of ints which behave like built-in
    function range() - the first is minimum age
    and the second is one over the maximum age.
    The default value is None (any age).

    hobbies is a set of strings representing required hobbies,
    the default value is None (any hobbies).
    """
    selected: list = [date['name'] for date in potential_dates
                      if
                      (age_range is None or date['age'] in range(*age_range))
                      and (city is None or date['city'] == city)
                      and (hobbies is None or hobbies.issubset(date['hobbies']))
                      and (genders is None or date['gender'] in genders)]
    return ', '.join(selected)


# print(extended_select(DEFAULT_LIST, city='Berlin', genders={'female'}))
