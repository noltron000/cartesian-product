def cartesian_product(array):
	'''
	Vocabulary:
	- a collection is an array of arrays
	- a group is an array within a collection
	- old is the user's input
	- new is the transformed output
	- tmp is data not added to new for technical reasons

	Variable Names:
	- old_collection is the user's input
	- old_group is a nested array in old_collection
	- new_collection is the expected output
	- new_group is a nested array in new_collection
	- tmp_collection is data not yet added to new_collection
	- tmp_group is data not yet added to tmp_collection
	'''

	# new_collection starts as an empty array
	# old_collection equals the input array parameter
	new_collection = [[]]
	old_collection = array

	# start by iterating over the groups in old_collection
	for old_group in old_collection:

		# new_collection can't be modified while in a loop
		# tmp_collection will store a subset of new data
		# it will be added to new_collection after the next loop
		tmp_collection = []

		# iterate over new_collections
		# it will start with just an array with one empty array
		# every time we go through another old_group it fills up
		for new_group in new_collection:

			# finally, look through the data in old_group
			# this data is important;
			#    its what we need to transfer to the new structure
			for data in old_group:

				# new_group contains a set of important data
				# there is still yet more data to append to it...
				# ...set tmp_group to new_group and add data to it
				tmp_group = new_group.copy()
				tmp_group.append(data)

				# now transfer the data to our tmp_collection
				# it will be added to the new_collection to output
				tmp_collection.append(tmp_group)

			# exit old_group loop
			pass

		# exit new_collection loop
		pass

		# an item can't be changed while being looped over;
		#    we are no longer looping over new_collection
		new_collection = tmp_collection

	# exit old_collection loop
	pass

	# after the loops are over, we can return the result
	return new_collection

if __name__ == '__main__':
	# this part is just calling the function as an example
	X={'X'}
	Y={'Y'}
	Z={'Z'}

	simple_array = [[1,2,3],['a','b','c'],[X,Y,Z]]
	result = cartesian_product(simple_array)

	for group in result:
		print(group)
