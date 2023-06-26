from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms
from django.db.models import Avg

# Create your views here.
'''
# def index(request):
#    musician_list = Musician.objects.order_by('first_name')
#    diction = {'text_01':'This is Musician list','musician':musician_list,'intro_text':'Hi I am from Index','no_of_forms':len(musician_list),'date':Album.objects.get(pk = 1),"custom":'custom text sample:'}
#    return render(request,'first_app/index.html',context = diction)

# def form(request):
#    # new_form = forms.user_form()
#    # diction = {'test_form':new_form,'heading_1':"this is from user Djnago library"}

#    # if request.method == 'POST':
#    #    new_form = forms.user_form(request.POST)
#    #    #validator
#    #    diction.update({'test_form':new_form})

#    #    if new_form.is_valid():
#    #       user_name = new_form.cleaned_data['user_name']
#    #       user_dob = new_form.cleaned_data['user_dob']
#    #       user_email = new_form.cleaned_data['user_email']
#    #       diction.update({'user_name' : user_name})
#    #       diction.update({'user_dob' : user_dob})
#    #       diction.update({'user_email' : user_email})
#    #       diction.update({'boolean_field' : new_form.cleaned_data['boolean_field']})
#    #       diction.update({'char_field' : new_form.cleaned_data['char_field']})
#    #       diction.update({'field' : new_form.cleaned_data['field']})
#    #       diction.update({'radio' : new_form.cleaned_data['radio']})



#    #       #validator
#    #       diction.update({'number':new_form.cleaned_data['number_field']})
         
#    #       diction.update({'emailv' : 'Fields Match!!'})


#    #       diction.update({'form_submited' : "yes"})

#    ####model form
#    new_form = forms.MusicianForm()       #object created

#    if request.method == 'POST':
#       new_form = forms.MusicianForm(request.POST)

#       if new_form.is_valid():      #if valid
#          new_form.save(commit=True)     #save all data
#          return index(request)

#    diction = {'test_form':new_form, 'heading_1':'Add new musician','intro_text':'Hi I am from form','concat':'expression:'}
#    return render(request,'first_app/form.html',context = diction)

'''

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title':'Home Page','musician_list':musician_list}
    return render(request,'first_app/index.html',context=diction)


def album_list(request,artist_id):
    album_list = Album.objects.filter(artist = artist_id).order_by('release_date')

    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    artist = Musician.objects.get(id=artist_id)
    diction = {'title':'List of albums','artist':artist,'album_list':album_list,'artist_rating':artist_rating}
    return render(request,'first_app/album_list.html',context=diction)



def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("first_app:index")
            # return index(request)

    diction = {'title':'Add Album','album_form':form}
    return render(request,'first_app/album_form.html',context=diction)


def musician_form(request):
    form = forms.MusicianForm()

    if request.method == "POST":
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("first_app:index")
            # return index(request)

    diction = {'title':'Add Musician','musician_form':form}
    return render(request,'first_app/musician_form.html',context=diction)


def edit_artist(request,artist_id):
    artist = Musician.objects.get(pk = artist_id) #pk or id
    form = forms.MusicianForm(instance=artist)
    diction = {}
    if request.method=='POST':
        form = forms.MusicianForm(request.POST,instance=artist)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_msg':'Artist Updated Successfully!'})
            return album_list(request,artist_id)

    
    diction.update({'title':'Edit Form','edit_form':form})

    return render(request,'first_app/edit_artist.html',context=diction)


def edit_album(request,album_id):
    album = Album.objects.get(id=album_id)
    form = forms.AlbumForm(instance=album)
    diction = {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_msg':'Album Successfully Updated!'})

            # return index(request)
            

    diction.update({'title':'Edit Album','edit_form':form,'album':album})
    return render(request,'first_app/edit_album.html',context=diction)


def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'success_msg':"Album is successfully deleted!"}
    return render(request,'first_app/delete.html',context=diction)


def delete_artist(request,artist_id):
    artist = Musician.objects.get(id=artist_id).delete()
    diction = {'success_msg':'Artist is successfully deleted!'}
    return render(request,'first_app/delete.html',context=diction)
