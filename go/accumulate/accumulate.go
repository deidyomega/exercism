package accumulate

const testVersion = 1

func Accumulate(input []string, function func(string) string) []string {
	for index := 0; index < len(input); index++ {
		input[index] = function(input[index])
	}
	return input
}