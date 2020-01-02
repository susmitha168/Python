test_str = "Good Morning"

print("The Original String  " + str(test_str))

sub_str = [test_str[i: j] for i in range(len(test_str)) for j in (i+1,len(test_str)+1)]

print("The substrings are  " + str(sub_str))
