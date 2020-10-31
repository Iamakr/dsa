// There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.
// In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
// Your score is the sum of the points of the cards you have taken.
// Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

//solution
//First take points from k cards from start and after that one by one remove one card from start and take one from back ;
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int ans=INT_MIN;
        int i,currsum=0;
        for(i=0;i<k;i++){
            currsum+=cardPoints[i];
        }
        ans=currsum;
        for(i=0;i<k;i++){
            currsum=currsum+cardPoints[cardPoints.size()-i-1]-cardPoints[k-i-1];
            ans=max(ans,currsum);
        }
        return ans;
    }
};