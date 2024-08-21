class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        store ={}
        answer = ''
        i = 0
        for k in key :
            if k != ' ' and k not in store:
                store[k] = i
                i+=1
        for i in range(len(message)):
            if message[i] == ' ':
                answer += ' '
            else:
                answer += chr(store[message[i]] + 97) 
        return answer
