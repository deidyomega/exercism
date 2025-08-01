package erratum

import "fmt"

const testVersion = 2

func Use(opener func() (Resource, error), str string) error {
	res, err := opener()

	if err != nil {
		fmt.Println(err.Error)
	}
	fmt.Println(res)

	return nil
}