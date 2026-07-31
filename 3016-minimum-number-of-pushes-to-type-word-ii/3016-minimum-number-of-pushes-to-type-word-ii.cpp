class Solution {
public:
    int minimumPushes(string word) {
        int n = word.size();
        if(n<8) return n;
        int arr[26]={0}, c=0;
        for(int i=0; i<n; i++){
            arr[word[i]-'a']++;
        }
        sort(arr, arr+26, greater<int>());
        for(int i=0; i<26; i++){
            c+=arr[i]*((i/8)+1);
        }
        return c;
    }
};