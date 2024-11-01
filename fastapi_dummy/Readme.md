# Steps

1. Create Virtual Env
2. Install fastapi, uvicorn
3. After adding main, use `uvicorn main:app --reload` to run the server

## Routers

- Separate operators into multiple files
- share a prefix b/w multiple operations
- Share Tags

```python
from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])

app.include_router(router)
```
