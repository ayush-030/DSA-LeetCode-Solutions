# 🚀 LeetCode Solutions

A collection of my solutions to **LeetCode problems**, organized by topics and difficulty.  
This repository documents my **DSA learning journey** while preparing for coding interviews.  

---

## 📂 Repository Structure
📦 leetcode-solutions

┣ 📂 arrays

┃ ┣ 📜 two_sum.py

┣ 📂 strings

┣ 📂 linked_list

┣ 📂 dynamic_programming

┣ 📂 graphs

┣ 📜 README.md

- **arrays/** → Problems related to arrays  
- **strings/** → String manipulation problems  
- **linked_list/** → Linked List problems  
- **dynamic_programming/** → DP problems  
- **graphs/** → Graph-related problems  

---

## Example Solution

**Problem:** [Two Sum](https://leetcode.com/problems/two-sum/)  
**Difficulty:** Easy  
**Approach:** HashMap / Dictionary  

### Python

# Problem: Two Sum
# Difficulty: Easy
# Approach: HashMap / Dictionary
# Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

---

## 🛠️ Tech Stack
- **Language**: Python 🐍  
- **Platform**: [LeetCode](https://leetcode.com/)  
- **Version Control**: Git + GitHub  

---

## 🎯 Goals
- Solve **at least 1 problem daily** (or batch on weekends).  
- Cover all major patterns (**Arrays, Strings, DP, Graphs, Trees**).  
- Build strong **DSA foundations** for placements & interviews.  

---

## 🤝 Contributing
This repo is part of my **personal coding journey**.  
Feel free to **fork** and try out the problems yourself! 🚀  

---

## ✨ “Code every day, grow every day.”