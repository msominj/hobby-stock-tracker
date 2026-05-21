# Hobby Stock Tracker - App Specification

## One-Liner
A visual inventory app for hobbyists to track craft supplies by photo and quantity, with a built-in shopping and wish list.

## High-Level Functional Requirements

1. **Inventory Management**
   - Users can add new inventory items, each with:
     - A photo (taken or uploaded)
     - A category (e.g., threads, fabrics, wool, filaments, etc.)
     - A quantity counter
   - Quantities can be decremented or updated after use.
   - All changes are persisted locally (e.g., local database or file storage).

2. **Visual Main View**
   - The main screen displays a scrollable grid of item photos.
   - Each item shows its current stock count clearly on the photo or as an overlay.

3. **Search and Filter**
   - Users can search for items by name.
   - Users can filter items by category.
   - Search and filter features allow quick location of specific stock.

4. **Shopping/Wish List Integration**
   - Any item can be flagged as "needed" (e.g., low stock or wish list).
   - Flagged items are automatically added to a shopping list or wish list.
   - The shopping/wish list is easily accessible for store visits or online ordering.

## Non-Functional Requirements (Optional)
- Responsive design for mobile and desktop use.
- Simple, intuitive user interface with clear visual cues.
- Data privacy: all inventory data remains local unless explicitly exported.
- Optional: Export/import inventory data (e.g., CSV, JSON, or photo archive).

## Out of Scope
- No cloud sync or user accounts required for MVP.
- No in-app purchasing or direct e-commerce integration.

---
This specification outlines the core features and user experience for the "Hobby Stock Tracker" app, focusing on visual inventory management and ease of use for hobbyists managing craft supplies.