# Book API — View Configurations

## Overview
This API provides CRUD operations for managing books using Django REST Framework's **generic views**.

---

## Views

### 1. BookListCreateView
**Endpoint:** `/books/`

- **GET**: Returns a list of all books.
  - Permission: Public (no authentication required).
- **POST**: Creates a new book.
  - Permission: Authenticated users only.
  - Custom Validation: Rejects submissions without a `title`.

**Custom Hooks Used:**
- `get_permissions()`: Dynamically assigns permissions based on request method.
- `perform_create()`: Adds custom validation before saving the book.

---

### 2. BookRetrieveUpdateDestroyView
**Endpoint:** `/books/<id>/`

- **GET**: Returns details of a specific book by ID.
  - Permission: Public.
- **PUT/PATCH**: Updates book details.
  - Permission: Authenticated users only.
  - Custom Validation: Title cannot be empty.
- **DELETE**: Deletes the specified book.
  - Permission: Authenticated users only.

**Custom Hooks Used:**
- `get_permissions()`: Dynamically changes access control per HTTP method.
- `perform_update()`: Prevents updates with empty titles.

---

## Permissions Summary
| Action  | Authentication Required | Public Access |
|---------|------------------------|---------------|
| List    | No                     | ✅            |
| Retrieve| No                     | ✅            |
| Create  | Yes                    | ❌            |
| Update  | Yes                    | ❌            |
| Delete  | Yes                    | ❌            |

---

## Testing
Use **Postman** or **curl**:
```bash
# List all books
curl http://127.0.0.1:8000/books/

# Create book (requires authentication)
curl -X POST http://127.0.0.1:8000/books/ \
     -H "Content-Type: application/json" \
     -d '{"title": "New Book", "publication_date": "2025-08-09", "author": 1}'


## Testing Documentation

### Testing Strategy

- We use Django’s built-in test framework (based on Python’s `unittest`) to ensure the API behaves correctly.
- A separate test database is automatically created during testing to protect production and development data.
- Tests cover all CRUD operations on the Book model endpoints.
- We also test filtering by author, searching by title, and ordering by publication year.
- Authentication and permission enforcement are verified on protected endpoints.
- Each test simulates HTTP requests and checks both response status codes and returned data.

### Test Cases

1. **Create Book Requires Authentication:**  
   Ensures unauthenticated users cannot create books and authenticated users can.

2. **List Books:**  
   Retrieves all books; verifies filtering, searching, and ordering features.

3. **Retrieve Single Book:**  
   Fetches a specific book by ID and verifies response data.

4. **Update Book:**  
   Checks that authenticated users can update book details successfully.

5. **Delete Book:**  
   Confirms authenticated users can delete books and the book is removed.

6. **Permissions:**  
   Verifies endpoints enforce authentication as expected.

### How to Run Tests

Run the tests using the following command from the project root:

```bash
python manage.py test api
