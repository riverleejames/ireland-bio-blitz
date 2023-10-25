# Postman Crud Testing

# Create Document  - (POST)

```python
POST /testing_crud HTTP/1.1
Host: 127.0.0.1:5984
Content-Type: application/json
Authorization: Basic YWRtaW46Y2E3dXdheGE=
Content-Length: 46

{
  "field1": "value1",
  "field2": "value2"
}
```

```json
{
    "ok": true,
    "id": "240b867ec60efcb9e3b315175e001d65",
    "rev": "1-c16f4cee870c7bbdf57b98c0e0956ee2"
}
```

# Get All Documents - (GET)

```json
GET /testing_crud/_all_docs HTTP/1.1
Host: 127.0.0.1:5984
Authorization: Basic YWRtaW46Y2E3dXdheGE=
```

```json
//Return Value (JSON)
{
    "total_rows": 1,
    "offset": 0,
    "rows": [
        {
            "id": "240b867ec60efcb9e3b315175e001d65",
            "key": "240b867ec60efcb9e3b315175e001d65",
            "value": {
                "rev": "1-c16f4cee870c7bbdf57b98c0e0956ee2"
            }
        }
    ]
}
```

# Get Specific Documents - (GET)

```json
GET /testing_crud/240b867ec60efcb9e3b315175e001d65 HTTP/1.1
Host: 127.0.0.1:5984
Authorization: Basic YWRtaW46Y2E3dXdheGE=
```

```json
//Return Value 
{
    "_id": "240b867ec60efcb9e3b315175e001d65",
    "_rev": "1-c16f4cee870c7bbdf57b98c0e0956ee2",
    "field1": "value1",
    "field2": "value2"
}
```

# Update Document - (PUT)

```json
PUT /testing_crud/240b867ec60efcb9e3b315175e001d65 HTTP/1.1
Host: 127.0.0.1:5984
Content-Type: application/json
Authorization: Basic YWRtaW46Y2E3dXdheGE=
Content-Length: 137

{
  "_id": "240b867ec60efcb9e3b315175e001d65",
  "_rev": "1-c16f4cee870c7bbdf57b98c0e0956ee2",
  "field1": "River",
  "field2": "James"
}
```

```json
//Return Value
{
    "ok": true,
    "id": "240b867ec60efcb9e3b315175e001d65",
    "rev": "2-eac3f08147204b35a7edb412e1701992"
}
```

# Get Specific Document After Update (GET)

```json
GET /testing_crud/240b867ec60efcb9e3b315175e001d65 HTTP/1.1
Host: 127.0.0.1:5984
Authorization: Basic YWRtaW46Y2E3dXdheGE=
```

```json
{
    "_id": "240b867ec60efcb9e3b315175e001d65",
    "_rev": "2-eac3f08147204b35a7edb412e1701992",
    "field1": "River",
    "field2": "James"
}
```

# Delete Document - (DEL)

```json
DELETE /testing_crud/240b867ec60efcb9e3b315175e001d65?rev=2-eac3f08147204b35a7edb412e1701992 HTTP/1.1
Host: 127.0.0.1:5984
Authorization: Basic YWRtaW46Y2E3dXdheGE=
```

```json
{
    "ok": true,
    "id": "240b867ec60efcb9e3b315175e001d65",
    "rev": "3-3d494909149235073b9834ed86474209"
}
```