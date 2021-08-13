from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Community, User
from django.core.paginator import Paginator

# Create your views here.
def community(request):
    community = Community.objects.order_by('-writeDay')
    paginator = Paginator(community, 15)
    page = request.POST.get('page')
    community = paginator.get_page(page)

    search = request.POST.get('search')
    if search == 'true':
        author = request.POST.get('writer')
        community = Community.objects.filter(writer = author)
        return render(request, 'community.html', {'community': community})
    return render(request, "community.html", {'community': community})

def create_post(request):
    if request.method == "POST":
        user = User.objects.get(login_ID = request.session['login_ID'])
        nickName = User.objects.get(login_ID = request.session['nickName'])
        title = request.POST.get('title')
        detailContent = request.POST.get('detailContent')
        keywordID = request.POST.get('keywordID')
        image = request.POST.get('image')

        # 제목, 내용, 관심분야(머릿글)을 설정해야 저장할 수 있다.
        if title != '' & title is not None & detailContent != '' & detailContent is not None & keywordID != '' & keywordID is not None:
            # 작성된 내용을 create_post에 저장
            create_post = Community(
                userID = user,
                nickName = nickName,
                title = title,
                detailContent = detailContent,
                keywordID = keywordID,
                image = image
            )
            community = create_post.save(commit=False)
            # 작성시간을 추가한 뒤
            community.writeDay = timezone.now()
            # 다시 저장
            community.save()
        return redirect('post', community.id)

def update(request, id):
    community = get_object_or_404(Community, pk=id)
    return render(request, 'community.html', {'community': community})

def updateAction(request, id):
  community = get_object_or_404(Community, pk=id)
  community.title = request.POST.get('title')
  community.userID = request.POST.get('userID')
  community.writeDay = timezone.now()
  community.detailContent = request.POST.get('detailContent')
  community.save()

  return redirect('post', community.id)

def delete(request, id):
  community = get_object_or_404(Community, pk=id)
  community.delete()

  return redirect('community.html')

def comment(request, id):
    if request.method == "POST":
        user = User.objects.get(login_ID = request.session['login_ID'])
        nickName = User.objects.get(login_ID = request.session['nickName'])
        detailContent = request.POST.get('detailContent')

        create_comment = Community(
            userID = user,
            nickName = nickName,
            detailContent = detailContent
        )
        community = create_comment.save(commit=False)
        community.writeDay = timezone.now()
        community.save()
        return render(request, 'post')
    return redirect(request, 'coummunity')

def comedit(request):
    return render(request, "comedit.html")

def comread(request):
    return render(request, "comread.html")

def comregist(request):
    return render(request, "comregist.html")