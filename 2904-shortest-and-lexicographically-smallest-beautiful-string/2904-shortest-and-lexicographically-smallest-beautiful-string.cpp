class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();
        int l = 0, count1 = 0;
        string ans = "";

        for (int r = 0; r < n; r++) {
            if (s[r] == '1') count1++;

            while (count1 == k) {
                string sub = s.substr(l, r - l + 1);
                if (ans.empty() || sub.size() < ans.size() || (sub.size() == ans.size() && sub < ans)) {
                    ans = sub;
                }
                if (s[l] == '1') count1--;
                l++;
            }
        }
        return ans;
    }
};