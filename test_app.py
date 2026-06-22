from app import TodoAPI
import pytest

@pytest.fixture
def api():
    return TodoAPI()

@pytest.fixture
def api_with_items():
    """TodoAPI pre-loaded with two items."""
    api = TodoAPI()
    api.add_item("Buy groceries")
    api.add_item("Walk the dog")
    return api


# --- get_list ---

def test_get_list_empty(api):
    assert api.get_list() == {"todos": []}

def test_get_list_returns_all_items(api_with_items):
    result = api_with_items.get_list()
    assert len(result["todos"]) == 2


# --- add_item ---

def test_add_item_returns_new_todo(api):
    result = api.add_item("Buy groceries")
    assert result == {"id": 1, "title": "Buy groceries"}

def test_add_item_increments_id(api):
    api.add_item("First")
    result = api.add_item("Second")
    assert result["id"] == 2

def test_add_item_appears_in_list(api):
    api.add_item("Buy groceries")
    todos = api.get_list()["todos"]
    assert any(t["title"] == "Buy groceries" for t in todos)


# --- delete_item ---

def test_delete_item_returns_deleted_todo(api_with_items):
    deleted = api_with_items.delete_item(1)
    assert deleted["id"] == 1
    assert deleted["title"] == "Buy groceries"

def test_delete_item_removes_from_list(api_with_items):
    api_with_items.delete_item(1)
    ids = [t["id"] for t in api_with_items.get_list()["todos"]]
    assert 1 not in ids

def test_delete_item_not_found_returns_none(api):
    assert api.delete_item(999) is None

def test_delete_item_leaves_others_intact(api_with_items):
    api_with_items.delete_item(1)
    todos = api_with_items.get_list()["todos"]
    assert len(todos) == 1
    assert todos[0]["id"] == 2