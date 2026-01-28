# Sorting Algorithms Cheatsheet

## Quick Reference Table

| Algorithm      | Best       | Average    | Worst      | Space | Stable | Adaptive | In-Place |
| -------------- | ---------- | ---------- | ---------- | ----- | ------ | -------- | -------- |
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)  | Yes    | Yes      | Yes      |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)  | Yes    | Yes      | Yes      |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)  | No     | No       | Yes      |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)  | Yes    | No       | No       |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(1)  | No     | No       | Yes      |
| Timsort        | O(n)       | O(n log n) | O(n log n) | O(n)  | Yes    | Yes      | No       |

### Key Terms

- **Stable**: Equal elements keep their original relative order
- **Adaptive**: Runs faster on partially sorted input
- **In-Place**: Uses O(1) extra memory (not counting recursion stack)

---

## 1. Bubble Sort

### Mental Model

**Bubbles rise.** Larger values "bubble up" to the end with each pass.

### Analogy

Heaviest balls sink to the bottom of a tube of water. Each pass, the heaviest unsorted element floats to its final position.

### How It Works

1. Walk through the array comparing **adjacent pairs**
2. If left > right, **swap them**
3. After one pass, the **largest element is at the end**
4. Repeat, ignoring the last (already sorted) positions
5. Stop when a pass makes **zero swaps**

### Visual Trace

```
[5, 3, 8, 1]

Pass 1: 5>3 swap → [3, 5, 8, 1] → 5<8 ok → 8>1 swap → [3, 5, 1, 8]
                                                                    ↑ 8 placed

Pass 2: 3<5 ok → 5>1 swap → [3, 1, 5, 8]
                                    ↑ 5 placed

Pass 3: 3>1 swap → [1, 3, 5, 8]
                        ↑ 3 placed. No swaps needed → done.
```

### The Invariant

> After k passes, the last k elements are sorted and in their final positions.

### Code Pattern

```python
swapping = True
end = len(arr)
while swapping:
    swapping = False
    for i in range(1, end):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            swapping = True
    end -= 1
```

### When to Use

Almost never. Educational purposes only. Insertion sort is better in every practical scenario.

---

## 2. Insertion Sort

### Mental Model

**Sorting cards in your hand.** Pick up one card at a time, slide it into the correct position in your already-sorted hand.

### Analogy

You're dealt cards one by one. Each new card slides left through your hand until it finds its spot.

### How It Works

1. Start from the second element (index 1)
2. Compare it with elements to its left
3. Shift it left until it's in the correct position
4. The sorted region grows by one each step

### Visual Trace

```
[5, 2, 4, 6, 1, 3]
 ✓  ↑              Pick 2 → slides past 5 → [2, 5, 4, 6, 1, 3]
 ✓  ✓  ↑           Pick 4 → slides past 5 → [2, 4, 5, 6, 1, 3]
 ✓  ✓  ✓  ↑        Pick 6 → stays         → [2, 4, 5, 6, 1, 3]
 ✓  ✓  ✓  ✓  ↑     Pick 1 → slides to 0   → [1, 2, 4, 5, 6, 3]
 ✓  ✓  ✓  ✓  ✓  ↑  Pick 3 → slides to 1   → [1, 2, 3, 4, 5, 6]
```

### The Invariant

> After processing index i, elements 0 through i are sorted relative to each other.

### Code Pattern

```python
for i in range(1, len(arr)):
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
```

### When to Use

- Small arrays (< ~50 elements)
- Nearly sorted data (best case O(n))
- Online/streaming data (sort as elements arrive)
- Used inside Timsort for small runs

---

## 3. Selection Sort

### Mental Model

**Pick the smallest, place it next.** Scan the unsorted region, find the minimum, put it at the front.

### Analogy

Picking the shortest person from a lineup to stand at position 1, then the next shortest for position 2, and so on.

### How It Works

1. Find the minimum in the entire array → swap to position 0
2. Find the minimum in positions 1..end → swap to position 1
3. Repeat until done

### Visual Trace

```
[29, 10, 14, 37, 13]
 ↑                    Scan all → min is 10 → swap
[10, 29, 14, 37, 13]
  ✓  ↑                Scan rest → min is 13 → swap
[10, 13, 14, 37, 29]
  ✓   ✓  ↑            Scan rest → min is 14 → already in place
[10, 13, 14, 37, 29]
  ✓   ✓   ✓  ↑        Scan rest → min is 29 → swap
[10, 13, 14, 29, 37]  Done
```

### The Invariant

> After iteration i, the first i elements are the i smallest values in their final positions.

### Code Pattern

```python
for i in range(len(arr)):
    smallest_idx = i
    for j in range(i, len(arr)):
        if arr[j] < arr[smallest_idx]:
            smallest_idx = j
    arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]
```

### When to Use

- When **writes/swaps are expensive** (e.g., flash memory) — only O(n) swaps
- Otherwise, prefer insertion sort

---

## 4. Merge Sort

### Mental Model

**Divide and conquer.** Split in half, sort each half, merge the two sorted halves.

### Analogy

Sorting exam papers: split the pile, give each half to a helper, each helper splits again, until someone has 1 paper (already sorted). Then merge sorted piles back up — just compare the top of each pile.

### How It Works

1. **Base case**: array of 0 or 1 elements is already sorted
2. **Divide**: split array in half
3. **Recurse**: merge_sort each half
4. **Merge**: combine two sorted halves into one sorted result

### Visual Trace

```
DIVIDE                              CONQUER (merge back up)

     [38, 27, 43, 3]                   [3, 27, 38, 43]
          /    \                              ↑
   [38, 27]    [43, 3]             [27, 38]  +  [3, 43]
      / \        / \                  ↑            ↑
   [38] [27]  [43] [3]           [38]+[27]     [43]+[3]
```

### Why Merge Is Easy

When both lists are sorted, merging is a one-pass zipper:

```
Left:  [3, 27]    Right: [9, 38]

Compare 3 vs 9  → take 3     [3]
Compare 27 vs 9 → take 9     [3, 9]
Compare 27 vs 38 → take 27   [3, 9, 27]
Left empty → take 38          [3, 9, 27, 38]
```

### The Invariant

> If merge_sort correctly sorts smaller arrays, then splitting, sorting both halves, and merging them sorts the whole array. Base case (length ≤ 1) grounds the recursion.

### Code Pattern

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
```

### Time Complexity — Why O(n log n)

```
Level 0:  [████████████████]  → n work to merge
Level 1:  [████████][████████] → n work to merge
Level 2:  [████][████][████][████] → n work to merge
...
log₂(n) levels × n work per level = O(n log n)
```

### When to Use

- Need guaranteed O(n log n) worst case
- Need stability
- Linked lists (no random access needed, O(1) extra space)

---

## 5. Quick Sort

### Mental Model

**Pick a pivot, partition around it.** Everything smaller goes left, everything larger goes right. The pivot is now in its final position. Recurse on both sides.

### Analogy

Organizing a bookshelf: pick one book (pivot), put shorter books left, taller books right. That book is in its forever position. Repeat for each side.

### How It Works (Lomuto Partition)

1. Pick pivot (last element)
2. Maintain pointer `i` = boundary of "less than pivot" region
3. Scan with `j`: if `arr[j] < pivot`, grow the region, swap element in
4. Place pivot at `i + 1`
5. Recurse on left and right of pivot

### Partition Visual Trace

```
[3, 1, 4, 1, 5, 2]  pivot = 2, i starts before array
 j
 3<2? No

[3, 1, 4, 1, 5, 2]
    j
 1<2? Yes → i++, swap → [1, 3, 4, 1, 5, 2]
                          i

[1, 3, 4, 1, 5, 2]
       j
 4<2? No

[1, 3, 4, 1, 5, 2]
          j
 1<2? Yes → i++, swap → [1, 1, 4, 3, 5, 2]
                             i

[1, 1, 4, 3, 5, 2]
             j
 5<2? No

Place pivot at i+1: swap arr[2] ↔ arr[5]
[1, 1, 2, 3, 5, 4]
       ↑
    pivot in final position → return index 2
```

### The Invariant

> After each partition call, the pivot is in its final sorted position. It will never move again.

### Code Pattern

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        mid = partition(arr, low, high)
        quick_sort(arr, low, mid - 1)
        quick_sort(arr, mid + 1, high)
    return arr
```

### Time Complexity

```
Best/Average: Balanced splits → log n levels × n work = O(n log n)
Worst: Always pick min/max as pivot → n levels × n work = O(n²)
```

### When to Use

- General-purpose in-place sorting
- When average case matters more than worst case
- When stability is not required

---

## 6. Timsort & Powersort (Production)

### What Python Actually Uses

`sorted()` and `list.sort()` use **Timsort** with a **Powersort merge policy** (since Python 3.11).

### Key Idea

Real-world data has **runs** — stretches already in order. Timsort exploits them.

### How It Works

1. **Find natural runs** (ascending or descending sequences)
2. **Extend short runs** to a minimum length using **insertion sort**
3. **Merge runs** using merge sort's merge step
4. **Galloping mode**: when one run dominates during merge, switch to binary search to skip ahead
5. **Powersort merge policy** (3.11+): decides merge order to minimize total comparisons

### Why These Building Blocks?

```
Insertion Sort → handles small runs efficiently (low overhead)
Merge Sort     → combines runs stably with O(n log n) guarantee
Galloping      → skips ahead when data has structure
Powersort      → near-optimal merge ordering
```

### Why Merge Sort Over Quick Sort for Production?

| Requirement           | Merge Sort | Quick Sort |
| --------------------- | ---------- | ---------- |
| Stable                | Yes        | No         |
| Guaranteed O(n log n) | Yes        | No         |
| In-place              | No         | Yes        |

Python chose **correctness guarantees** (stability + worst case) over saving memory.

---

## Comparison by Properties

### When Each Algorithm Shines

| Scenario                       | Best Choice    | Why                              |
| ------------------------------ | -------------- | -------------------------------- |
| Small array (< 50)             | Insertion Sort | Low overhead, cache-friendly     |
| Nearly sorted                  | Insertion Sort | O(n) best case                   |
| Guaranteed performance         | Merge Sort     | Always O(n log n)                |
| Stability required             | Merge Sort     | Natural stability                |
| In-place, average case matters | Quick Sort     | O(1) space, fastest average      |
| Writes/swaps are expensive     | Selection Sort | Only O(n) swaps                  |
| Real-world production          | Timsort        | Best of all worlds               |
| Learning fundamentals          | All of them    | Each teaches a different concept |

### The Symmetry Between Merge Sort and Quick Sort

| Aspect   | Merge Sort                 | Quick Sort                    |
| -------- | -------------------------- | ----------------------------- |
| Strategy | Split first, work on merge | Work on partition, split free |
| Split    | Always middle (trivial)    | Partition (the real work)     |
| Combine  | Merge (the real work)      | Nothing (trivial)             |
| Top-down | Easy split → hard combine  | Hard split → easy combine     |

---

## Spaced Repetition Prompts

### Card 1: Invariants

**Q:** What is the invariant for each sorting algorithm?
**A:**

- **Bubble**: After k passes, last k elements are in final positions
- **Insertion**: After processing index i, elements 0..i are sorted relative to each other
- **Selection**: After iteration i, first i elements are the i smallest in final positions
- **Merge**: If it works on smaller arrays, splitting + sorting halves + merging sorts the whole
- **Quick**: After partition, the pivot is in its final position forever

### Card 2: Time Complexity

**Q:** Which O(n²) sorts have O(n) best case? Which doesn't?
**A:** Bubble and insertion sort are **adaptive** — O(n) on sorted input. Selection sort is always O(n²) because it always scans the full remaining array.

### Card 3: Stability

**Q:** Which sorts are stable?
**A:** Bubble, insertion, merge sort. Selection sort and quick sort are NOT stable.

### Card 4: The Split

**Q:** What's the fundamental difference between merge sort and quick sort?
**A:** Merge sort does the hard work **after** splitting (merging). Quick sort does the hard work **before** splitting (partitioning).

### Card 5: Production

**Q:** Why does Python use merge sort (Timsort) instead of quick sort?
**A:** Stability guarantee + O(n log n) worst case. Quick sort is unstable and has O(n²) worst case.

### Card 6: Space

**Q:** Which sorts use extra memory?
**A:** Merge sort uses O(n) extra space. All others are in-place O(1). Timsort uses O(n) because it's merge-sort-based.

### Card 7: Partition

**Q:** What does the `i` pointer track in Lomuto partition?
**A:** The rightmost index of the "less than pivot" region. Starts at `low - 1` (empty region), grows by 1 each time a small element is found.

### Card 8: Swaps

**Q:** Which sort minimizes the number of swaps?
**A:** Selection sort — exactly n-1 swaps maximum (one per pass). This matters when writes are expensive.
