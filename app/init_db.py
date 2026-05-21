
from app.db import engine, Base, SessionLocal
import app.models  # Ensure models are imported
from app.models import InventoryItem, WishlistItem

def insert_sample_data():
    db = SessionLocal()
    # Only insert if tables are empty
    if db.query(InventoryItem).count() == 0:
        db.add_all([
            InventoryItem(name="Red Yarn", category="Yarn", quantity=5, photo_path="https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=facearea&w=100&h=100", needed=False),
            InventoryItem(name="Blue Wool", category="Wool", quantity=2, photo_path="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=facearea&w=100&h=100", needed=True),
            InventoryItem(name="PLA Filament", category="Filaments", quantity=1, photo_path="https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=facearea&w=100&h=100", needed=True),
            InventoryItem(name="Acrylic Paint", category="Paints", quantity=10, photo_path="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=facearea&w=100&h=100", needed=False)
        ])
    if db.query(WishlistItem).count() == 0:
        db.add_all([
            WishlistItem(name="Blue Wool", category="Wool", quantity=2, photo_path="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=facearea&w=100&h=100"),
            WishlistItem(name="PLA Filament", category="Filaments", quantity=1, photo_path="https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=facearea&w=100&h=100")
        ])
    db.commit()
    db.close()

if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Inserting sample data...")
    insert_sample_data()
    print("Done.")
