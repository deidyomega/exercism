def is_leap_year(value: int):
    # Used: https://support.microsoft.com/en-us/help/214019/method-to-determine-whether-a-year-is-a-leap-year

    if value % 4 != 0:
        return False

    if value % 100 != 0:
        return True

    if value % 400 == 0:
        return True

    return False