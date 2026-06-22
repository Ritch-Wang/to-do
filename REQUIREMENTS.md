# To-Do Management System

## Purpose

The purpose of this application is to help users manage tasks that need to be completed.

A user should be able to **create** tasks, **view** existing tasks, **update** task information, and **mark** tasks as completed.

The application should provide a simple and reliable way to track outstanding work.

---

## Users

### Task Owner

A Task Owner is a person who manages their own list of tasks.

Initially, the system will only support a single user.

---

## Business Concepts

### To-Do Item

A To-Do Item represents a piece of work that needs to be completed.

Each To-Do Item has:

* A title
* A completion status
* A creation date

---

## Functional Requirements

### View To-Do Items

A user shall be able to view all existing To-Do Items

Acceptance Criteria:

* All items shall be displayed
* Completed and incomplete items shall be visible
* Initially an empty list

---

### Add a To-Do Item to the list

A user shall be able to create a new To-Do Item

Acceptance Criteria:

* A title/description is required
* A new item has "incomplete" status
* The item shall record when it was created - BONUS / low priority

---

### Update a To-Do Item

User can modify a To-Do Item

Acceptance Criteria:

* The title/description can be updated
* can be marked as complete / incomplete

---

### Delete

Acceptance Criteria:

* Deleted items shall no longer be visible
