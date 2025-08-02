from sqlalchemy.future import select
from app.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
import decimal

def round_price(value):
    if isinstance(value, float):
        return decimal.Decimal(str(round(value, 2)))
    return value

async def create_product(session: AsyncSession, name: str, description: str, quantity: int, price: float):
    product = Product(
        name=name,
        description=description,
        quantity=quantity,
        price=round_price(price)
    )
    session.add(product)
    try:
        await session.commit()
        await session.refresh(product)
        return product
    except IntegrityError:
        await session.rollback()
        raise

async def get_products(session: AsyncSession):
    result = await session.execute(select(Product).order_by(Product.id))
    return result.scalars().all()
