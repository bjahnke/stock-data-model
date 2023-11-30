class BaseRepository(Generic[T]):
    def __init__(self, s: Session, model: Type[T], id_attr: str = 'id'):
        self.session = s
        self.model = model
        self.id_attr = id_attr

    def get_by_id(self, id_value: int) -> Optional[T]:
        return self.session.query(self.model).filter(getattr(self.model, self.id_attr) == id_value).one_or_none()


class StockRepository(BaseRepository[Stock]):
    def __init__(self, session: Session):
        super().__init__(session, Stock)


class StockDataRepository(BaseRepository[StockData]):
    def __init__(self, session: Session):
        super().__init__(session, StockData, 'bar_number')


class TimestampDataRepository(BaseRepository[TimestampData]):
    def __init__(self, session: Session):
        super().__init__(session, TimestampData, 'bar_number')


class RegimeRepository(BaseRepository[Regime]):
    def __init__(self, session: Session):
        super().__init__(session, Regime, 'stock_id')


class FloorCeilingRepository(BaseRepository[FloorCeiling]):
    def __init__(self, session: Session):
        super().__init__(session, FloorCeiling, 'stock_id')


class PeakRepository(BaseRepository[Peak]):
    def __init__(self, session: Session):
        super().__init__(session, Peak, 'stock_id')

# Example Usage
if __name__ == '__main__':
    _s = None  # Assume a valid SQLAlchemy session is created here

    # Creating repository instances
    stock_repo = StockRepository(_s)
    stock_data_repo = StockDataRepository(_s)
    timestamp_data_repo = TimestampDataRepository(_s)
    regime_repo = RegimeRepository(_s)
    floor_ceiling_repo = FloorCeilingRepository(_s)
    peak_repo = PeakRepository(_s)

    # Example: Fetch a stock by its ID
    stock = stock_repo.get_by_id(1)

    # Example: Fetch stock data by bar number
    stock_data = stock_data_repo.get_by_id(100)
