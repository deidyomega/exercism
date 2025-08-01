package hamming

import "errors"

const testVersion = 6

func Distance(dna1, dna2 string) (int, error) {
	var count int
	length := len(dna1) // cache this, so we don't have to redetermine every loop

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