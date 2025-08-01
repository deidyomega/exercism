package acronym

import "strings"

const testVersion = 3

func Abbreviate(str string) string {
	// convert dashes to spaces
	str = strings.Replace(str, "-", " ", -1)
	strList := strings.Split(str, " ")
	output := ""
	for _, word := range strList {
		output += strings.ToUpper(string(word[0]))
	}
	return output
}