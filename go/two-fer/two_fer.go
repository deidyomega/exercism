package twofer

import "fmt"

func ShareWith(myString string) string {
	if myString == "" {
		return "One for you, one for me."
	}
	return fmt.Sprintf("One for %s, one for me.", myString)
}