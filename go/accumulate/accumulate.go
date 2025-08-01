package accumulate

const testVersion = 1

func Accumulate(input_set []string, function func(string) string) []string {
	for index := 0; index < len(input_set); index++ {
		input_set[index] = function(input_set[index])
	}
	return input_set
}