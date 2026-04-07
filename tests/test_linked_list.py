import pytest

from data_structures.linked_list.single import LinkedList


def make_linked_list(values):
	ll = LinkedList()
	for value in values:
		ll.append(value)
	return ll


def test_empty_list_initial_state():
	ll = LinkedList()

	assert len(ll) == 0
	assert bool(ll) is False
	assert ll.head is None
	assert ll.tail is None
	assert list(ll) == []
	assert str(ll) == " => None"


def test_append_on_empty_sets_head_tail_and_count():
	ll = LinkedList()
	ll.append(10)

	assert len(ll) == 1
	assert bool(ll) is True
	assert ll.head is ll.tail
	assert ll.head.data == 10
	assert list(ll) == [10]


def test_append_multiple_preserves_order_and_tail():
	ll = LinkedList()
	ll.append(1)
	ll.append(2)
	ll.append(3)

	assert len(ll) == 3
	assert ll.head.data == 1
	assert ll.tail.data == 3
	assert ll.tail.next is None
	assert list(ll) == [1, 2, 3]
	assert str(ll) == "1 => 2 => 3 => None"


def test_prepend_on_empty_sets_head_tail_and_count():
	ll = LinkedList()
	ll.prepend(7)

	assert len(ll) == 1
	assert ll.head is ll.tail
	assert ll.head.data == 7
	assert list(ll) == [7]


def test_prepend_multiple_reverses_input_order():
	ll = LinkedList()
	ll.prepend(1)
	ll.prepend(2)
	ll.prepend(3)

	assert len(ll) == 3
	assert ll.head.data == 3
	assert ll.tail.data == 1
	assert list(ll) == [3, 2, 1]


def test_mixed_prepend_and_append_keeps_links_consistent():
	ll = LinkedList()
	ll.append(2)
	ll.prepend(1)
	ll.append(3)

	assert len(ll) == 3
	assert ll.head.data == 1
	assert ll.tail.data == 3
	assert list(ll) == [1, 2, 3]


def test_popleft_raises_on_empty_list():
	ll = LinkedList()

	with pytest.raises(IndexError, match="popleft from empty list"):
		ll.popleft()


def test_pop_raises_on_empty_list():
	ll = LinkedList()

	with pytest.raises(IndexError, match="pop from empty list"):
		ll.pop()


def test_popleft_single_element_empties_list_cleanly():
	ll = make_linked_list([42])

	assert ll.popleft() == 42
	assert len(ll) == 0
	assert not ll
	assert ll.head is None
	assert ll.tail is None
	assert list(ll) == []


def test_pop_single_element_empties_list_cleanly():
	ll = make_linked_list([42])

	assert ll.pop() == 42
	assert len(ll) == 0
	assert not ll
	assert ll.head is None
	assert ll.tail is None
	assert list(ll) == []


def test_popleft_multiple_moves_head_and_preserves_tail():
	ll = make_linked_list([1, 2, 3])

	assert ll.popleft() == 1
	assert len(ll) == 2
	assert ll.head.data == 2
	assert ll.tail.data == 3
	assert list(ll) == [2, 3]


def test_pop_multiple_moves_tail_and_terminates_tail_next():
	ll = make_linked_list([1, 2, 3, 4])

	assert ll.pop() == 4
	assert len(ll) == 3
	assert ll.tail.data == 3
	assert ll.tail.next is None
	assert list(ll) == [1, 2, 3]


def test_remove_returns_false_on_empty_list():
	ll = LinkedList()

	assert ll.remove(123) is False


def test_remove_head_default_removes_first_match_only():
	ll = make_linked_list([5, 5, 6])

	assert ll.remove(5) is True
	assert len(ll) == 2
	assert ll.head.data == 5
	assert ll.tail.data == 6
	assert list(ll) == [5, 6]


def test_remove_tail_updates_tail_reference():
	ll = make_linked_list([1, 2, 3])

	assert ll.remove(3) is True
	assert len(ll) == 2
	assert ll.tail.data == 2
	assert ll.tail.next is None
	assert list(ll) == [1, 2]


def test_remove_middle_node_relinks_neighbors():
	ll = make_linked_list([1, 2, 3, 4])

	assert ll.remove(3) is True
	assert len(ll) == 3
	assert list(ll) == [1, 2, 4]


def test_remove_value_not_present_returns_false_and_no_change():
	ll = make_linked_list([1, 2, 3])

	assert ll.remove(9) is False
	assert len(ll) == 3
	assert list(ll) == [1, 2, 3]


def test_remove_all_false_stops_after_first_removal():
	ll = make_linked_list([1, 2, 1, 1, 3])

	assert ll.remove(1, all=False) is True
	assert len(ll) == 4
	assert list(ll) == [2, 1, 1, 3]


def test_remove_all_true_removes_all_matches_across_head_middle_and_tail():
	ll = make_linked_list([1, 2, 1, 3, 1])

	assert ll.remove(1, all=True) is True
	assert len(ll) == 2
	assert ll.head.data == 2
	assert ll.tail.data == 3
	assert ll.tail.next is None
	assert list(ll) == [2, 3]


def test_remove_all_true_when_every_node_matches_empties_list():
	ll = make_linked_list([7, 7, 7])

	assert ll.remove(7, all=True) is True
	assert len(ll) == 0
	assert ll.head is None
	assert ll.tail is None
	assert list(ll) == []


@pytest.mark.parametrize(
	"values,target,expected",
	[
		([], 1, False),
		([1], 1, True),
		([1, 2, 3], 2, True),
		([1, 2, 3], 9, False),
	],
)
def test_contains(values, target, expected):
	ll = make_linked_list(values)
	assert ll.contains(target) is expected


@pytest.mark.parametrize(
	"values,target,expected_index",
	[
		([], 1, -1),
		([1], 1, 0),
		([1, 2, 3], 2, 1),
		([5, 6, 5, 7], 5, 0),
		([1, 2, 3], 9, -1),
	],
)
def test_find(values, target, expected_index):
	ll = make_linked_list(values)
	assert ll.find(target) == expected_index


def test_replace_first_occurrence_only_by_default():
	ll = make_linked_list([1, 2, 1, 3])

	assert ll.replace(1, 9) is True
	assert len(ll) == 4
	assert list(ll) == [9, 2, 1, 3]


def test_replace_all_occurrences():
	ll = make_linked_list([1, 2, 1, 3, 1])

	assert ll.replace(1, 9, all=True) is True
	assert len(ll) == 5
	assert list(ll) == [9, 2, 9, 3, 9]


def test_replace_value_not_found_returns_false_and_no_change():
	ll = make_linked_list([1, 2, 3])

	assert ll.replace(8, 99) is False
	assert list(ll) == [1, 2, 3]


def test_protected_empty_list_helper_does_nothing_when_count_not_one():
	ll = make_linked_list([1, 2])

	assert ll._empty_list() is None
	assert len(ll) == 2
	assert list(ll) == [1, 2]


def test_protected_empty_list_helper_resets_when_singleton():
	ll = make_linked_list([11])

	assert ll._empty_list() == 11
	assert len(ll) == 0
	assert ll.head is None
	assert ll.tail is None


def test_repr_returns_string_without_error():
	ll = make_linked_list([1, 2, 3])
	assert isinstance(repr(ll), str)
