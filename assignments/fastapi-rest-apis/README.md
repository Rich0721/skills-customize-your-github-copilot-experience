# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice creating endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core CRUD Endpoints

#### Description
Build a FastAPI application for managing a simple list of books. Implement endpoints to create, read, update, and delete books using in-memory storage.

#### Requirements
Completed program should:

- Create a FastAPI app with routes for `GET /books`, `GET /books/{book_id}`, `POST /books`, `PUT /books/{book_id}`, and `DELETE /books/{book_id}`
- Return JSON responses with clear fields for each book (`id`, `title`, `author`, `year`)
- Return appropriate status codes for success and error cases (for example, `404` when a book is not found)
- Use in-memory data (list or dictionary) without a database


### 🛠️	Add Query Filtering and Validation

#### Description
Improve your API by adding query parameters and input validation so the API is easier to use and more reliable.

#### Requirements
Completed program should:

- Add optional query filtering to `GET /books` (for example, filter by author)
- Use Pydantic models for request validation when creating or updating books
- Reject invalid input with meaningful validation errors (for example, missing `title` or invalid `year`)
- Include at least one example request and response in code comments or testing notes
