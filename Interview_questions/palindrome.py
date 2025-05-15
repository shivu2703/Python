def is_palindrome(str):
    str= str.lower()
    return str == str[::-1]

print(f"Is kataka palindrome: {is_palindrome("kataka")}")
print(f"Is Radar palindrome: {is_palindrome("Radar")}")
print(f"Is Katak palindrome: {is_palindrome("Katak")}")