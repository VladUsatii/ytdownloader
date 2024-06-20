from flask import render_template, Blueprint, request, flash, redirect, url_for, jsonify
from forms import InputForm
import time

# imports for downloading
from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import sys, os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    form = InputForm()
    return render_template('index.html', form=form)

@main.route('/process', methods=['POST'])
def process():
    form = InputForm()
    if form.validate_on_submit():
        input_string = form.input_string.data
        result = process_input_string(input_string)
        return jsonify({'result': result})
    return jsonify({'error': 'Invalid input'}), 400

def process_input_string(input_string):
    # finds youtube video to download
    video_caller = YouTube(input_string).streams.first().download()
    return f"Downloaded video to the local folder of this downloader: {input_string}"