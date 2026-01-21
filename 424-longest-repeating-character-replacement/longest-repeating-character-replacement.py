class Solution(object):
    def characterReplacement(self, s, k):
        n=len(s)
        left,right=0,0
        maxLen=0
        maxFreq=0
        mpp={}
        while(right<n):
            if(s[right] in mpp):
                mpp[s[right]]+=1
            else:
                mpp[s[right]]=1
            maxFreq=max(maxFreq,mpp[s[right]])
            while(right-left+1 - maxFreq >k):
                mpp[s[left]]-=1
                if(mpp[s[left]]==0):
                    del mpp[s[left]]
                left+=1
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen