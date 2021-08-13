from django.shortcuts import render, redirect

# Create your views here.
def main_no(request):
    return render(request, "main_no.html")

def main_yes(request):
    if request.session['nickName'] is not None or request.session['nickName'] != "":
        #현재 가입한 동아리


        #추천 동아리


        #유형별 동아리


        return render(request, "main_yes.html")
    else:
        return redirect('/')

