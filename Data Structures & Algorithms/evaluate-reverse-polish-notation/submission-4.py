class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st= []
        for i in tokens:
            if i =="+":
                a1= st.pop()
                a2= st.pop()
                st.append(a1+a2)
            elif i =="-":
                a1= st.pop()
                a2= st.pop()
                st.append(a2-a1)
            elif i =="*":
                a1= st.pop()
                a2= st.pop()
                st.append(a1*a2)
            elif i =="/":
                a1= st.pop()
                a2= st.pop()
                st.append(int(a2/a1))
            else:
                st.append(int(i))
        return st.pop()
            

        
        


        