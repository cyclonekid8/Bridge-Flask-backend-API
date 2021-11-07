{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a60bb82",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,jsonify,request,Response\n",
    "from flask_cors import CORS, cross_origin\n",
    "app=Flask(__name__)\n",
    "CORS(app, support_credentials=True)\n",
    "if __name__ == '__main__':\n",
    "    app.debug=True\n",
    "    app.run(host='localhost',port=5000)\n",
    "@app.route('/',methods=['GET','POST'])\n",
    "def get_users():\n",
    "    if request.method=='POST':\n",
    "        return jsonify({'user1':'Muz','user2':'Khai','user3':'Haziq','user4':'Fin'})\n",
    "    if request.method=='GET':\n",
    "        return 'Hello'\n",
    "@app.route('/wins',methods=['POST'])\n",
    "def wins():\n",
    "    data=request.get_json()\n",
    "    spades={'2S':0,'3S':1,\"4S\":2,\"5S\":3,'6S':4,'7S':5,'8S':6,'9S':7,'0S':8,'JS':9,'QS':10,'KS':11,'AS':12}\n",
    "    clubs={'2C':0,'3C':1,\"4C\":2,\"5C\":3,'6C':4,'7C':5,'8C':6,'9C':7,'0C':8,'JC':9,'QC':10,'KC':11,'AC':12}\n",
    "    hearts={'2H':0,'3H':1,\"4H\":2,\"5H\":3,'6H':4,'7H':5,'8H':6,'9H':7,'0H':8,'JH':9,'QH':10,'KH':11,'AH':12}\n",
    "    diamonds={'2D':0,'3D':1,\"4D\":2,\"5D\":3,'6D':4,'7D':5,'8D':6,'9D':7,'0D':8,'JD':9,'QD':10,'KD':11,'AD':12}\n",
    "    \n",
    "    \n",
    "    if data['trump']=='No trump':\n",
    "        \n",
    "        values=data['values']\n",
    "        suit=data['suit']\n",
    "        rank=[]\n",
    "        indexx=0\n",
    "        for value in values:\n",
    "            if suit=='SPADES':\n",
    "                if value[0] not in spades.keys():\n",
    "                    rank.append([value[0],0])\n",
    "                else:\n",
    "                    rank.append([value[0],spades[value[0]]])\n",
    "            if suit=='HEARTS':\n",
    "                if value[0] not in hearts.keys():\n",
    "                    rank.append([value[0],0])\n",
    "                else:\n",
    "                    rank.append([value[0],hearts[value[0]]])\n",
    "\n",
    "            if suit=='DIAMONDS':\n",
    "                if value[0] not in diamonds.keys():\n",
    "                    rank.append([value[0],0])\n",
    "                else:\n",
    "                    rank.append([value[0],diamonds[value[0]]])\n",
    "\n",
    "            if suit=='CLUBS':\n",
    "                if value[0] not in clubs.keys():\n",
    "                    rank.append([value[0],0])\n",
    "                else:\n",
    "                    rank.append([value[0],clubs[value[0]]])\n",
    "        maxx=0\n",
    "        for j in rank:\n",
    "            if j[1]>maxx:\n",
    "                maxx=j[1]\n",
    "        for i in rank:\n",
    "            indexx+=1\n",
    "            if i[1]==maxx:\n",
    "                break\n",
    "        resp=jsonify({'rank':rank,'index':indexx})\n",
    "            \n",
    "        return resp\n",
    "        \n",
    "    else:\n",
    "        resp={}\n",
    "        dict1={'spades':2,'hearts':2,'diamonds':2,'clubs':2}\n",
    "        dict2={'S':'spades','H':'hearts','D':'diamonds','C':'clubs'}\n",
    "        print(data)\n",
    "        trumpsuit=data['trump']\n",
    "        values=data['values']\n",
    "        suit=data['suit']\n",
    "        rank=[]\n",
    "        trump={}\n",
    "        if trumpsuit=='SPADES':\n",
    "            trump=spades\n",
    "        if trumpsuit=='CLUBS':\n",
    "            trump=clubs\n",
    "        if trumpsuit=='HEARTS':\n",
    "            trump=hearts\n",
    "        if trumpsuit=='DIAMONDS':\n",
    "            trump=diamonds\n",
    "        indexx=0\n",
    "        for value in values:\n",
    "            if(suit=='SPADES'):\n",
    "                if(value[1] != trumpsuit and value[0] not in spades.keys()):\n",
    "                    rank.append([value[0],0])\n",
    "                if(value[1] ==trumpsuit):\n",
    "                    rank.append([value[0],trump[value[0]]+30])\n",
    "                else:\n",
    "                    \n",
    "                    rank.append([value[0],spades[value[0]]])\n",
    "            if(suit=='HEARTS'):\n",
    "                if(value[1] != trumpsuit and value[0] not in hearts.keys()):\n",
    "                    rank.append([value[0],0])\n",
    "                if(value[1] ==trumpsuit):\n",
    "                    rank.append([value[0],trump[value[0]]+30])\n",
    "                else:\n",
    "                    rank.append([value[0],hearts[value[0]]])\n",
    "            if(suit=='CLUBS'):\n",
    "                if(value[1] != trumpsuit and value[0] not in clubs.keys()):\n",
    "                    rank.append([value[0],0])\n",
    "                if(value[1] ==trumpsuit):\n",
    "                    rank.append([value[0],trump[value[0]]+30])\n",
    "                else:\n",
    "                    rank.append([value[0],clubs[value[0]]])\n",
    "            if(suit=='DIAMONDS'):\n",
    "                if(value[1] != trumpsuit and value[0] not in diamonds.keys()):\n",
    "                    rank.append([value[0],0])\n",
    "                if(value[1] ==trumpsuit):\n",
    "                    rank.append([value[0],trump[value[0]]+30])\n",
    "                else:\n",
    "                    rank.append([value[0],diamonds[value[0]]])\n",
    "        \n",
    "        \n",
    "        maxx=0\n",
    "        for j in rank:\n",
    "            if j[1]>maxx:\n",
    "                maxx=j[1]\n",
    "                    \n",
    "            \n",
    "        for i in rank:\n",
    "            indexx+=1\n",
    "                \n",
    "            if i[1]==maxx:\n",
    "                break\n",
    "        print(rank,indexx)\n",
    "        resp=jsonify({'rank':rank,'index':indexx})\n",
    "        return resp\n",
    "@app.route('/bid',methods=['GET','POST'])\n",
    "@cross_origin(supports_credentials=True)\n",
    "def bid():\n",
    "    biddict={'1 Diamonds':1,'1 Clubs':2,'1 Hearts':3,'1 Spades':4,'1 No Trump':5,\n",
    "            '2 Diamonds':6,'2 Clubs':7,'2 Hearts':8,'2 Spades':9,'2 No Trump':10,\n",
    "            '3 Diamonds':11,'3 Clubs':12,'3 Hearts':13,'3 Spades':14,'3 No Trump':15,\n",
    "            '4 Diamonds':16,'4 Clubs':17,'4 Hearts':18,'4 Spades':19,'4 No Trump':20,\n",
    "            '5 Diamonds':21,'5 Clubs':22,'5 Hearts':23,'5 Spades':24,'5 No Trump':25,\n",
    "            '6 Diamonds':26,'6 Clubs':27,'6 Hearts':28,'6 Spades':29,'6 No Trump':30,\n",
    "            '7 Diamonds':31,'7 Clubs':32,'7 Hearts':33,'7 Spades':34,'7 No Trump':35}\n",
    "    data=request.get_json()\n",
    "    \n",
    "    if request.method==\"GET\":\n",
    "        resp=jsonify({'dict':biddict})\n",
    "        print(\"here\")\n",
    "        \n",
    "        return resp\n",
    "    if request.method==\"POST\":\n",
    "        \n",
    "        data=request.get_json()\n",
    "        keyy=data['bid']\n",
    "        value=biddict[keyy]\n",
    "        temp=biddict.copy()\n",
    "        for k,v in temp.items():\n",
    "            if v<=value:\n",
    "                biddict.pop(k)\n",
    "        resp=jsonify({'dict':biddict})\n",
    "        print(\"there\")\n",
    "        \n",
    "        return resp"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}