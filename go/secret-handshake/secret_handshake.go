package secret

import (
	"fmt"
	"strconv"
)

const testVersion = 2

// 1 = wink
// 10 = double blink
// 100 = close your eyes
// 1000 = jump
// 10000 = Reverse the order of the operations in the secret handshake.

func Handshake(code uint) (action []string) {

	// This gives you the string of the binary of the code...
	bin := fmt.Sprintf(strconv.FormatInt(int64(code), 2))

	fmt.Println("PRINTING")
	fmt.Println(bin)

	return []string{}
}