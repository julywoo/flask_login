#coding:utf-8

from database import init_db,db_session
from flask import Flask,redirect,request,session,url_for,abort,render_template,flash
from models import User

from app import app

#main page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#로그인
@app.route('/login' ,methods=['post'])
def login():
    if request.method=='POST':
        user_id=request.form['email']
        user_pw=request.form['password']

        user=User.query.filter_by(user_id=user_id).filter_by(user_pw=user_pw).first()

        if(user):
            session['logged_in']=True
            session['user_id']=user.user_id
            session['user_img']=user.user_img
            session['user_name']=user.user_name
            return redirect('/login_success')
        else:
            return '로그인 정보가 맞지 않음'
    else:
        return '잘못된 접근'

@app.route('/login_success')
def login_accept():
    return render_template('login_success.html')
#회원가입