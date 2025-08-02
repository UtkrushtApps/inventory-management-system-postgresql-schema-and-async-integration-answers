from alembic import op
import sqlalchemy as sa

revision = '20230601_01'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('quantity', sa.Integer, nullable=False, default=0),
        sa.Column('price', sa.Numeric(10, 2), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')), 
        sa.UniqueConstraint('name', name='uq_products_name'),
    )
    op.create_index('ix_products_name', 'products', ['name'])

def downgrade():
    op.drop_index('ix_products_name', table_name='products')
    op.drop_table('products')
