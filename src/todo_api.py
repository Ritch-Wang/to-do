class TodoAPI:
    def __init__(self):
        self.todos = []

    def get_list(self):
        return {"todos": self.todos}

    def add_item(self, title):
        new_todo = {
            "id": len(self.todos) + 1,
            "title": title
        }
        self.todos.append(new_todo)
        return new_todo
    
    def delete_item(self, item_id):
        for i, todo in enumerate(self.todos):
            if todo["id"] == item_id:
                return self.todos.pop(i)
            
        return None
