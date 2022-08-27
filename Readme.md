# CS50W 2021 Capstone Project - Video Chat

## To Run The Application

Navigate The Root Directory Of The Project, where manage.py file is located. Then, run the following commands:
> pip3 install requirements.txt

> pyhton3 manage.py makemigrations

> python3 manage.py migrate

> python3 manage.py runserver

### Distinctiveness and Complexity

This application is very different from other CS50w final projects that have been completed so far. However, anyone have done a group video chat app using Django and JavaScript. It is disctinctfrom the Social Network App built from my previous projects, as there is no ability to like/unlike/comment content.

It is also distinct from an e-commerce platform, as video chatting is free and immediate with no delay or watching feature, and importantly, there is nothing to buy/sell on the website.

This app is simply a video calling chatting web app.


### What's contained in each file

The ***main.html*** file is the website template, the ***lobby*** page is the default root where the user is automatically redirected to, the lobby and the ***room*** page is self-explanatory. I will focus on views pages and static files, the ***getToken*** function simply generate new tokens for the agora.io API that is used in my website, the ***lobby*** function simply display the lobby, same as ***room***, but the ***createMember*** function creates members as they register using the JavaScript local storage and Json files stored in the browser, and the ***getMember*** function gets the member from the database and display the users in the ***room*** page,and finally the ***deleteMember*** function deletes the user as soon as they leave the call.
For the static files, we only talk about ./assets that contains the *AgoraRTC_N-4.8.1.js* file, and it's an API file that cannot be edited or else the app will never work correctly. And in the other hand there is a ./images folder that contains the images of the app, and then the ./js folder that contains *streams.js* file, and it's a Vanilla JavaScript file that handles the API and the displaying of the camera and other things... Finally I created the ./styles folder that contains *main.css* file, and it contains the full app CSS code.

The website is very easy to use and doesn't require any **special** knowledge or something else.

Happy Chatting!