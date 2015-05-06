states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'Illinois' : 'IL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

cities = {
	'CA' : 'Sacramento',
	'IL' : 'Springfield',
	'FL' : 'Jacksonville'
}

cities['MI'] = 'Lansing'
cities['OR'] = 'Salem'
cities['NY'] = 'Albany'

print '-'*10
print "IL State has: ", cities['IL']
print "OR State has: ", cities['OR']

print '*'*10
print "Michigan has %r for short." %states['Michigan']
print "Illinois has %r for short." %states['Illinois']

print '~'*10
print 'Florida has ', cities[states['Florida']]
print 'California has ', cities[states['California']]

print '+'*10
for state, abbrev in states.items():
	print "%s is short for %s" %(abbrev, state)

print '+'*10
for abbrev, city in cities.items():
	print "%s has the city of %s" %(abbrev, city)

print '+'*10
for state, abbrev in states.items():
	print "%s is short for %s State, which has the city of %s" %(
		abbrev, state, cities[abbrev])
