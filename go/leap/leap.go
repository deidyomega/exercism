package leap

const testVersion = 3

func IsLeapYear(year int) bool {
	// Used: https://support.microsoft.com/en-us/help/214019/method-to-determine-whether-a-year-is-a-leap-year

	if year % 4 != 0 {
		return false
	}

	if year % 100 != 0 {
		return true
	}

	if year % 400 == 0 {
		return true
	}

	return false	

}