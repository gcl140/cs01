def fetch_evens(alist):
	for i in range(0, len(alist)):
		if alist[i] % 2 == 0:
			print(alist[i])

def fetch_even_positions(alist):
	for i in range(0, len(alist)):
		if i % 2 == 0:
			print(alist[i])
			
def plug_in(alist, n):
	for i in range(len(alist)):
		# if alist[i] >= n:
		print(n, alist[i])
		if n < alist[i]:
			alist.insert(i, n)
			return alist
		
	alist.append(n)
	return alist
	
# def check_sort(alist):
# 	for i in range(len(alist) - 1):
# 		if alist[i] < alist[i+1] or alist[i] > alist[i+1]:
# 			return True

def check_sort(glist):
    if len(glist) < 2:
        return True  # a 0- or 1-element list is trivially sorted

    increasing = True
    decreasing = True

    for i in range(len(glist) - 1):
        if glist[i] < glist[i + 1]:
            decreasing = False
        elif glist[i] > glist[i + 1]:
            increasing = False

    return increasing or decreasing # remember math or physics


		# if alist[i] != len(alist):
			# print(alist[i], len(alist))
			# print(alist[i], alist[i + 1])

# glist = [1, 2, 4, 5, 12, 20, 81]
# glist = [1, 2, 4, 5, 12, 81, 31]
# glist = [81, 72, 64, 55, 42, 30, 21]
# fetch_evens(glist)
# fetch_even_positions(glist)
# print(plug_in(glist, 13))

# glist = [1, 2, 4, 5, 12, 81, 31]
def compare_functions(alist1, alist2):
	if len(alist1) != len(alist2):
		return False
    
	i = 0
	j = len(alist2) - 1
	while i < len(alist1):
		print(alist1[i], alist2[j])
		print(i, j, "positons")
		if alist1[i] != alist2[j]:
			return False
		i += 1
		j -= 1
    
glist1 = [1, 2, 4, 5, 12, 1, 31]
glist2 = [31, 81, 12, 5, 4, 2, 1]

# print(compare_functions(glist1, glist2))
print("-----")


	
def ml_pie(n):
    i = 1
    result = 0
    call = 0
    while i <= n:
        if i % 2 != 0:  # only odd denominators
            if call % 2 == 0:
                result += 1 / i   # + for even index
            else:
                result -= 1 / i   # - for odd index
            call += 1
        i += 1
    return 4 * result  # multiply by 4 to approximate π

print(ml_pie(6))

# print(ml_pie(3))