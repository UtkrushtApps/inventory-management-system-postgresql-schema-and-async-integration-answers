# Solution Steps

1. 1. Design the PostgreSQL schema: Create a normalized 'products' table with columns id (PK, autoincrement), name (unique, not-null), description (text, nullable), quantity (integer, not-null, default 0), price (numeric 10,2, not-null), created_at and updated_at (timestamps, timezone-aware). Add a unique constraint on name and create an index on it.

2. 2. Write an Alembic migration (alembic/versions/...) to create and drop the products table and index.

3. 3. Define the SQLAlchemy ORM model in app/models.py that maps to the products table, using appropriate column types, constraints, and indexes.

4. 4. Configure async database connection and session management in app/database.py with SQLAlchemy's AsyncEngine, sessionmaker, and dependency-injection for FastAPI.

5. 5. Create Pydantic schemas (app/schemas.py) for product creation (ProductCreate) and product reading (ProductRead) with strict type validation and constraints.

6. 6. Implement the async database access logic in app/crud.py for 'create_product' (inserting a new product and handling commit/rollback) and 'get_products' (fetching all products, ordered by id). Handle rounding for price values and unique constraint errors appropriately.

7. 7. (Not shown, but assumed) In the FastAPI route handlers, use the async session dependency and call these CRUD functions for POST and GET endpoints. Return Pydantic schemas as responses.

