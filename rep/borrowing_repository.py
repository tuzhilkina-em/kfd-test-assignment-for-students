from typing import List, Dict
from rep.base_repository import BaseRepository
from models.borrow import BorrowingRecord

class BorrowingRepository(BaseRepository[BorrowingRecord]):
    def __init__(self):
        self._storage: List[BorrowingRecord] = []

    def add(self, record: BorrowingRecord) -> bool:
        self._storage.append(record)
        return True

    def get(self, id: str) -> BorrowingRecord:
        return None  # Not implemented for simplicity

    def get_all(self) -> List[BorrowingRecord]:
        return self._storage

    def get_overdue(self) -> List[BorrowingRecord]:
        return [r for r in self._storage if r.is_overdue() and not r.return_date]