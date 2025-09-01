# 🚀 LeetCode Solutions

A collection of my solutions to **LeetCode problems**, organized by topics and difficulty.  
This repository documents my **DSA learning journey** while preparing for coding interviews.  

---

## 📂 Repository Structure
- 📦 DSA-LeetCode-Solutions
- ┣ 📂 Arrays → Problems related to arrays
- ┣ 📂 Linked List → Linked List problems  
- ┣ 📂 Sliding Window → Problems using Sliding Window technique  
- ┣ 📂 Strings → String manipulation problems  
- ┣ 📂 Dynamic Programming → DP problems 
- ┣ 📂 Graphs → Graph-related problems  
- ┣ 📜 README.md

---

## 🌟 Example Solution

**Problem:** [Two Sum](https://leetcode.com/problems/two-sum/)  
**Difficulty:** Easy  
**Approach:** HashMap / One-pass  

```python
# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Pattern: Hashing / One-pass

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Map:
                return [Map[diff], i]
            Map[n] = i
        return
```
---

## 🛠️ Tech Stack
- **Language**: Python 
- **Platform**: [LeetCode](https://leetcode.com/)  
- **Version Control**: Git + GitHub  

---

## 🎯 Goals
- Cover all major patterns (**Arrays, Strings, DP, Graphs, Trees**).  
- Build strong **DSA foundations** for placements & interviews.  

---

## 🤝 Contributing
This repo is part of my **personal coding journey**.  
Feel free to **fork** and try out the problems yourself! 🚀  

---

✨ “Code every day, grow every day.”