from flask import Flask, flash, request, redirect, url_for, render_template, send_file
import json
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def hello_world():

    URL = 'https://www.boots.ie/health/covid-19/covid-vaccination'
    header = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(URL, headers = header)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = {}

    if ('Due to large demand we currently have no further appointments available for the Janssen COVID-19 single dose vaccine. We will open appointments again as soon as more stock becomes available.')  in (soup.text):
        data['output_str'] = ('Appointments available')

    else:
        data['output_str'] = ('NULL')

    
    json_data = json.dumps(data)
    return json_data
