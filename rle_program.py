def to_hex_string(data):
    hex_string = ""

    for num in data:
        # Ensure the number is within the valid range (0-255)
        num = max(0, min(num, 255))
        # Convert to hexadecimal and remove the '0x' prefix
        hex_representation = hex(num)[2:]
        hex_string += hex_representation

    return hex_string


def count_runs(flat_data):
    runs = 0
    current_run = 1

    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            current_run += 1
        else:
            runs += (current_run + 14) // 15
            current_run = 1

    runs += (current_run + 14) // 15

    return runs


def encode_rle(flat_data):
    if not flat_data:
        return []  # Return an empty list if the input list is empty

    encoded_data = []
    current_run = [flat_data[0], 1]

    for i in range(1, len(flat_data)):
        if flat_data[i] == current_run[0]:
            if current_run[1] < 15:
                current_run[1] += 1
            else:
                encoded_data.extend(current_run)
                current_run = [flat_data[i], 1]
        else:
            encoded_data.extend(current_run)
            current_run = [flat_data[i], 1]

    encoded_data.extend(current_run)

    result = []
    for i in range(0, len(encoded_data), 2):
        result.extend([encoded_data[i + 1], encoded_data[i]])

    return result


def get_decoded_length(rle_data):
    result = 0
    total = sum(rle_data[i] for i in range(len(rle_data)) if i % 2 == 0)
    return total


def decode_rle(rle_data):
    decoded_data = []
    i = 0
    while i < len(rle_data):
        count = rle_data[i]
        value = rle_data[i + 1]
        decoded_data.extend([value] * count)
        i += 2
    return decoded_data


def string_to_data(data_string):
    hexList = {'0': 0, '1': 1, '2': 2, '3': 3,
               '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15, 'X': 0}
    data_string = data_string.upper()
    data_result = []
    for i in data_string:
        data_result.extend([hexList[i]])
    return data_result
