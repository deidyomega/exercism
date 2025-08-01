package twofer

import "fmt"

func ShareWith(my_string string) string {
	if my_string == "" {
		return "One for you, one for me."
	}
	var value = fmt.Sprintf("One for %s, one for me.", my_string)
	return value
}