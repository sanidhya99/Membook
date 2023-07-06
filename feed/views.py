from django.shortcuts import render,redirect
from .models import *
from .forms import *
from register.models import CustomUser
from datetime import datetime
from django.contrib import messages
#------------------------------------------------------------------------------------------
def feed(response):
    show=post.objects.all().order_by('-id')
   
    return render(response,'feed/posts.html',{"feeds":show,})
#------------------------------------------------------------------------------------------
def profile(response):
    if response.user.is_authenticated:
        person=response.user
        print("hello")
        ps=post.objects.filter(author=response.user.id).order_by('-id')
        # ps=post.objects.get(author=response.user)
    else:
        return redirect("/login")    
            
    return render(response,'feed/profile.html',{"person":person,"posts":ps,})
#------------------------------------------------------------------------------------------
def users(response):
    us=CustomUser.objects.all()

    return render(response,'feed/users.html',{"users":us,})
#------------------------------------------------------------------------------------------

def view(response,id):
    a=False
    if(id==response.user.id):
        return redirect("/visit/profile")
    us=CustomUser.objects.get(id=id)
    shooter=response.user
    if block.objects.filter(blocker=response.user,blocked=us).exists():
        a=True
    else:
        a=False    
    b=True
    if friends.objects.filter(friend=us,email=shooter).exists():
        b=True
        print(b)
        print("friends")
        print(us)
    else:
        b=False
        print("not yet")
    print(b)   
    if b is False:
        if response.method=="POST":
            if response.POST.get("add" + str(id)) == "clicked":
                if block.objects.filter(blocker=us,blocked=shooter).exists():
                    
                    messages.info(response,message="You are blocked by the user!!!")
                else:
                    rq=requests.objects.create(subject=us,sender=response.user.email,accept=False)
                    rq.save()
    else:
        if response.method=='POST':
            if response.POST.get("delete" + str(id)) == "clicked":
                fr=friends.objects.filter(friend=us,email=shooter)
                for f in fr:
                    f.delete()     
    if a is False:
        if response.method=='POST':
            if response.POST.get("block"+str(id))=="clicked":
                if friends.objects.filter(friend=shooter,email=us).exists():
                    for f in friends.objects.filter(friend=shooter,email=us):
                        f.delete()
                bl=block(blocker=shooter,blocked=us)
                bl.save()
    else:
        if response.method=='POST':
            if response.POST.get("unblock"+str(id))=="clicked":
                b=block.objects.get(blocker=shooter,blocked=us)
                b.delete()
                

    ps=post.objects.filter(author=us.id)
    return render(response,'feed/view.html',{"user":us,"check":b,"posts":ps,"check2":a})
#------------------------------------------------------------------------------------------
def viewmail(response,mail):
    if(mail==response.user.email):
        return redirect("/visit/profile")
    us=CustomUser.objects.get(email=mail)
    if response.method=="POST":
        if response.POST.get("c" + str(mail)) == "clicked":
            sub=CustomUser.objects.get(email=mail).id
            rq=requests.objects.create(subject=us,sender=response.user.email,accept=False)
            rq.save()
    return render(response,'feed/viewmail.html',{"user":us,})
#------------------------------------------------------------------------------------------
def input(response):
    if response.method=="POST":
        form=posts(response.POST)
        if form.is_valid():
            image=form.cleaned_data["photo"]
            caption=form.cleaned_data["caption"]
            time=datetime.now().time()
            date=datetime.now().date()
            pt=post.objects.create(author=response.user,photo=image,caption=caption,time=time,date=date,)
            pt.save()
    else:
        form=posts()
    return render(response,'feed/input.html',{"form":form,})

#------------------------------------------------------------------------------------------

def request(response):
    rq=requests.objects.filter(subject=response.user.id)
    if response.method=='POST':
        for r in rq:
            if(response.POST.get("add"+str(r.sender))=="clicked"):
                fr=friends.objects.create(friend=response.user,email=r.sender)
                print(f"nandani and sanidhya are life partners")
                fr.save()
                r.delete()
            elif(response.POST.get("del"+str(r.sender))=="clicked"):
                r.delete()    
    b=False            
    if(len(rq)==0):
        b=False
    else:
        b=True    
    return render(response,'feed/requests.html',{"requests":rq,"check":b,})
def home(response):
    if response.user.is_authenticated:
        msg=response.user.name
    else:
        msg="GUEST"    
    

    return render(response,"feed/home.html",{"us":msg})   

def cmnt(response,id):
    cmts=comments.objects.filter(post=id).order_by('-id')
    if response.method=='POST':
        form=comment(response.POST)
        if form.is_valid():
            text=form.cleaned_data["text"]
            time=datetime.now().time()
            date=datetime.now().date()
            pt=post.objects.get(id=id)
            cm=comments.objects.create(post=pt,author=response.user.name,text=text,time=time,date=date)
            cm.save()
    else:
        form=comment()
    
    b=False
    if len(cmts)==0:
        b=False
    else:
        b=True    
    return render(response,'feed/comments.html',{"form":form,"comments":cmts,"check":b,})
