from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from HMS.models import StudentUser, Recruiter

# Create your views here.


def training(request):
    return render(request, "training.html")


def trainadmin(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    d = {"error": error}
    return render(request, "trainadmin.html", d)


def adminhome(request):
    if (
        not request.user.is_authenticated
    ):  # this to check rec khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")  # rec  login page pr aa jaye
    return render(request, "adminhome.html")


def trainuser(request):  # this is for user login
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        # uname hmne loginpage mein yeh name rakh hai isliye yeh use kr liya u  can give name=email also
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(
                        request, user
                    )  # first if else will check whether the type is student or recruiter if student then no error
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        # this is for try block
        else:
            error = "yes"  # this is for if to end
    d = {"error": error}
    return render(request, "trainuser.html", d)


def trainrecruiter(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        # uname hmne loginpage mein yeh name rakh hai isliye yeh use kr liya u  can give name=email also
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "pending":
                    login(
                        request, user
                    )  # first if else will check whether the type is student or recruiter if student then no error
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"  # this is for try block
        else:
            error = "yes"  # this is for if to end
    d = {"error": error}
    return render(request, "trainrecruiter.html", d)


def recsignup(request):
    error = ""
    if request.method == "POST":
        f = request.POST["fname"]
        l = request.POST["lname"]
        i = request.FILES["image"]  # image ke alwayssss use files
        p = request.POST["pwd"]
        e = request.POST["email"]
        con = request.POST["contact"]
        g = request.POST["gender"]
        company = request.POST["company"]
        try:
            user = User.objects.create_user(
                password=p, username=e
            )
            Recruiter.objects.create(
                user=user,
                mobile=con,
                image=i,
                gender=g,
                company=company,
                type="recruiter",
                status="pending",
            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(e)
    d = {"error": error}
    return render(request, "recsignup.html", d)


def rechome(request):
    if (
        not request.user.is_authenticated
    ):  # this to check rec khi aise to nhi aa gya without beung registered
        return redirect("/trainrecruiter/")  # rec  login page pr aa jaye
    return render(request, "rechome.html")


def userhome(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainuser/")  # user e login page pr aa jaye
    return render(request, "userhome.html")


def Logout(request):
    logout(request)
    return redirect("/training/")


def usersignup(request):
    error = ""
    if request.method == "POST":
        f = request.POST["fname"]
        l = request.POST["lname"]
        i = request.FILES["image"]  # image ke alwayssss use files
        p = request.POST["pwd"]
        e = request.POST["email"]
        con = request.POST["contact"]
        g = request.POST["gender"]
        try:
            user = User.objects.create_user(
                password=p, username=e
            )
            StudentUser.objects.create(
                user=user, mobile=con, image=i, gender=g, type="student"
            )
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    d = {"error": error}
    return render(request, "usersignup.html", d)


def viewusers(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    data = StudentUser.objects.all()
    d = {"data": data}

    return render(request, "viewusers.html", d)


def delete_user(request, pid):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    student = User.objects.get(
        id=pid
        )  # same neeche jaisa
    student.delete()
    return redirect("/viewusers/")

 
def delete_recruiter(request, pid):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    recruiter = User.objects.get(
        id=pid
    )  # imp we have not delete from recruiter main model bcoz vo sirf vha se del krega isliye hmne user se kiya del har jagah se del hoga
    recruiter.delete()
    return redirect("/allrecruiters/")


def pending(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    data = Recruiter.objects.filter(status="pending")
    d = {"data": data}

    return render(request, "pending.html", d)


def changestatus(request, pid):
    if(
        not request.user.is_authenticated
    ):
      return redirect("/trainadmin/")                   # this to check user khi aise to nhi aa gya without beung registered                                                              
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST["status"]
        recruiter.status = s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    d = {"recruiter": recruiter, "error": error}
    return render(request, "changestatus.html", d)



def accepted(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    data = Recruiter.objects.filter(status="Accept")
    d = {"data": data}

    return render(request, "accepted.html", d)


def rejected(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    data = Recruiter.objects.filter(status="Reject")
    d = {"data": data}

    return render(request, "rejected.html", d)


def allrecruiters(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    data = Recruiter.objects.all()
    d = {"data": data}

    return render(request, "allrecruiters.html", d)


def passadmin(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainadmin/")
    error = ""
    if request.method == "POST":
        c = request.POST["currentpassword"]
        n = request.POST["newpassword"]
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):  # this are function in django
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "passadmin.html", d)


def passuser(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainuser/")
    error = ""
    if request.method == "POST":
        c = request.POST["currentpassword"]
        n = request.POST["newpassword"]
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):  # this are function in django
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "passuser.html", d)


def passrec(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainrecruiter/")
    error = ""
    if request.method == "POST":
        c = request.POST["currentpassword"]
        n = request.POST["newpassword"]
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):  # this are function in django
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "passrec.html", d)


def addjobrec(request):
    if (
        not request.user.is_authenticated
    ):  # this to check user khi aise to nhi aa gya without beung registered
        return redirect("/trainrecruiter/")
    return render(request, "addjobrec.html")
