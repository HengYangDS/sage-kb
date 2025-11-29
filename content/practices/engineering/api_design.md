# API Design Guidelines

> **Load Time**: On-demand (~120 tokens)  
> **Purpose**: RESTful API design principles and best practices

---

## 1. URL Design

### Resource Naming

| ✓ Good | ✗ Bad |
|--------|-------|
| `/users` | `/getUsers` |
| `/users/123` | `/user?id=123` |
| `/users/123/orders` | `/getUserOrders` |
| `/search?q=keyword` | `/doSearch` |

### Naming Rules

- Use **nouns** to represent resources
- Use **plural** forms
- Use **lowercase** + **hyphens**
- Keep hierarchy to 3 levels max

```
/users                    # User collection
/users/{id}               # Single user
/users/{id}/orders        # User's orders
/users/{id}/orders/{oid}  # User's single order
```

---

## 2. HTTP Methods

| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| `GET` | Retrieve resource | ✓ | ✓ |
| `POST` | Create resource | ✗ | ✗ |
| `PUT` | Full update | ✓ | ✗ |
| `PATCH` | Partial update | ✗ | ✗ |
| `DELETE` | Delete resource | ✓ | ✗ |

### Operation Mapping

| Operation | Method | URL | Example |
|-----------|--------|-----|---------|
| List | GET | /resources | GET /users |
| Detail | GET | /resources/{id} | GET /users/123 |
| Create | POST | /resources | POST /users |
| Update | PUT/PATCH | /resources/{id} | PUT /users/123 |
| Delete | DELETE | /resources/{id} | DELETE /users/123 |

---

## 3. Status Codes

### Success Responses

| Code | Meaning | Use Case |
|------|---------|----------|
| `200` | OK | GET/PUT/PATCH success |
| `201` | Created | POST creation success |
| `204` | No Content | DELETE success |

### Client Errors

| Code | Meaning | Use Case |
|------|---------|----------|
| `400` | Bad Request | Parameter validation failed |
| `401` | Unauthorized | Not authenticated |
| `403` | Forbidden | No permission |
| `404` | Not Found | Resource doesn't exist |
| `409` | Conflict | Resource conflict |
| `422` | Unprocessable | Business rule validation failed |
| `429` | Too Many Requests | Rate limited |

### Server Errors

| Code | Meaning | Use Case |
|------|---------|----------|
| `500` | Internal Error | Server error |
| `502` | Bad Gateway | Upstream service error |
| `503` | Service Unavailable | Service unavailable |
| `504` | Gateway Timeout | Upstream timeout |

---

## 4. Request Format

### Request Body (JSON)

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin"
}
```

### Query Parameters

| Purpose | Parameter | Example |
|---------|-----------|---------|
| Pagination | `page`, `limit` | `?page=2&limit=20` |
| Sorting | `sort`, `order` | `?sort=created_at&order=desc` |
| Filtering | field name | `?status=active&role=admin` |
| Search | `q` | `?q=keyword` |
| Field selection | `fields` | `?fields=id,name,email` |

---

## 5. Response Format

### Success Response

```json
{
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "meta": {
    "request_id": "abc-123"
  }
}
```

### List Response

```json
{
  "data": [
    {"id": 1, "name": "User 1"},
    {"id": 2, "name": "User 2"}
  ],
  "meta": {
    "total": 100,
    "page": 1,
    "limit": 20,
    "pages": 5
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {"field": "email", "message": "Invalid email format"}
    ]
  },
  "meta": {
    "request_id": "abc-123"
  }
}
```

---

## 6. Versioning

### URL Path (Recommended)

```
/api/v1/users
/api/v2/users
```

### Header

```
Accept: application/vnd.api+json;version=1
```

### Version Strategy

| Strategy | Pros | Cons |
|----------|------|------|
| URL path | Clear, easy to test | URL changes |
| Header | Clean URLs | Hidden, hard to test |
| Query param | Flexible | Easy to miss |

---

## 7. Pagination

### Offset-based

```
GET /users?page=2&limit=20
```

Response meta:
```json
{
  "meta": {
    "total": 100,
    "page": 2,
    "limit": 20,
    "pages": 5
  }
}
```

### Cursor-based

```
GET /users?cursor=abc123&limit=20
```

Response meta:
```json
{
  "meta": {
    "next_cursor": "def456",
    "has_more": true
  }
}
```

| Type | Use Case |
|------|----------|
| Offset | Small datasets, need page jumps |
| Cursor | Large datasets, real-time data |

---

## 8. Authentication

### Bearer Token

```
Authorization: Bearer <token>
```

### API Key

```
X-API-Key: <key>
```

---

## 9. Quick Checklist

| ✓ Do | ✗ Don't |
|------|---------|
| Use nouns for resources | Use verbs in URLs |
| Use plural forms | Mix singular/plural |
| Return appropriate status codes | Always return 200 |
| Include request_id in responses | Omit tracking info |
| Version your API | Break existing clients |
| Use consistent response format | Mix response structures |

---

## Related

- `content/practices/engineering/error_handling.md` — Error handling patterns
- `content/guidelines/code_style.md` — Code style guidelines

---

*Part of AI Collaboration Knowledge Base*
