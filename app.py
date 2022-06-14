from flask import Flask,jsonify,request,Response,render_template,make_response

from flask_cors import CORS, cross_origin
import os
import time
import numpy as np
app=Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.debug=True
    app.run(host='localhost',port=int(os.environ.get("PORT",8080)))
def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)
    
@app.route('/')
def index():
    context = { 'server_time': format_server_time() }
    # 1
    template = render_template('index.html', context=context)
    # 2
    response = make_response(template)
    # 3
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response

@cross_origin(supports_credentials=True)
@app.route('/muz',methods=['POST','GET'])
def getMuz():
    if request.method=='GET':
        return 'HELLO GET'
    if request.method=='POST':
        return 'HELLO POST'
@cross_origin(supports_credentials=True)
@app.route('/wins',methods=['POST'])
def wins():
    data=request.get_json()
    spades={'2S':0,'3S':1,"4S":2,"5S":3,'6S':4,'7S':5,'8S':6,'9S':7,'0S':8,'JS':9,'QS':10,'KS':11,'AS':12}
    clubs={'2C':0,'3C':1,"4C":2,"5C":3,'6C':4,'7C':5,'8C':6,'9C':7,'0C':8,'JC':9,'QC':10,'KC':11,'AC':12}
    hearts={'2H':0,'3H':1,"4H":2,"5H":3,'6H':4,'7H':5,'8H':6,'9H':7,'0H':8,'JH':9,'QH':10,'KH':11,'AH':12}
    diamonds={'2D':0,'3D':1,"4D":2,"5D":3,'6D':4,'7D':5,'8D':6,'9D':7,'0D':8,'JD':9,'QD':10,'KD':11,'AD':12}
    
    
    if data['trump']=='NO TRUMP':
        
        values=data['values']
        suit=data['suit']
        rank=[]
        indexx=0
        for value in values:
            if suit=='SPADES':
                if value[0] not in spades.keys():
                    rank.append([value[0],0])
                else:
                    rank.append([value[0],spades[value[0]]])
            if suit=='HEARTS':
                if value[0] not in hearts.keys():
                    rank.append([value[0],0])
                else:
                    rank.append([value[0],hearts[value[0]]])

            if suit=='DIAMONDS':
                if value[0] not in diamonds.keys():
                    rank.append([value[0],0])
                else:
                    rank.append([value[0],diamonds[value[0]]])

            if suit=='CLUBS':
                if value[0] not in clubs.keys():
                    rank.append([value[0],0])
                else:
                    rank.append([value[0],clubs[value[0]]])
        maxx=0
        for j in rank:
            if j[1]>maxx:
                maxx=j[1]
        for i in rank:
            indexx+=1
            if i[1]==maxx:
                break
        resp=jsonify({'rank':rank,'index':indexx})
            
        return resp
        
    else:
        resp={}
        dict1={'spades':2,'hearts':2,'diamonds':2,'clubs':2}
        dict2={'S':'spades','H':'hearts','D':'diamonds','C':'clubs'}
        print(data)
        trumpsuit=data['trump']
        values=data['values']
        suit=data['suit']
        rank=[]
        trump={}
        if trumpsuit=='SPADES':
            trump=spades
        if trumpsuit=='CLUBS':
            trump=clubs
        if trumpsuit=='HEARTS':
            trump=hearts
        if trumpsuit=='DIAMONDS':
            trump=diamonds
        indexx=0
        for value in values:
            if(suit=='SPADES'):
                if(value[1] != trumpsuit and value[0] not in spades.keys()):
                    rank.append([value[0],0])
                if(value[1] ==trumpsuit):
                    rank.append([value[0],trump[value[0]]+30])
                else:
                    
                    rank.append([value[0],spades[value[0]]])
            if(suit=='HEARTS'):
                if(value[1] != trumpsuit and value[0] not in hearts.keys()):
                    rank.append([value[0],0])
                if(value[1] ==trumpsuit):
                    rank.append([value[0],trump[value[0]]+30])
                else:
                    rank.append([value[0],hearts[value[0]]])
            if(suit=='CLUBS'):
                if(value[1] != trumpsuit and value[0] not in clubs.keys()):
                    rank.append([value[0],0])
                if(value[1] ==trumpsuit):
                    rank.append([value[0],trump[value[0]]+30])
                else:
                    rank.append([value[0],clubs[value[0]]])
            if(suit=='DIAMONDS'):
                if(value[1] != trumpsuit and value[0] not in diamonds.keys()):
                    rank.append([value[0],0])
                if(value[1] ==trumpsuit):
                    rank.append([value[0],trump[value[0]]+30])
                else:
                    rank.append([value[0],diamonds[value[0]]])
        
        
        maxx=0
        for j in rank:
            if j[1]>maxx:
                maxx=j[1]
                    
            
        for i in rank:
            indexx+=1
                
            if i[1]==maxx:
                break
        print(rank,indexx)
        resp=jsonify({'rank':rank,'index':indexx})
        return resp
@cross_origin(supports_credentials=True)
@app.route('/bid',methods=['GET','POST'])

def bid():
    biddict={'1 Clubs':1,'1 Diamonds':2,'1 Hearts':3,'1 Spades':4,'1 No Trump':5,
            '2 Clubs':6,'2 Diamonds':7,'2 Hearts':8,'2 Spades':9,'2 No Trump':10,
            '3 Clubs':11,'3 Diamonds':12,'3 Hearts':13,'3 Spades':14,'3 No Trump':15,
            '4 Clubs':16,'4 Diamonds':17,'4 Hearts':18,'4 Spades':19,'4 No Trump':20,
            '5 Clubs':21,'5 Diamonds':22,'5 Hearts':23,'5 Spades':24,'5 No Trump':25,
            '6 Clubs':26,'6 Diamonds':27,'6 Hearts':28,'6 Spades':29,'6 No Trump':30,
            '7 Clubs':31,'7 Diamonds':32,'7 Hearts':33,'7 Spades':34,'7 No Trump':35}
    bidlist=["1 Clubs","1 Diamonds","1 Hearts","1 Spades","1 No Trump",
             "2 Clubs","2 Diamonds","2 Hearts","2 Spades","2 No Trump",
             "3 Clubs","3 Diamonds","3 Hearts","3 Spades","3 No Trump",
             "4 Clubs","4 Diamonds","4 Hearts","4 Spades","4 No Trump",
             "5 Clubs","5 Diamonds","5 Hearts","5 Spades","5 No Trump",
             "6 Clubs","6 Diamonds","6 Hearts","6 Spades","6 No Trump",
             "7 Clubs","7 Diamonds","7 Hearts","7 Spades","7 No Trump"]
    data=request.get_json()
    
    if request.method=="GET":
        resp=jsonify({'list':bidlist})
        print("here")
        
        return resp
    if request.method=="POST":
        
        data=request.get_json()
        keyy=data['bid']
        index=bidlist.index(keyy)
        print(data,index)
        
        newbid=bidlist[index+1:]
        resp=jsonify({"list":newbid})
        
        
        
        return resp
    