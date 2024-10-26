from itertools import groupby


def bit_xor(a, b):
    return a ^ b


pattern_to_xorbit = {
    "0": 0b1010,
    "1": 0b0101,
    "2": 0b1111,
    "3": 0b0010,
    "4": 0b1011,
    "5": 0b0111,
    "6": 0b1110,
    "7": 0b0001,
}


def handle_only_0to9_xor(value: int, xor_bit: int) -> int:
    result = value - 65
    counter = 0
    while bit_xor(result, xor_bit) > 9:
        result -= 16
        counter += 1
        # NaN 처리
        if result < 0:
            return None
    return bit_xor(result, xor_bit) + counter * 9


def split_string_into_list(string: str) -> list[str]:
    return [int(string[i : i + 2], 16) for i in range(0, len(string), 2)]


def decode_in_sequence(encoded_lst: list[str]) -> list[int]:
    return [
        handle_only_0to9_xor(color, pattern_to_xorbit[str(idx % 8)])
        for idx, color in enumerate(encoded_lst)
    ]


def split_list(lst: list[int]) -> list[list[int]]:
    return [list(group) for key, group in groupby(lst, lambda x: x is not None) if key]


def combine_elements(lst: list[int]) -> list[int]:
    return [(lst[i] * 16 + lst[i + 1]) for i in range(0, len(lst) - 1, 2)]


def apply_to_nested_list(lst: list[list[int]], func) -> list[list[int]]:
    return [func(ele) for ele in lst]


def to_color_dict(lst: list[list[int]]) -> dict[int, list[int]]:
    return {ele[0]: ele[1:] for ele in lst}


def decode_given_color_query(color_query: str) -> dict[int, list[int]]:
    return to_color_dict(
        apply_to_nested_list(
            split_list(decode_in_sequence(split_string_into_list(color_query))),
            combine_elements,
        )
    )


if __name__ == "__main__":
    # Sample usage
    print(
        decode_given_color_query(
            "4b454a524e434e4987464e464b424d45598a504260475c585d578443505660494e434b8f4c435d47594d4a41884849484b474e434c"
        )
    )
    pass
