import pytest
from data_structures.trees.binary_search_tree import BinarySearchTree
from core.exceptions import EmptyTreeError, DuplicateKeyError, KeyNotFoundError

def make_sample_tree():
    bst = BinarySearchTree()
    for v in [10, 12, 38, 3, 20, 8, 2, 11, 50, 35]:
        bst.insert(v)
    return bst

def test_insert_and_size():
    bst = BinarySearchTree()
    assert bst.size() == 0
    bst.insert(10)
    assert bst.size() == 1
    bst.insert(20)
    assert bst.size() == 2
    bst.insert(5)
    assert bst.size() == 3
    with pytest.raises(DuplicateKeyError):
        bst.insert(10)  # Duplicate key

def test_search():
    bst = make_sample_tree()
    assert bst.search(10) is True
    assert bst.search(50) is True
    assert bst.search(100) is False  # Non-existent key

def test_delete():
    bst = make_sample_tree()
    bst.delete(2)  # Leaf node
    assert bst.inorder() == [3, 8, 10, 11, 12, 20, 35, 38, 50]
    bst.delete(3)  # Node with one child
    assert bst.inorder() == [8, 10, 11, 12, 20, 35, 38, 50]
    bst.delete(10)  # Node with two children
    assert bst.inorder() == [8, 11, 12, 20, 35, 38, 50]
    with pytest.raises(KeyNotFoundError):
        bst.delete(100)  # Non-existent key

def test_traversals():
    bst = make_sample_tree()
    assert bst.inorder() == [2, 3, 8, 10, 11, 12, 20, 35, 38, 50]
    assert bst.preorder() == [10, 3, 2, 8, 12, 11, 38, 20, 35, 50]
    assert bst.postorder() == [2, 8, 3, 11, 35, 20, 50, 38, 12, 10]

def test_min_and_max():
    bst = make_sample_tree()
    assert bst.minm() == 2
    assert bst.maxm() == 50
    bst.delete(2)
    assert bst.minm() == 3
    bst.delete(50)
    assert bst.maxm() == 38
    with pytest.raises(EmptyTreeError):
        empty_bst = BinarySearchTree()
        empty_bst.minm()
    with pytest.raises(EmptyTreeError):
        empty_bst = BinarySearchTree()
        empty_bst.maxm()

def test_height():
    bst = make_sample_tree()
    assert bst.height() == 4  # Height of the tree
    bst.delete(50)
    assert bst.height() == 4
    bst.delete(38)
    assert bst.height() == 3

def test_dunder_methods():
    bst = make_sample_tree()
    assert str(bst) == "2, 3, 8, 10, 11, 12, 20, 35, 38, 50"
    assert repr(bst) == "BinarySearchTree([2, 3, 8, 10, 11, 12, 20, 35, 38, 50])"
    assert bool(bst) is True
    bst = BinarySearchTree()
    assert bool(bst) is False
    assert len(bst) == 0

def test_empty_tree_exceptions():
    bst = BinarySearchTree()
    with pytest.raises(EmptyTreeError):
        bst.delete(10)
    with pytest.raises(EmptyTreeError):
        bst.minm()
    with pytest.raises(EmptyTreeError):
        bst.maxm()