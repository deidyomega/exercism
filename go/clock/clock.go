package clock

import (
	"fmt"
	"math"
)

const testVersion = 4

// Clock structure
type Clock struct {
	hour   int
	minute int
}

// New Generates a new clock, given hours and minutes
func (Clock) New(hour, minute int) Clock {
	hour += int(math.Floor(float64(minute / 60)))
	finalMinute := minute % 60
	finalHour := hour % 24
	return Clock{hour: finalHour, minute: finalMinute}
}

// String Returns string of clock
func (c *Clock) String() string {
	return fmt.Sprintf("%01d:%01d", c.hour, c.minute)
}

// Add adds n minutes to given clock
func (c *Clock) Add(minutes int) Clock {
	// This instages a new clock, so our return isn't messed up
	clock := Clock{hour: c.hour, minute: c.minute}
	if minutes == 0 {
		return clock
	}

	return clock
}