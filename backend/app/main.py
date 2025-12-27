from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- Nhớ dòng import này

app = FastAPI()

# --- CẤU HÌNH CORS (CHO PHÉP TẤT CẢ) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Dấu * nghĩa là chấp nhận mọi địa chỉ (localhost, 127.0.0.1, mobile...)
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép mọi phương thức: GET, POST, PUT, DELETE...
    allow_headers=["*"],  # Cho phép mọi loại header
)
# ---------------------------------------


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Backend!"}
