s1 = "amansaxena"

s2 = "ytyasaxenaman"

def longest_substring(s1,s2):

    if len(s1) >= len(s2):
        longer_string = s1
        shorter_string = s2
    else:
         shorter_string = s1
         longer_string = s2
         
    for max_length in range(len(shorter_string),0,-1):
        starting_positions = [x for x in range(0,len(shorter_string)-max_length+1)]
        substrings = [shorter_string[x:x+max_length] for x in starting_positions]
        for x in substrings:
            if x in longer_string:
                return(x)

print(longest_substring(s1,s2))