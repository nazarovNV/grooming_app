from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Room, Task, Vote


def room_list(request):
    rooms = Room.objects.all().order_by('-created_at')
    return render(request, 'poker/room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    tasks = room.tasks.all()

    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        task_description = request.POST.get('task_description')
        if task_title:
            Task.objects.create(
                room=room,
                title=task_title,
                description=task_description
            )
            return redirect('room_detail', room_id=room_id)

    return render(request, 'poker/room_detail.html', {
        'room': room,
        'tasks': tasks
    })


def vote(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        voter_name = request.POST.get('voter_name')
        score = request.POST.get('score')

        if voter_name and score:
            Vote.objects.update_or_create(
                task=task,
                voter_name=voter_name,
                defaults={'score': score}
            )

    return redirect('room_detail', room_id=task.room.id)


def complete_voting(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        final_score = request.POST.get('final_score')
        if final_score:
            task.final_score = final_score
            task.save()

    return redirect('room_detail', room_id=task.room.id)


def vote_results(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    votes = task.votes.all()

    # Подсчет результатов
    vote_counts = {}
    for vote in votes:
        vote_counts[vote.score] = vote_counts.get(vote.score, 0) + 1

    return render(request, 'poker/vote_results.html', {
        'task': task,
        'votes': votes,
        'vote_counts': vote_counts
    })


def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            room = Room.objects.create(name=room_name)
            return redirect('room_detail', room_id=room.id)

    return redirect('room_list')