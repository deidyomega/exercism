package erratum

const testVersion = 2

func Use(opener ResourceOpener, input string) (err error) {
	resource, err := opener()
	for err != nil {
		// This asks if the error's type is TransientError
		// if it is (ok), then contiune,
		// else, return the error
		if _, ok := err.(TransientError); ok {
			resource, err = opener()
		} else {
			return err
		}
	}

	// This basically is golangs try.  We defer the close to the end,
	// if everything blows up, this still runs
	defer resource.Close()

	defer func() {
		// This recovers from the resource.Frob(input)
		if recoverStatus := recover(); recoverStatus != nil {
			// If it's a FrobError, .Defrob the resource
			// using the frobErrs defrobtag
			if frobErr, ok := recoverStatus.(FrobError); ok {
				resource.Defrob(frobErr.defrobTag)
			}
			// Either way, set the err to the recoveries error
			err = recoverStatus.(error)
		}
	}()

	// While the two funcs above were defined first
	// This executes, and depending on what happens
	// the two above are ran
	resource.Frob(input)

	if err != nil {
		return err
	}

	// if by Gods green earth we make it this far without a return
	// then there is no error, and we can just return nil
	return nil
}