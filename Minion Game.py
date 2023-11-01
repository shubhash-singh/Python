def minion_game(string):
    consonant = "bcdfghjklmnpqrstvwxyz"
    count=0
    sub_string=""
    for i in string:
        for j in consonant:
            if i==j.upper():
                count+=1
                sub_string+=i
                print(sub_string)
                
        print(sub_string)
        
        
        
    print(f"Stuart {count}")
                

if __name__ == '__main__':
    s = input()
    minion_game(s)