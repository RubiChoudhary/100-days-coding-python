def duplicates(self, arr, n): 
    	# code here
	    unique_list = []
        duplicate_list = []

        for i in arr:
            if i not in unique_list:
                unique_list.append(i)
            elif i not in duplicate_list:
                duplicate_list.append(i)

        return duplicate_list
