from botLogic import BOT
FILENAME="question.csv"

n="why should we eat rice"


#get data ready
filedata=BOT.get_file_data(FILENAME)
datakey=BOT.get_file_data_key2(filedata)

#after comment 
comment_key=BOT.find_keyword(n)
def count_Similer()
    maxvalue=1
    maxindex=0
    for i in range(0,len(datakey)):
        counthai=BOT.common_member(datakey[i],comment_key)
        if 1 < len(counthai):
            maxindex=i
            maxvalue=len(counthai)
        print(counthai)
    return maxindex,maxvalue

def predict(maxindex,maxvalue):
    if maxvalue!=1:
        return(filedata[maxindex][1])
    else:
        return("SORRY: i can't find question relead to your query")




    
#questions
print("-"*40)
print("QUERY: ",n)
if maxvalue!=1:
    print("QUESTION: ",filedata[maxindex][0])
    print("ANSWER: ",filedata[maxindex][1])
else:
    print("SORRY: i can't find question relead to your query")

#answer
# print("ANSWER: ",filedata[maxindex][1])
print("-"*40)


