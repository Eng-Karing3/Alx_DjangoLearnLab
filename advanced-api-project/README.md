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
