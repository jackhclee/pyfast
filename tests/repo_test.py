from pyfast.db import repo

def test_get_records():
  assert repo.get_record(100) == {"rec_id": 100}