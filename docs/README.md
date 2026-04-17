# DSA Library in Python

A structured, modular, and scalable implementation of **Data Structures and Algorithms in Python**, designed for deep understanding, clean architecture, and long-term reference.

---

## Overview

This project is not just a collection of DSA problems—it is a **mini standard library** for:

* Implementing core data structures
* Designing reusable algorithms
* Practicing interview-style problems
* Understanding system-level design in Python

---

## 🏗Project Structure

``` bash
dsa/
│
├── core/                  # Shared components
│   ├── node.py
│   ├── interfaces.py
│   └── exceptions.py
│
├── structures/            # Data structures
│   ├── array/
│   ├── linked_list/
│   ├── stack/
│   ├── queue/
│   └── trees/
│
├── algorithms/            # Reusable algorithms
│   ├── linked_list/
│   ├── tree/
│   ├── dp/
│   └── greedy/
│
├── problems/              # Interview-style problems
│
├── tests/                 # Unit tests (pytest)
├── benchmarks/            # Performance analysis
├── utils/                 # Helpers + visualization
│
└── main.py                # Entry point / demos
```

---

## 📦 Implemented Data Structures

### Linked Lists

* Singly Linked List
* Doubly Linked List (under development)
* Circular Linked List (under development)

### Stack

* Array-based Stack (planned)
* Linked Stack

### Queue

* Simple Queue (planned)
* Circular Queue (planned)
* Linked Queue

### Trees

* Binary Tree
* Binary Search Tree (BST)

### Arrays (*coming soon!*)

* Static Array
* Dynamic Array (resizable)

---

## ⚙️ Algorithms

Algorithms are organized by topic and separated from data structures. **Currently working on it.**

### Examples:

* Linked List

  * Reverse List
  * Cycle Detection

* Trees

  * BST Validation (multiple approaches)
  * Traversals

* Dynamic Programming *(planned)*

* Greedy *(planned)*

---

## Design Philosophy

### 1. Separation of Concerns

* `structures/` → how data is stored
* `algorithms/` → how data is processed
* `problems/` → how concepts are applied


### 2. Multiple Approaches per Problem

Each algorithm may have:

* Optimal solution
* Alternative solutions
* Brute-force approach

Only the **best implementation is exposed**, while others remain for learning.

### 3. Clean Python Design

* Encapsulation (`_size`, `_root`)
* Iterables (`__iter__`)
* Debug-friendly (`__repr__`)
* Consistent APIs via interfaces

---

### 4. Reusability

Algorithms operate on:

* raw nodes (`head`, `root`)
* not tied to specific classes

---

## 🧠 Learning Goals

This project helps you:

* Master DSA concepts deeply
* Understand time/space trade-offs
* Learn clean code architecture
* Build production-quality Python code

---

## 💡 Example Usage

```python
from structures.trees.binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)

print(bst)        # BST(5, 10, 15)

for x in bst:
    print(x)
```

---

## 🤝 Contributing

This is primarily a personal learning project, but suggestions and improvements are welcome.

---

## ⭐ Key Insight

> *This project is not just about solving problems, it’s about building a **systematic understanding of data structures and algorithms**.*

---

## 📌 Author

Built as part of a structured journey into:

* Data Structures
* Algorithms
* System Design
* Python Engineering

---
