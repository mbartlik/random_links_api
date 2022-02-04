import os
from os import path
import pymysql
import random
import requests

from flask import Flask
from flask import jsonify
from flask import request



app = Flask(__name__)

app.secret_key = 'pqiwdjf'

# info about signing into the google cloud sql database
db_user = 'root'
db_password = ''
db_name = 'main'
db_connection_name = 'random-links-api:us-east4:random-links'

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

@app.route("/fun-link", methods=['GET', 'POST', 'DELETE'])
def fun_link():
    # get connection and cursor
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'GET':
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

    # add a link to the database
    if request.method == 'POST':
        new_link = request.form['link']
        new_description = request.form['description']

        try:
            requests.get(new_link)
        except Exception as e:
            return jsonify(
                status="Failure - " + new_link + " is an invalid url"
            ), 406

        try:
            cur.execute('INSERT INTO fun_links VALUES (%s, %s)', (new_link, new_description))
            conn.commit()
            conn.close()

            return jsonify(
                status="Success - Added " + new_link + " to fun links"
            )
        except:
            pass
        return jsonify(
            status="Failure - an error occurred when adding " + new_link + " to fun links"
        )

    # delete a link from the database
    if request.method == 'DELETE':
        to_delete = request.form['link']

        try:
            result = cur.execute('DELETE FROM fun_links WHERE link LIKE \'%' + to_delete + '%\'')

            # if there was no link deleted
            if result < 1:
                return jsonify(
                    status='Failure - Could not find a link like ' + to_delete + ' in the database'
                )

            conn.commit()
            conn.close()

            # success response
            return jsonify(
                status='Success - Deleted ' + to_delete + ' from the database' 
            )
        except Exception as e:
            pass
        
        # failure response
        return jsonify(
            status='Failure - There was some error when trying to delete the link from the database'
        )
            


@app.route("/game-link", methods=['GET', 'POST', 'DELETE'])
def game_link():
    # get connection and cursor
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'GET':
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

    # add a link to the database
    if request.method == 'POST':
        new_link = request.form['link']
        new_description = request.form['description']

        try:
            requests.get(new_link)
        except Exception as e:
            return jsonify(
                status="Failure - " + new_link + " is an invalid url"
            ), 406

        try:
            cur.execute('INSERT INTO game_links VALUES (%s, %s)', (new_link, new_description))
            conn.commit()
            conn.close()
            
            return jsonify(
                status="Success - Added " + new_link + " to game links"
            )
        except:
            pass
        return jsonify(
            status="Failure - an error occurred when adding " + new_link + " to game links"
        )

    # delete a link from the database
    if request.method == 'DELETE':
        to_delete = request.form['link']

        try:
            result = cur.execute('DELETE FROM game_links WHERE link LIKE \'%' + to_delete + '%\'')

            # if there was no link deleted
            if result < 1:
                return jsonify(
                    status='Failure - Could not find a link like ' + to_delete + ' in the database'
                )

            conn.commit()
            conn.close()

            # success response
            return jsonify(
                status='Success - Deleted ' + to_delete + ' from the database' 
            )
        except Exception as e:
            pass
        
        # failure response
        return jsonify(
            status='Failure - There was some error when trying to delete the link from the database'
        )

@app.route("/news-link", methods=['GET', 'POST', 'DELETE'])
def news_link():
    # get connection and cursor
    conn = get_connection()
    cur = conn.cursor()

    if request.method == 'GET':
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

    # add a link to the database
    if request.method == 'POST':
        new_link = request.form['link']
        new_description = request.form['description']

        try:
            requests.get(new_link)
        except Exception as e:
            return jsonify(
                status="Failure - " + new_link + " is an invalid url"
            ), 406

        try:
            cur.execute('INSERT INTO news_links VALUES (%s, %s)', (new_link, new_description))
            conn.commit()
            conn.close()
            
            return jsonify(
                status="Success - Added " + new_link + " to news links"
            )
        except:
            pass
        return jsonify(
            status="Failure - an error occurred when adding " + new_link + " to news links"
        )

    # delete a link from the database
    if request.method == 'DELETE':
        to_delete = request.form['link']

        try:
            result = cur.execute('DELETE FROM news_links WHERE link LIKE \'%' + to_delete + '%\'')

            # if there was no link deleted
            if result < 1:
                return jsonify(
                    status='Failure - Could not find a link like ' + to_delete + ' in the database'
                )

            conn.commit()
            conn.close()

            # success response
            return jsonify(
                status='Success - Deleted ' + to_delete + ' from the database' 
            )
        except Exception as e:
            pass
        
        # failure response
        return jsonify(
            status='Failure - There was some error when trying to delete the link from the database'
        )