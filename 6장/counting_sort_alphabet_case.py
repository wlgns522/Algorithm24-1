def counting_sort_alphabet_case(arr):
    count = [0] * 52  
    output = [''] * len(arr)

    for char in arr:
        if 'a' <= char <= 'z':
            count[ord(char) - ord('a')] += 1
        elif 'A' <= char <= 'Z':
            count[ord(char) - ord('A') + 26] += 1

    for i in range(1, 52):
        count[i] += count[i - 1]

    for char in reversed(arr):
        if 'a' <= char <= 'z':
            output[count[ord(char) - ord('a')] - 1] = char
            count[ord(char) - ord('a')] -= 1
        elif 'A' <= char <= 'Z':
            output[count[ord(char) - ord('A') + 26] - 1] = char
            count[ord(char) - ord('A') + 26] -= 1
    
    return ''.join(output)

input_string = "qwertyuiopalskWOEIRUTYAdjKDJFHGZfhgmxncbvzQPLSMXNCBV"
sorted_string = counting_sort_alphabet_case(input_string)
print(f"정렬된 문자열: {sorted_string}")
