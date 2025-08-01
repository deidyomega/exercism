package bob

import "strings"

const testVersion = 3

func Hey(text string) string {
	text = strings.TrimSpace(text)
	length := len(text)

	// Test for Blank
	if length == 0 {
		return "Fine. Be that way!"
	}

	// Test for Shouting
	if strings.ContainsAny(text, "ABCDEFGHIJKLMNOPQRSTUVWXYZ") && strings.ToUpper(text) == text {
		return "Whoa, chill out!"
	}

	// Test for question
	if text[length-1:] == "?" {
		return "Sure."
	}

	return "Whatever."

}