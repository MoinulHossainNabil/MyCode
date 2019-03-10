def swap_case(s):
    result=[i.upper() if i.islower() else i.lower() for i in s]
    return ''.join(result)
