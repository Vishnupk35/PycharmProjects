#Decorator function is used to avoid multiple similar functions.

#Decorator function should placed above the fn with @dec_fn
# Here we need results only in positive terms without making changes to the respective function.
# We are using dec_fn as an extra function to act on some other function without modifying it.
def dec_fn(fn): #def decorate_fn name(fn) #fn is the function which we are using
    def inner_fn(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)#fn acts like the func we are calling
    return inner_fn

@dec_fn
def sub(n1,n2):
    return n1-n2
@dec_fn
def div(n1,n2):
    return n1/n2

print(sub(10,20)) #Will get positive answer because dec_fn working.
print(div(10,20))