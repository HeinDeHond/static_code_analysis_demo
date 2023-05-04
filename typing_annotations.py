from typing import Any, List, Optional, Dict, Union


def format_name(first_name: Any, last_name: Any):
    """Return a full name: "John JAMESEON"."""

    a = first_name.capitalize()  # Add here a proper method to have the first name capitalized.
    b = last_name.upper()  # Add here a proper method to have the last name uppercased.
    return f"{a} {b}"


def format_name_annotated(first_name: str, last_name: str) -> str:
    """Return a full name: "John JAMESEON"."""

    a = first_name.capitalize()  # Add here a proper method to have the first name capitalized.
    b = last_name.upper() # Add here a proper method to have the last name uppercased.
    return f"{a} {b}"


def process_character(s):
    ...


def add_words_to_collection(string_to_process: Any, collection: List):
    for word in string_to_process:
        collection.append(word)
        pass
    return collection[0]


def add_words_to_collection_annotated(
    string_to_process: str, collection: list[str]
) -> list[str]:
    for word in string_to_process.split():
        collection.append(word)
        pass
    return collection


def concatenate(s1: str, s2: str) -> str:
    return s1 + s2


def is_even(x: int) -> bool:
    return x % 2 == 0


def greet(name: str, greeting: Optional[str] = None) -> str:
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}!"


def parse_number(num: str) -> Union[float, int, None]:
    result: Union[float, int, None] = float('nan')
    try:
        result = int(num)
    except ValueError:
        try:
            result = float(num)
        except ValueError:
            result = None
    return result


def get_evens(numbers: List[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


def count_words(words: str) -> Dict[str, int]:
    word_counts: Dict[str, int] = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def merge_dicts(fruits1: Dict[int, int], fruits2: Dict[int, int]) -> Dict[int, int]:
    result = fruits1.copy()
    for key, value in fruits2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


# Define two dictionaries
fruits1 = [{"apple": 3}, {"banana": 2}, {"orange": 1}]
fruits2 = {"banana": 1, "cherry": 4}


def main():
    print(format_name("john", "jameson"))
    print(format_name_annotated("john", "jameson"))


if __name__ == "__main__":
    main()
