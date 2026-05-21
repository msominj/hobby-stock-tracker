
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pathlib import Path
from pydantic import BaseModel
from typing import List, Optional
from app.db import SessionLocal
from app.models import InventoryItem, WishlistItem

app = FastAPI()

# Home page route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Allow CORS for local frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas
class InventoryItemBase(BaseModel):
    name: str
    category: str
    quantity: int
    photo_path: Optional[str] = None
    needed: bool = False

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemResponse(InventoryItemBase):
    id: int
    class Config:
        orm_mode = True

class WishlistItemBase(BaseModel):
    name: str
    category: str
    quantity: int
    photo_path: Optional[str] = None

class WishlistItemCreate(WishlistItemBase):
    pass

class WishlistItemResponse(WishlistItemBase):
    id: int
    class Config:
        orm_mode = True



# --- API ENDPOINTS ---
# Inventory CRUD

@app.get("/api/inventory", response_model=List[InventoryItemResponse])
def get_inventory(db: Session = Depends(get_db)):
    return db.query(InventoryItem).all()

@app.post("/api/inventory", response_model=InventoryItemResponse)
def create_inventory(item: InventoryItemCreate, db: Session = Depends(get_db)):
    db_item = InventoryItem(**item.dict(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/api/inventory/{item_id}", response_model=InventoryItemResponse)
def update_inventory(item_id: int, item: InventoryItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/api/inventory/{item_id}")
def delete_inventory(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"ok": True}

# Wishlist CRUD
@app.get("/api/wishlist", response_model=List[WishlistItemResponse])
def get_wishlist(db: Session = Depends(get_db)):
    return db.query(WishlistItem).all()

@app.post("/api/wishlist", response_model=WishlistItemResponse)
def create_wishlist(item: WishlistItemCreate, db: Session = Depends(get_db)):
    db_item = WishlistItem(**item.dict(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/api/wishlist/{item_id}", response_model=WishlistItemResponse)
def update_wishlist(item_id: int, item: WishlistItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(WishlistItem).filter(WishlistItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/api/wishlist/{item_id}")
def delete_wishlist(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(WishlistItem).filter(WishlistItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"ok": True}


# --- HTML ROUTES ---
@app.get("/inventory", response_class=HTMLResponse)
def inventory(request: Request):
    return templates.TemplateResponse("inventory.html", {"request": request})

@app.get("/wishlist", response_class=HTMLResponse)
def wishlist(request: Request):
    return templates.TemplateResponse("wishlist.html", {"request": request})
