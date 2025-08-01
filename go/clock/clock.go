package clock

import (
	"fmt"
)

const testVersion = 4

// Clock structure
type Clock struct {
	hour   int
	minute int
}

// New Generates a new clock, given hours and minutes
func New(hour, minute int) Clock {
	return Clock{hour: 0, minute: 0}.Add(hour*60 + minute)
}

// String Returns string of clock
func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.hour, c.minute)
}

// Add adds n minutes to given clock
func (c Clock) Add(minutes int) Clock {
	// Get total minutes
	minutes += c.minute + c.hour*60

	// While minutes is less than 0, add another day
	// This allows us to preserve time, but use positives
	for minutes < 0 {
		minutes += 24 * 60
	}

	// Get the minute hand
	c.minute = minutes % 60

	// Remove minutes already shown on minute hand
	// Divide by 60 to convert remainder into hours (should be int)
	// modulate by 24 hours
	c.hour = (minutes - c.minute) / 60 % 24

	return c
}