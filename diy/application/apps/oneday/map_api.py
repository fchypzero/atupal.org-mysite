
from application import app
from flask import request
from application.apps.oneday import getLine
from application.apps.oneday import getInfo

import urllib
import json

@app.route('/getmap', methods = ['GET', 'POST'])
def getmap():
    lat = request.args.get('lat', '')
    lng = request.args.get('lng', '')
    lat = float('lat')
    lng = float('lng')

@app.route('/getList', methods = ['GET', 'POST'])
def getList():
    lat = float(request.form['lat'])
    lng = float(request.form['lng'])
    begin = int(request.form['begin'])
    end = int(request.form['end'])
    return getLine.Line().getline(lat, lng, begin, end)

@app.route('/getLine', methods = ['GET', 'POST'])
def getLineInfo():
    line = str(request.form['line']).split('-')
    lat = float(request.form['lat'])
    lng = float(request.form['lng'])
    img = []
    intra = []
    bus = []
    map_1 = []
    for i in xrange(len(line)):
        tmp = getInfo.getInfo(line[i])
        img.append(tmp['img'])
        intra.append(tmp['intra'])
        bus.append(tmp['bus'])
        map_1.append("http://api.map.baidu.com/staticimage?markers=" + urllib.quote(line[i]) + "&center=" + urllib.quote(line[i]))
    map_3 = "http://api.map.baidu.com/staticimage?center=116.403874,39.914889&width=400&height=300&zoom=11&markers=116.288891,40.004261|116.487812,40.017524|116.525756,39.967111|116.536105,39.872374|116.442968,39.797022|116.270494,39.851993|116.275093,39.935251|116.383177,39.923743&markerStyles=l,A|m,B|l,C|l,D|m,E|,|l,G|m,H"
    ret = {
            'map_3':map_3,
            'map_1':map_1,
            'img':img,
            'intra':intra,
            'bus':bus
            }
    return json.dumps(ret)