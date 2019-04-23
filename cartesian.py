def cartesian_product(old_collection)
	# this psuedocode was  helpful in determining the output
	'''
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
	'''
	# the loop exponentially increases in size as we go
	# this means it is a heavy performance factor
	pass

def convert_group(old_group, new_group)
	# this psuedocode was  helpful in determining the output
	'''
	# input: [x, y, z], [a, 1]
	# output: [[a, 1, x], [a, 1, y], [a, 1, z]]
	# create an empty base array.

	# for each item in the given old group:
		# create a new array equal to the given new group.
		# append the item to the new array.
		# append this new array to the base array.

	# return the filled base array.
	'''
	pass
