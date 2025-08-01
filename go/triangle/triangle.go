package triangle

const testVersion = 3

func KindFromSides(a, b, c float64) Kind {

	return "NaT"
}

// Notice KindFromSides() returns this type. Pick a suitable data type.
type Kind struct {
	a int
	b int
	c int
}

// Pick values for the following identifiers used by the test program.
// NaT // not a triangle
// Equ // equilateral
// Iso // isosceles
// Sca // scalene

// Organize your code for readability.