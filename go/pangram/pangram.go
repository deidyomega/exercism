package pangram

import "strings"

const testVersion = 2

func IsPangram(str string) bool {
	// The idea is to remove all testChars until they are gone, if that happens, then it's a Pangram, if the str runs out before that event, then return false
	str = strings.ToLower(str)
	testChars := []rune{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
	for _, char := range str {
		for index, tchar := range testChars {
			if char == tchar {
				testChars = append(testChars[:index], testChars[index+1:]...)
			}

			if len(testChars) == 0 {
				return true
			}
		}
	}
	return false
}