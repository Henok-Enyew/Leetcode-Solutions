#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <regex>
#include <cctype>

using namespace std;

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> bannedSet(banned.begin(), banned.end());
        
        transform(paragraph.begin(), paragraph.end(), paragraph.begin(), ::tolower);
        regex word_regex(R"([a-z]+)");
        sregex_iterator iter(paragraph.begin(), paragraph.end(), word_regex);
        sregex_iterator end;

        unordered_map<string, int> wordCount;

        while (iter != end) {
            string word = iter->str();
            if (bannedSet.find(word) == bannedSet.end()) {
                wordCount[word]++;
            }
            ++iter;
        }

        string answer;
        int maxCount = 0;
        for (const auto& entry : wordCount) {
            if (entry.second > maxCount) {
                maxCount = entry.second;
                answer = entry.first;
            }
        }

        return answer;
    }
};
