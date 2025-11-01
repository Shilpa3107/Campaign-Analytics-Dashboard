from database import SessionLocal, engine
from models import Campaign, Base

def seed_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Campaign).count() == 0:  # Only seed if empty
        campaigns = [
             {"id": 1, "name": "Summer Sale", "status": "Active", "clicks": 150, "cost": 45.99, "impressions": 1000},
        {"id": 2, "name": "Black Friday", "status": "Paused", "clicks": 320, "cost": 89.50, "impressions": 2500},
        {"id": 3, "name": "Winter Deals", "status": "Active", "clicks": 220, "cost": 60.20, "impressions": 1800},
        {"id": 4, "name": "Festival Promo", "status": "Paused", "clicks": 440, "cost": 110.00, "impressions": 3000},
        {"id": 5, "name": "End of Year Sale", "status": "Active", "clicks": 180, "cost": 55.80, "impressions": 1500},
        {"id": 6, "name": "New Launch", "status": "Active", "clicks": 270, "cost": 72.50, "impressions": 2100},
        {"id": 7, "name": "Special Offer", "status": "Paused", "clicks": 130, "cost": 35.20, "impressions": 900},
        {"id": 8, "name": "Diwali Sale", "status": "Active", "clicks": 390, "cost": 140.10, "impressions": 3500},
        {"id": 9, "name": "Holi Discounts", "status": "Paused", "clicks": 125, "cost": 50.75, "impressions": 1100},
        {"id": 10, "name": "Limited Edition Drop", "status": "Active", "clicks": 520, "cost": 200.00, "impressions": 4800},
        ]

        for c in campaigns:
            db.add(Campaign(**c))

        db.commit()
    db.close()
