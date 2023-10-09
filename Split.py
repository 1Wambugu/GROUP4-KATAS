def solution(S):
    #split the string to words
    split_string =S.split()
    # print(split_string)

    #variable to hold reversed string
    reversed_string= ""

    #for loop and slice()to reverse split_string
    for i in split_string:
        reversed_string= i[::-1]
        print(reversed_string, end=" ")
    
    return str()

print(solution("we test coders"))