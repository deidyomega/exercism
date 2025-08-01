package hamming

import "errors"

const testVersion = 6

func Distance(dna1_s, dna2_s string) (int, error) {
	dna1 := []rune(dna1_s)
	dna2 := []rune(dna2_s)
	var count int
	length := len(dna1)

	if length != len(dna2) {
		return -1, errors.New("Length must be identical")
	}

	for i := 0; i < length; i++ {
		if dna1[i] != dna2[i] {
			count++
		}
	}
	return count, nil
}