from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from .forms import GroupForm

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'group_form.html', {'form': form})

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'group_form.html', {'form': form})

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'group_confirm_delete.html', {'group': group})
