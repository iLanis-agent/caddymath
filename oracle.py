import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def caddies(n, b):
    k = -(-n//b)
    return f"The {pl(n,' cupcake',' cupcakes')} at {pl(b,' cupcake',' cupcakes')} a caddy {v(n,'takes','take')} {pl(k,' caddy',' caddies')}, the last caddy holding {pl(n-(k-1)*b,' cupcake',' cupcakes')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' cupcake',' cupcakes')} at {pl(w,' cupcake',' cupcakes')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' cupcake',' cupcakes')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' caddy',' caddies')} at ${m(pc)} a caddy {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a cupcake."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' cupcake',' cupcakes')} at {pl(pm,' cupcake',' cupcakes')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(794)
R = random.randint
cases = [
 dict(fn="caddies", args=["290","12"], expect=caddies(290,12)),
 dict(fn="weeks", args=["290","22"], expect=weeks(290,22)),
 dict(fn="cost", args=["25","13.50","290"], expect=cost(25,1350,290)),
 dict(fn="time", args=["290","5"], expect=time_(290,5)),
 dict(fn="caddies", args=["1","1"], expect=caddies(1,1)),
 dict(fn="caddies", args=["360","8"], expect=caddies(360,8)),
 dict(fn="caddies", args=["1000000","1000"], expect=caddies(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["360","30"], expect=weeks(360,30)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="caddies", args=[str(n),str(b)], expect=caddies(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["caddies",["0","8"]],["caddies",["1000001","8"]],["caddies",["2.5","8"]],["caddies",["290","0"]],["caddies",["290","1001"]],
 ["weeks",["0","30"]],["weeks",["290","0"]],["weeks",["290","100001"]],["weeks",["290","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","12.75","290"]],["cost",["100001","12.75","290"]],["cost",["46","0","290"]],["cost",["46","12.755","290"]],["cost",["46","12.75","0"]],
 ["time",["0","8"]],["time",["290","0"]],["time",["290","101"]],["time",["290","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
