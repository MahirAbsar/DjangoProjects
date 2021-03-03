from django.shortcuts import render
from first_app.models import Musician,Albums
from first_app.forms import MusicianForm,AlbumForm
from django.db.models import Avg,Max

# Create your views here.


def index(request):
    Musician_list = Musician.objects.order_by('first_name')
    diction = {'title':'Home Page','musician_list':Musician_list}
    return render(request,'first_app/index.html',context=diction)

def musician_form(request):
    form = MusicianForm()

    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title':'Add Musician','musician_form':form}
    return render(request,'first_app/add_musician.html',context=diction)

def album_form(request):
    form = AlbumForm()
    if request.method == "POST":
         form = AlbumForm(request.POST)
         if form.is_valid():
             form.save(commit=True)
             return index(request)
    diction = {'title':'Add Album','album_form':form}
    return render(request,'first_app/add_album.html',context=diction)

def list_of_albums(request,id):
    Musician_list = Musician.objects.get(pk=id)
    Album_info = Albums.objects.filter(artist=id).order_by('num_stars')
    Average = Albums.objects.filter(artist=id).aggregate(Avg('num_stars'))
    diction = {'title':'List Of Albums','musician_list':Musician_list,'album_list':Album_info,"avg":Average}
    return render(request,'first_app/album_list.html',context=diction)

def update_musician(request,id):
    musician_info = Musician.objects.get(pk=id)
    form = MusicianForm(instance=musician_info)
    if request.method=="POST":
        form = MusicianForm(request.POST,instance=musician_info)
        if form.is_valid():
            form.save(commit=True)
            return list_of_albums(request,id)
    diction ={'title':'Update Musician','edit_info':form}
    diction.update({'musician_id':id})
    return render(request,'first_app/update_musician.html',context=diction)

def update_album(request,id):
    album_info = Albums.objects.get(pk=id)
    form = AlbumForm(instance = album_info)
    diction={}
    if request.method =="POST":
        form = AlbumForm(request.POST,instance = album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':"Successfully Updated"})
    diction.update({"title":"Edit Album Info"})
    diction.update({"edit_album":form})
    diction.update({'album_id':id})
    return render(request,'first_app/edit_album.html',context=diction)

def delete_album(request,id):
    Album_delete = Albums.objects.get(pk=id).delete()
    diction = {"delete_confirm":"Album Deleted Successfully"}
    return render(request,'first_app/delete.html',context=diction)

def delete_musician(request,id):
    musician_info = Musician.objects.get(pk=id).delete()
    diction = {"delete_confirm":"Musician Deleted Successfully"}
    return render(request,'first_app/delete.html',context=diction)
