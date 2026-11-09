# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduced binary search trees and recursive tree operations. I implemented an employee-directory example that stored unique employee identification numbers in a BST.

## Implementation

I completed the starter's `Node` and `BST` classes while retaining every TODO prompt. Each node stored a value plus references to its left and right children. Recursive insertion placed smaller IDs in the left subtree and larger IDs in the right subtree. Duplicate IDs were ignored so each employee ID appeared once. Recursive search compared the target with the current node and followed only the possible subtree. In-order traversal visited the left subtree, current node, and right subtree, producing IDs in ascending order.

The demonstration inserted seven IDs in an order that created both left and right branches. It searched for two existing IDs and two missing IDs and displayed the sorted traversal.

## Edge Cases and Tree Shape

The program traversed and searched an empty tree, ignored a duplicate ID, and traversed a single-node tree. I also inserted sequential IDs into a separate tree to demonstrate a right-skewed shape. That tree remained correct, but its height grew linearly and reduced search efficiency.

## Performance and Real-World Use

Insertion and search took O(h) time, where h was the tree height. In a reasonably balanced BST, h was approximately log n, allowing each comparison to discard a subtree. In a skewed BST, h could become n, making operations O(n), similar to a linked list. In-order traversal always took O(n) because it visited every node. The tree used O(n) storage plus recursive call-stack space proportional to its height.

Employee directories, ordered account identifiers, and inventory indexes can use tree structures when applications need both searching and sorted traversal. A self-balancing tree would protect production software from inefficient insertion orders.

## Running the Program

From the repository root, I ran:

```bash
python3 unit4_trees/unit4_discussion.py
```

No external packages were required.

## Discussion Board Reflection

I learned how recursive insertion, searching, and in-order traversal worked together in a binary search tree. I used employee identification numbers because their natural ordering clearly showed why smaller values moved left and larger values moved right. My main challenge was making every recursive method return the correct result to its caller. Returning the updated node during insertion reconnected each subtree, while returning the recursive Boolean result allowed a search to travel back through the call stack. A reasonably balanced BST improved searching because each comparison discarded either the left or right subtree, producing approximately O(log n) search time instead of scanning every record. However, that advantage depended on tree shape. Sequential insertion created a one-sided tree whose height approached the number of nodes, reducing insertion and search to O(n), much like a linked list. I handled empty trees, duplicate values, a single-node tree, missing IDs, and a deliberately skewed tree. The exercise showed that a BST preserves sorted organization and can search efficiently, but production software may need a self-balancing implementation to prevent input order from damaging performance.

## Original Assignment Requirements

All instructor TODO prompts remained visible in `unit4_discussion.py`. The completed program inserted values recursively, searched recursively, returned a sorted in-order traversal, tested existing and missing values, demonstrated multiple edge cases and tree shapes, and documented a real-world employee-directory scenario.
