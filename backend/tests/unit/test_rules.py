from datetime import date
import pytest
from app.rules import leave_days
@pytest.mark.req('TC-04','AC-01.3','FR-03')
@pytest.mark.parametrize('start,end,period,expected',[('2026-10-23','2026-10-26','full',2),('2026-10-20','2026-10-20','am',.5),('2026-10-20','2026-10-20','pm',.5)])
def test_workdays_and_half_day(start,end,period,expected):
    assert leave_days(date.fromisoformat(start),date.fromisoformat(end),period)==expected
@pytest.mark.req('TC-04','AC-01.3','FR-03')
@pytest.mark.parametrize('start,end,period',[('2026-10-24','2026-10-25','full'),('2026-10-20','2026-10-21','am'),('2026-10-24','2026-10-24','pm')])
def test_invalid_day_ranges(start,end,period):
    with pytest.raises(ValueError):leave_days(date.fromisoformat(start),date.fromisoformat(end),period)
