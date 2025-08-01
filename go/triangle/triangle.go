package triangle

import "math"

const testVersion = 3

type Kind string

const NaT = "Not A Triagle"
const Equ = "Equilateral"
const Iso = "Isosceles"
const Sca = "Scalene"

func KindFromSides(a, b, c float64) Kind {
	if !isTriangle(a, b, c) {
		return NaT
	}

	if a == b && b == c {
		return Equ
	}

	if a == b || b == c || c == a {
		return Iso
	}

	return Sca
}

func isTriangle(a, b, c float64) bool {
	// Lets only get discrete numbers guys...
	if math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) {
		return false
	}

	// And no nans...
	if math.IsNaN(a) || math.IsNaN(b) || math.IsNaN(c) {
		return false
	}

	// All sides must be greater than zero
	if a <= 0 || b <= 0 || c <= 0 {
		return false
	}

	// Inequality Rule
	if a+b < c || a+c < b || b+c < a {
		return false
	}

	return true

}