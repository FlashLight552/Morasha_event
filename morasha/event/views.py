from django.shortcuts import render, get_object_or_404, redirect
from .models import EventUsers, Questions, Answers


def index(request):
    if request.method == "POST":
        name = request.POST.get("your_name")

        if not EventUsers.objects.filter(user_name = name):

            q = EventUsers(user_name = str(name))
            q.save()

            context = {
            "username": q.user_name,}

            response = render(request, "index.html", context)
            response.set_cookie('event_user_id', q.user_id)
            return response


        try:
            request.COOKIES['event_user_id']
            return redirect('/')
        except KeyError:
            context = {"name_already_used": True}
            return render(request, "index.html", context)

    try:
        username = request.COOKIES['event_user_id']
        username = EventUsers.objects.get(user_id = username).user_name
    except KeyError:
        # Cookie is not set
        username = None

    context = {
        "username": username,
    }
    return render(request, "index.html", context)
    # return render('/')

def quest(request, pk):
    try:
        username = request.COOKIES['event_user_id']
        username = EventUsers.objects.get(user_id = username).user_name
    except:
        return redirect('/')
        # username = None


    if request.method == "POST":
        answer = request.POST.get("answer")
        question_name = request.POST.get("question_name")

        if not Answers.objects.filter(user = username, question_name=question_name):
            q = Answers(user = username, answer = answer, question_name=question_name, sort_id=pk)
            q.save()

        context = {'complete':True, 
                   "username":username,}
        response = render(request, "quest.html", context)
        response.set_cookie(f'question-{pk}', True)
        return response

    try:
        request.COOKIES[f'question-{pk}']
        context =   {'complete':True,
                    "username":username,}
        
        return render(request, "quest.html", context)
    
    except KeyError:
        q = get_object_or_404(Questions, link_id = pk)
        context = {
                'question_name': q.question_name,
                'question': q.question,
                'username': username,
                }
        
        return render(request, "quest.html", context)
    
def result(request):
    q = Answers.objects.order_by('user', 'sort_id')
    context = {"model": q,}
    
    return render(request, "result.html", context)
