package gigasecond

// import path for the time package from the standard library
import "time"

const testVersion = 4

func AddGigasecond(value time.Time) time.Time {
	return value.Add(time.Second * time.Duration(1000000000))
}