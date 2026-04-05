## Planned Project Structure

``` bash
dsa/
│
├── core/                         # Shared abstractions
│   ├── __init__.py
│   ├── node.py                   # Generic node definitions
│   ├── exceptions.py             # Custom errors
│   └── interfaces.py             # Abstract base classes
│
├── structures/                   # ALL data structures
│   ├── __init__.py
│   │
│   ├── linked_list/
│   │   ├── __init__.py
│   │   ├── singly.py
│   │   ├── doubly.py
│   │   └── circular.py
│   │
│   ├── stack/
│   │   ├── __init__.py
│   │   ├── array_stack.py
│   │   └── linked_stack.py
│   │
│   ├── queue/
│   │   ├── __init__.py
│   │   ├── simple_queue.py
│   │   ├── circular_queue.py
│   │   └── deque.py
│   │
│   ├── trees/
│   │   ├── __init__.py
│   │   ├── binary_tree.py
│   │   ├── binary_search_tree.py
│   │   ├── avl_tree.py
│   │   ├── segment_tree.py
│   │
│   ├── heap/
│   │   ├── __init__.py
│   │   ├── min_heap.py
│   │   ├── max_heap.py
│   │
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── adjacency_list.py
│   │   └── adjacency_matrix.py
│   │
│   └── hash/
│       ├── __init__.py
│       └── hashmap.py
│
├── algorithms/                     # PURE algorithms (no DS logic inside)
│   ├── __init__.py
│   │
│   ├── linked_list/
│   │   ├── cycle.py
│   │   ├── reversal.py
│   │   └── merge.py
│   │
│   ├── tree/
│   │   ├── traversal.py
│   │   ├── lca.py
│   │   └── height.py
│   │
│   ├── graph/
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   └── dijkstra.py
│   │
│   ├── sorting/
│   │   ├── quicksort.py
│   │   └── mergesort.py
│   │
│   └── searching/
│       └── binary_search.py
│
├── problems/                       # Interview style problems
│   ├── __init__.py
│   │
│   ├── arrays/
│   ├── linked_list/
│   ├── trees/
│   ├── graphs/
│   │
│   ├── greedy/
│   │   ├── p1_fractional_knapsack.py
│   │   └── p2_activity_selection.py
│   │
│   ├── dp/
│   │   ├── p1_01_knapsack.py
│   │   └── p2_lcs.py
│   │
│   └── mixed/
│        └── leetcode_ideas.py
│
├── utils/                          # Helpers, visualization, etc.
│   ├── __init__.py
│   ├── visualization.py
│   └── helpers.py
│
│
├── tests/                          # Unit tests
│   ├── __init__.py
│   ├── test_linked_list.py
│   └── test_tree.py
│
│
├── benchmarks/                     # Performance comparisons
│   └── compare_structures.py
│
└── main.py
```