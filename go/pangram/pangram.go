package pangram

import "strings"

const testVersion = 2

func IsPangram(str string) bool {
	// The idea is to remove all testChars until they are gone, if that happens, then it's a Pangram, if the str runs out before that event, then return false
	str = strings.ToLower(str)
	for _, letter := range "abcdefghijklmnopqrstuvwxyz" {
		// This does the second loop for me
		if !strings.ContainsRune(str, letter) {
			return false
		}
	}
	return true
}