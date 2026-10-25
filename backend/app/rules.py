from datetime import date, timedelta
def leave_days(start: date,end: date,period: str)->float:
    if end<start: raise ValueError('結束日期不得早於開始日期')
    if period not in {'full','am','pm'}: raise ValueError('時段不合法')
    if period!='full' and start!=end: raise ValueError('半天假只接受單日')
    days=sum((start+timedelta(days=i)).weekday()<5 for i in range((end-start).days+1))
    if days==0: raise ValueError('請選擇工作日')
    return float(days) if period=='full' else 0.5
