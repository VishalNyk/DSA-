class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        if (n <= 2) return n;

        int mx = 0;

        for (int i = 0; i < n; i++) {
            unordered_map<double, int> mp;
            
            for (int j = i + 1; j < n; j++) {
                double slope;
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx == 0) {
                    slope = numeric_limits<double>::infinity(); // Handle vertical line
                } else {
                    slope = (double)dy / dx;
                    if (slope == -0.0) slope = 0.0; // Fix -0.0 vs 0.0 hash map key bug
                }

                mp[slope]++;
                mx = max(mx, mp[slope] + 1); // +1 includes the anchor point i
            }
        }

        return mx;
    }
};