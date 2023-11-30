from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, backref, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Type, TypeVar, Generic, Optional

Base = declarative_base()
T = TypeVar('T', bound=Base)


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    is_relative = Column(Boolean) # Assuming String, change if different
    interval = Column(String)  # Assuming String, change if different
    data_source = Column(String)
    market_index = Column(String)
    sec_type = Column(String)


class StockData(Base):
    __tablename__ = 'stock_data'
    bar_number = Column(Integer, primary_key=True)
    close = Column(Float)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    stock = relationship("Stock", backref=backref("stock_data", uselist=False))


class TimestampData(Base):
    __tablename__ = 'timestamp_data'
    bar_number = Column(Integer, primary_key=True)
    interval = Column(String)
    timestamp = Column(DateTime)
    data_source = Column(String)


class Regime(Base):
    __tablename__ = 'regime'
    start = Column(Integer, ForeignKey('timestamp_data.bar_number'), primary_key=True)
    end = Column(Integer, ForeignKey('timestamp_data.bar_number'), primary_key=True)
    rg = Column(String)
    type = Column(String)
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key=True)
    stock = relationship("Stock", backref="regime")


class FloorCeiling(Base):
    __tablename__ = 'floor_ceiling'
    test = Column(String)
    fc_val = Column(Float)
    fc_date = Column(DateTime)
    rg_ch_date = Column(DateTime)
    rg_ch_val = Column(Float)
    type = Column(String)
    stock_id = Column(Integer, ForeignKey('stock.id'))


class Peak(Base):
    __tablename__ = 'peak'
    start = Column(Integer, ForeignKey('timestamp_data.bar_number'), primary_key=True)
    end = Column(Integer, ForeignKey('timestamp_data.bar_number'), primary_key=True)
    type = Column(Integer)
    lvl = Column(Integer)
    st_px = Column(Float)
    en_px = Column(Float)
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key=True)


if __name__ == '__main__':
    # Replace 'your_database_url' with the actual database URL
    engine = create_engine('your_database_url')
    Base.metadata.create_all(engine)
