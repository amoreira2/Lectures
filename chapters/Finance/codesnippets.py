def SR(R,W=[],freq=12):
    if np.empty(W):
        sr=R.mean()/R.std()*freq**0.5
    else:
        r=R@W
        sr=r.mean()/r.std()*freq**0.5
    return sr

def get_returns_daily(tickers,conn,startdate,enddate,variable='ret'):
    ticker=tickers[0]
    df = conn.raw_sql("""
                          select a.permno, b.ncusip, b.ticker, a.date, b.shrcd,
                          a.ret, a.vol, a.shrout, a.prc, a.cfacpr, a.cfacshr,a.retx
                          from crsp.dsf as a
                          left join crsp.msenames as b
                          on a.permno=b.permno
                          and b.namedt<=a.date
                          and a.date<=b.nameendt
                          where a.date between '"""+ startdate+"""'  and '"""+ enddate+            
                          """' and  b.ticker='"""+ticker+"'")
            
    df.set_index(['date','permno'],inplace=True)
    df=df[variable].unstack()
    return df

def get_returns_monthly(tickers,conn,startdate,enddate,variable='ret'):
    ticker=tickers[0]
    df = conn.raw_sql("""
                          select a.permno, b.ncusip, b.ticker, a.date, b.shrcd,
                          a.ret, a.vol, a.shrout, a.prc, a.cfacpr, a.cfacshr,a.retx
                          from crsp.msf as a
                          left join crsp.msenames as b
                          on a.permno=b.permno
                          and b.namedt<=a.date
                          and a.date<=b.nameendt
                          where a.date between '"""+ startdate+"""'  and '"""+ enddate+            
                          """' and  b.ticker='"""+ticker+"'")
            
    df.set_index(['date','permno'],inplace=True)
    df=df[variable].unstack()
    return df