# Authentication

認証は、共通鍵認証を用いる。

```
# Authorization Header
Bearer <token>
```

# APIs
## POST /records

### Request
```
{
    "suicaId": <string>,
    "recordType": <enum: "clock-in" | "clock-out">
}
```

### Response
```
204
```

## POST /users

### Request
```
{
    "name": <string>,
    "email": <string>,
    "suicaId": <string>
}
```

### Response
```
201
{
    "id": <string>
}
```