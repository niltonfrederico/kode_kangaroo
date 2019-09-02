import re

regex_first_letter_captalized = re.compile("(.)([A-Z][a-z]+)")
regex_all_letters_capitalized = re.compile("([a-z0-9])([A-Z])")


def string_to_snakecase(self, string):
    s1 = regex_first_letter_captalized.sub(r"\1_\2", string)
    return regex_all_letters_capitalized.sub(r"\1_\2", s1).lower()


def dict_keys_to_snakecase(self, response):
    converted_dict = {}
    for k, v in response.items():
        new_v = v
        if isinstance(v, dict):
            new_v = self.dict_keys_to_snakecase(v)
        elif isinstance(v, list):
            new_v = list()
            for x in v:
                new_v.append(self.dict_keys_to_snakecase(x))
        converted_dict[self.string_to_snakecase(k)] = new_v
    return converted_dict
