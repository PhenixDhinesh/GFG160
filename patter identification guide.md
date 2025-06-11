### The 4-Step Framework for Pattern Identification

When you first read a problem, run it through this process:

#### Step 1: Deeply Understand the Problem (The \"What\")

Don't just skim it. Force yourself to slow down and answer these questions. **Do not skip this step.**

1.  **What are the inputs?**
    *   Data type: Array, string, matrix, tree, graph?
    *   Data properties: Is it sorted? Are there duplicates? Are the numbers positive/negative?
    *   Example: \"Given a **sorted array** of **unique integers**...\"

2.  **What is the exact output required?**
    *   A number (length, count, max value)?
    *   A boolean (`true`/`false`)?
    *   A new collection (a list of pairs)?
    *   The same collection, but modified **in-place**?

3.  **Manually Solve an Example:** Take the example given in the problem and solve it by hand on a piece of paper or whiteboard. Talk yourself through your own logic. How did *your brain* solve it? This often reveals a natural, albeit sometimes inefficient, algorithm.
    *   *Example: For `[0, 1, 0, 3, 12]`, you might think: \"Okay, first is a zero. I'll mentally put it aside. Next is a one. Keep it. Next is a zero, put it aside. Next is a three, keep it...\" You are naturally partitioning the array into two groups.*

#### Step 2: Analyze Constraints and Complexity (The \"How Fast\")

The constraints aren't just details; they are massive clues about the required time and space complexity, which in turn points to specific patterns.

1.  **Look at the Input Size (N):**
    *   **N <= 25:** This screams **exponential complexity**. The solution is likely **recursion with backtracking**. (e.g., generating all permutations/subsets).
    *   **N <= 1,000:** An **O(N²)** solution is likely acceptable. This means nested loops are okay. (e.g., a simple brute-force pair search).
    *   **N <= 100,000:** You need an **O(N log N)** or **O(N)** solution.
        *   `O(N log N)` suggests sorting is part of the solution.
        *   `O(N)` suggests a single-pass algorithm. This is the home of **Two Pointers, Sliding Window, and Hash Maps**.
    *   **N > 1,000,000:** You need a **O(N)** or **O(log N)** solution.
        *   `O(N)` means a single pass is a must.
        *   `O(log N)` is almost always **Binary Search**.

2.  **Look at Memory Constraints:**
    *   \"Modify the input in-place\": This is a huge flag for **O(1) space complexity**. Patterns like **Two Pointers** or reversing sub-arrays are prime candidates.
    *   No explicit constraint? You can probably use extra data structures like a **Hash Map** or **Set** to optimize time.

#### Step 3: Hunt for Keywords and Data Structure Signals (The \"Pattern Trigger\")

Your brain should have a mapping of keywords to patterns.

| If you see...                                       | Your first thought should be...                               |
| ---------------------------------------------------- | ------------------------------------------------------------- |
| **Sorted** array/list                                | **Binary Search**, **Two Pointers (Opposite Ends)**             |
| **In-place** modification, partitioning, segregation | **Two Pointers (Fast/Slow)**                                  |
| **Contiguous subarray/substring** with a property    | **Sliding Window**                                            |
| \"Shortest/Longest/Max/Min **subarray/substring**\"    | **Sliding Window**, **Prefix Sum**, **Dynamic Programming**   |
| \"Top K elements\", \"Most frequent K\", \"Median\"        | **Heaps (Priority Queue)**                                    |
| Finding pairs that sum to a target (in an unsorted array) | **Hash Map**                                                  |
| \"All possible ways\", \"all permutations/subsets\"      | **Backtracking (Recursion)**                                  |
| \"Shortest path\", \"level-by-level\"                    | **Breadth-First Search (BFS)**                                |
| \"Find if a path exists\", \"traverse a maze\"           | **Depth-First Search (DFS)**, **Union-Find**                  |
| \"Prefix\" or \"Suffix\" operations on strings         | **Trie**, **Prefix Sum**                                      |
| \"Minimum cost\", \"Maximum profit\", \"Number of ways to do X\" | **Dynamic Programming (DP)**, sometimes **Greedy**            |
| A decision at each step seems to affect future choices | **Greedy**, **Dynamic Programming**                           |

#### Step 4: Formulate a Brute-Force Solution (The \"Baseline\")

Always think of the simplest, most obvious (even if slow) way to solve the problem.
*   **Why?** It proves you understand the problem, and it's a starting point for optimization.
*   **Example (Two Sum):** \"Find two numbers that add to a target.\"
    1.  **Brute Force:** Use two nested loops to check every possible pair. `O(N²)`.
    2.  **Analyze & Optimize:** The constraints say N is 10⁵, so `O(N²)` is too slow. How can I optimize the inner loop? The inner loop is just searching for a value (`target - current_number`). What data structure is good at fast lookups? **A Hash Map!**
    3.  **Optimal Solution:** Iterate once, storing elements in a hash map. For each element, check if its complement (`target - num`) is already in the map. This is `O(N)`.

By starting with brute force, you naturally walk toward the optimal pattern.

---

### A Practical Example: \"Find the longest substring with no repeating characters\"

1.  **Step 1 (Understand):**
    *   Input: A string `s`.
    *   Output: A number (the length of the longest substring).
    *   Manual Example: `s = \"abcabcbb\"`.
        *   `a` -> 1
        *   `ab` -> 2
        *   `abc` -> 3
        *   `abca` -> Oops, 'a' repeats. The substring was `abc` (length 3). Start over from `b`.
        *   `bca` -> 3
        *   `bcab` -> Oops, 'b' repeats. The substring was `bca` (length 3). Start over from `c`.
        *   ... and so on. The max I found was 3.

2.  **Step 2 (Constraints):**
    *   `s.length` can be up to 5 * 10⁴. This means `O(N²)`, my manual approach, is too slow. I need `O(N)`.

3.  **Step 3 (Keywords):**
    *   \"**substring**\" -> This is a contiguous block. Major signal for **Sliding Window**.
    *   \"no repeating characters\" -> I need a way to track the characters currently in my substring. A **Hash Set** or **Hash Map** would be perfect for O(1) add/remove/check operations.

4.  **Step 4 (Connect and Formulate):**
    *   The `O(N)` requirement and \"substring\" keyword strongly point to **Sliding Window**.
    *   The \"no repeating characters\" requirement points to using a **Hash Set** to maintain the characters in the current window.
    *   **The Algorithm:** I'll use two pointers, `left` and `right`, to define my window. I'll expand the window by moving `right`. If I encounter a character that's already in my hash set, I'll shrink the window from the `left` until the duplicate is gone. I'll keep track of the maximum window size seen. This is the classic sliding window pattern.

By following this structured approach, you move from being overwhelmed to being a detective, systematically uncovering the clues that lead you to the right pattern.
