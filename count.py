#to count the occurance of word in string

def word_count(str):    #function defination
       count=dict()        #inbuilt dict() to maintain key:value pair
       w=str.split()
       print(w)
       for a in w:
              if a in count:
                     count[a]+=1
              else:
                     count[a]=1
       return count
c=word_count('we are are in in the sql lab we are')   #function call
print(c)



#output
#['we', 'are', 'are', 'in', 'in', 'the', 'sql', 'lab', 'we', 'are']
#{'the': 1, 'in': 2, 'lab': 1, 'are': 3, 'we': 2, 'sql': 1}
