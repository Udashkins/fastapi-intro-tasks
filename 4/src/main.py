from fastapi import FastAPI, Cookie

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/language")
async def get_language(language: str | None = Cookie(None)):
    if language is None:
        return {"message": "Language not set"}
    return {"language": language}
# END
