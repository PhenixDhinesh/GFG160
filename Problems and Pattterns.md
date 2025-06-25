## 🧮 Basic Array Traversal

### Array/largest_second.py (Value Tracking)
* **My Pattern:** Manual tracking using conditionals
* **How I Should’ve Thought:** Recognize as standard max & second max tracking in one pass

---

## ⚙️ Greedy

### Array/majority_element_||.py (Frequency & Voting)
* **My Pattern:** Frequency map with sorting and threshold check
* **How I Should’ve Thought:** Use Moore’s Voting (extended) — at most 2 elements can have > n/3 votes

### Array/stock_buy_sell_multi_allowed.py (Profit Tracking)
* **My Pattern:** Used two pointers to track increasing segments
* **How I Should’ve Thought:** Accumulate adjacent gains greedily using simple diff check

### Array/stock_buy_sell_single_trade.py (Profit Tracking)
* **My Pattern:** Tracked peaks and valleys with multiple condition checks
* **How I Should’ve Thought:** Just track min-so-far and compute max profit at each step

### Array/Array/min_difference_btw_towers_||.py (Partition-Based Greedy)
* **My Pattern:** Tried edge-based greedy and assumed O(n), missed partition logic
* **How I Should’ve Thought:** Sort array, then for each index `i`, apply `+k` to left, `-k` to right; track min/max using boundary elements only (i.e., partition-based greedy)

---

## 🧭 Two Pointers

### Array/move_all_zeros_to_end.py (In-place Rearrangement)
* **My Pattern:** Used `pop(i)` and `append()` inside a loop — caused O(n²)
* **How I Should’ve Thought:** Apply fast/slow pointer to shift non-zero elements forward in-place

### Array/reverse_array.py (In-place Reversal)
* **My Pattern:** Used opposite-end pointers with in-place swap
* **How I Should’ve Thought:** Already optimal — standard two-pointer reversal

---

## 🔄 Array Manipulation

### Array/next_lexgrophical_larger_permute.py (Permutation Generation)
* **My Pattern:** Partial logic with sorting and rebuild — non-optimal structure
* **How I Should’ve Thought:** Identify pivot, swap with next greater, reverse suffix in-place

### Array/rotate_array.py (Cyclic Rotation)
* **My Pattern:** Used extra space with copied array and index shift
* **How I Should’ve Thought:** Use reversal algorithm or Juggling algorithm for in-place rotation
