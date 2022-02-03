import os
from os import path
import pymysql
import random

from flask import Flask
from flask import jsonify


app = Flask(__name__)

app.secret_key = 'pqiwdjf'

# info about signing into the google cloud sql database
db_user = 'root'
db_password = ''
db_name = 'RandomLinks'
db_connection_name = 'seismic-gecko-326618:us-east4:nfl-prediction-challenge'

deployed = True

# Establishes connection with Google Cloud SQL database
def get_connection():
	# when deployed to app engine the 'GAE_ENV' variable will be set to 'standard'
	if deployed:
		# use the local socket interface for accessing Cloud SQL
		unix_socket = '/cloudsql/{}'.format(db_connection_name)
		conn = pymysql.connect(user=db_user, password=db_password, unix_socket=unix_socket, db=db_name)
	else:
		# if running locally use the TCP connections instead
		# set up Cloud SQL proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
		host = '127.0.0.1'
		conn = pymysql.connect(user=db_user, password=db_password, host=host, db=db_name)

	return conn

@app.route("/fun-link")
def fun_link():
    # get connection and cursor
    conn = get_connection()
    cur = conn.cursor()

    # get links from database
    cur.execute('SELECT * FROM fun_links')
    fun_links = cur.fetchall()

    # if there are no links in the category return relevant response
    if len(fun_links) == 0:
        return jsonify(
            link='null',
            description='there are no links in the database'
        ), 204

    # pick random link from the list
    rand_choice = random.randrange(len(fun_links))
    rand_link = fun_links[rand_choice][0]
    rand_description = fun_links[rand_choice][1]

    return jsonify(
        link=rand_link,
        description=rand_description
    ), 200

@app.route("/game-link")
def game_link():
    # get connection and cursor
    conn = get_connection()
    cur = conn.cursor()

    # get links from database
    cur.execute('SELECT * FROM game_links')
    game_links = cur.fetchall()

    # if there are no links in the category return relevant response
    if len(game_links) == 0:
        return jsonify(
            link='null',
            description='there are no links in the database'
        ), 204

    # pick random link from the list
    rand_choice = random.randrange(len(game_links))
    rand_link = game_links[rand_choice][0]
    rand_description = game_links[rand_choice][1]

    return jsonify(
        link=rand_link,
        description=rand_description
    ), 200

@app.route("/news-link")
def news_link():
    # get connection and cursor
    conn = get_connection()
    cur = conn.cursor()

    # get links from database
    cur.execute('SELECT * FROM news_links')
    news_links = cur.fetchall()

    # if there are no links in the category return relevant response
    if len(news_links) == 0:
        return jsonify(
            link='null',
            description='there are no links in the database'
        ), 204

    # pick random link from the list
    rand_choice = random.randrange(len(news_links))
    rand_link = news_links[rand_choice][0]
    rand_description = news_links[rand_choice][1]

    return jsonify(
        link=rand_link,
        description=rand_description
    ), 200
