package leap

const testVersion = 3

// IsLeapYear used website https://support.microsoft.com/en-us/help/214019/method-to-determine-whether-a-year-is-a-leap-year
func IsLeapYear(year int) bool {
	if year%4 != 0 {
		return false
	}

	if year%100 != 0 {
		return true
	}

	if year%400 == 0 {
		return true
	}

	return false
}