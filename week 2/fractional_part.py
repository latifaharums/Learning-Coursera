#requirements
#fractional part is between 0 and 1
#0 produces error

#Create func
def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
# keep just the fractional part of the quotient
	if denominator > 0:
		return (numerator%denominator)/denominator
	return 0

#Print value
print(fractional_part(5, 5)) # Should print 0
print(fractional_part(5, 4)) # Should print 0.25
print(fractional_part(5, 3)) # Should print 0.66...
print(fractional_part(5, 2)) # Should print 0.5
print(fractional_part(5, 0)) # Should print 0
print(fractional_part(0, 5)) # Should print 0