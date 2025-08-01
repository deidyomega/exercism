package diffsquares

import (
	"math"
)

const testVersion = 1

func SumOfSquares(num int) int {
	number := float64(num)
	var count float64
	var index float64
	for index = 1; index <= number; index++ {
		count += math.Pow(index, 2)
	}
	return int(count)
}

func SquareOfSums(num int) int {
	count := 0
	for index := 1; index <= num; index++ {
		count += index
	}

	return int(math.Pow(float64(count), 2))
}

func Difference(number int) int {
	return SquareOfSums(number) - SumOfSquares(number)
}