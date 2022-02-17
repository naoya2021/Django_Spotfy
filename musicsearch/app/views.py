from django.shortcuts import render
from typing import ValuesView
from django.views.generic import View
import requests
import json
from .forms import SearchForm
from spotipy.oauth2 import SpotifyOAuth
from requests import Request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm 

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
class IndexView(View):
    def get(self,request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        
        return render(request,'app/templates/index.html',{
            'form':form
        })

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        if form.is_valid():
            keyword = form.cleaned_data['title']
        

            list_data=[]
            sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='クライアントキー',client_secret='シークレットキー'))
            results = sp.search(q=keyword,limit=25)
            for result in results['tracks']['items']:
                title = result['name']
                id = result['id']
                popularity = result['popularity']
                image = result['album']['images'][1]['url']
                artist_name = result['album']['artists'][0]['name']

                
                
                """
                artist = sp.search(q=id,type='artist')
                artist_id = artist['artists']['items']
                artist_name=sp.artist(artist_id)
                """
                query = {
                    'title':title,
                    'id':id,
                    'popularity':popularity,
                    'image':image,
                    'artist_name':artist_name
                }
                

                list_data.append(query)
                
    
        

            return render(request,'app/templates/list.html',{
                'list_data':list_data,
                'keyword':keyword
            })

        return render(request, 'app/templates/index.html',{
            'form':form
        })
   
        
class DetailView(View):
    def get(self,request,*args,**kwargs):
        id = self.kwargs['id']
        print(id)
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='クライアントキー',client_secret='シークレットキー'))
        
        detail_data = []
        
        track = sp.track(id)
        title = track['name']
        popularity = track['popularity']
        image = track['album']['images'][1]['url']
        artist_name = track['album']['artists'][0]['name']
        # release = track['release_date']

    
        query = {
                'title':title,
                'id':id,
                'popularity':popularity,
                'image':image,
                'artist_name':artist_name,
                # 'release':release
            }
        detail_data.append(query)
        print(detail_data)

        return render(request,'app/templates/detail.html',{
            'detail_data':detail_data
        })


class LoginView(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'app/templates/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'app/templates/login.html'
