// Convert a number to a string, the contents of which depend on the number's factors.

// - If the number has 3 as a factor, output 'Pling'.
// - If the number has 5 as a factor, output 'Plang'.
// - If the number has 7 as a factor, output 'Plong'.
// - If the number does not have 3, 5, or 7 as a factor,
//   just pass the number's digits straight through.

package raindrops

import "strconv"

const testVersion = 3

func Convert(value int) string {
	var output string

	if value%3 == 0 {
		output += "Pling"
	}
	if value%5 == 0 {
		output += "Plang"
	}
	if value%7 == 0 {
		output += "Plong"
	}

	if output == "" {
		return strconv.Itoa(value)
	}

	return output
}