s1 = "amansaxena"

s2 = "ytyasaxenaman"

def longest_substring(s1,s2):
    for max_length in range(len(s2),0,-1):
        starting_positions = [x for x in range(0,len(s2)-max_length+1)]
        substrings = [s2[x:x+max_length] for x in starting_positions]
        for x in substrings:
            if x in s1:
                return(x)

print(longest_substring(s1,s2))