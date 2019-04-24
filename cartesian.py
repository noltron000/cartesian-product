'''
	# this psuedocode was helpful in determining the output
	#    for the main cartesian product function

	---

	# old_collection: [[1, 2, 3], [a, b, c]]
	# new_collection: [[]]

	# for old_group in old_collection:
	# old_group = [1,2,3]
		# create empty new_collection_temp array
		# this will be used to store data from this next loop
		# for new_group in new_collection:
		# new_group = []
			# run convert_group with old_group and new_group
			# returns [[1],[2],[3]]
			# concatinates returned value with temp_new_collection array
			# temp_new_collection is now [[1],[2],[3]]
		# exit inner loop 

		# set new_collection equal to temp_new_collection
		# we can't modify a list during a loop so we do it here
		# new_collection now is [[1],[2],[3]]

	# old_group = [a,b,c]
		# create empty new_collection_temp array
		# this will be used to store data from this next loop
		# for new_group in new_collection:
		# new_group = [1]
			# run convert_group with old_group and new_group
			# returns [[1,a],[1,b],[1,c]]
			# concatinates returned value with temp_new_collection array
			# temp_new_collection is now [[1,a],[1,b],[1,c]]
		# new_group = [2]
			# run convert_group with old_group and new_group
			# returns [[2,a],[2,b],[2,c]]
			# concatinates returned value with temp_new_collection array
			# temp_new_collection is now [[1,a],[1,b],[1,c],[2,a],[2,b],[2,c]]
		# new_group = [3]
			# run convert_group with old_group and new_group
			# returns [[3,a],[3,b],[3,c]]
			# concatinates returned value with temp_new_collection array
			# temp_new_collection is now [[1,a],[1,b],[1,c],[2,a],[2,b],[2,c],[3,a],[3,b],[3,c]]
		# exit inner loop

		# set new_collection equal to temp_new_collection
		# we can't modify a list during a loop so we do it here
		# new_collection now is [[1,a],[1,b],[1,c],[2,a],[2,b],[2,c],[3,a],[3,b],[3,c]]
	# exit outter loop

	# the loop exponentially increases in size as we go
	# this means it is a heavy performance factor

	===

	# this psuedocode was helpful in determining the output
	# it was originally going to be a helper function
	# but was integrated into one piece later:

	---

	def convert_group(old_group, new_group)
	# input: [x, y, z], [a, 1]
	# output: [[a, 1, x], [a, 1, y], [a, 1, z]]
	# create an empty base array.

	# for each item in the given old group:
		# create a new array equal to the given new group.
		# append the item to the new array.
		# append this new array to the base array.

	# return the filled base array.
'''

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
	print(new_collection)
	return new_collection

result = cartesian_product([['a','b','c'],[1,2,3],['x','y','z']])
