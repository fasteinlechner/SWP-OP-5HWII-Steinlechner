import functools
import time

def timer(func):
    #@functools.wraps(func)
    def wraper_timer(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print("The Function needed:", (time_end-time_start))
    return wraper_timer

@timer
def function (a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
def check_url(func):
    
    urls = ["www.google.com", "www.yahoo.com", "www.bing.com"]
    @functools.wraps(func)
    def wraper_check_url(*args, **kwargs):
        for url in urls:
            if (url in args) or (url in kwargs.values()):
                print("THIS IS AN INVALID URL - Please use a valid URL!")
                return
        func(*args, **kwargs)
    return wraper_check_url

            

@check_url
def webrequest (url):
    print(url)

if __name__ =="__main__":
    function(*[0], **{ 'b':20})
    print(function.__name__)
    
    webrequest("www.google.com")
    webrequest(*("www.google.com", "www.yahoo.com",))
    webrequest(**{"url":"www.google.com"})
    

    
