from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
async def filter_items(
    min: int = Query(0, ge=0),
    max: int = Query(100, le=100)
):
    return {"min": min, "max": max}
# END
