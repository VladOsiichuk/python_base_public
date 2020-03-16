def append(s, symbol, position=None):
    if position is None:
        result = s + symbol
        return result

    result = ""
    for i in range(len(s)):
        if i != position:
            result += s[i]
        else:
            result += symbol + s[i]

    return result


def append_with_slices(s, symbol, index=None):
    """
    s = "1235"
    symbol = 4
    position = 3
    """
    if index is None:
        result = s + symbol
        return result

    #      s[:1] =="P" + y" +  s[1:] == "thon"
    return s[:index] + symbol + s[index:]


print(append_with_slices("Pthon", "y", 1))

# result = append("124", "3")
#
# # Should return True
# print("43" in result)
#
# if "43" in result:
#     print(result)
