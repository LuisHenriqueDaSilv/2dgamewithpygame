level_1 = [
    {
        "type":"Wall",
        "xpos": -128,
        "ypos":522,
        "ground":False,
        "inverted":True,
        "repeat_y":5
    },
    {
        "type":"Ground",
        "xpos": 0,
        "ypos": 650,
        "repeat_x": 20
    },
    {
        "type":"Wall",
        "xpos": 128*20,
        "ypos":522,
        "ground":True,
        "inverted":False,
        "repeat_y":1
    },
    {
        "type":"Ground",
        "xpos": 128*21,
        "ypos": 522,
        "repeat_x": 3
    },
    {
        "type":"Wall",
        "xpos": 24*128,
        "ypos":522,
        "ground":True,
        "inverted":True,
        "repeat_y": 1
    },
    {
        "type":"Ground",
        "xpos": 128*25,
        "ypos": 650,
        "repeat_x": 18
    },
    {
        "type":"Wall",
        "xpos": 43*128,
        "ypos":522,
        "ground":True,
        "inverted":False,
        "repeat_y": 1
    },
    {
        "type":"Ground",
        "xpos": 44*128,
        "ypos": 522,
        "repeat_x": 1
    },
    {
        "type":"Wall",
        "xpos": 45*128,
        "ypos": 394,
        "ground":True,
        "inverted":False,
        "repeat_y":1
    },

    {
        "type":"Ground",
        "xpos": 46*128,
        "ypos": 394,
        "repeat_x": 2
    },
    {
        "type":"Wall",
        "xpos": 48*128,
        "ypos": 394,
        "ground":True,
        "inverted":True,
        "repeat_y":1
    },
    {
        "type":"Wall",
        "xpos": 48*128,
        "ypos": 522,
        "ground":False,
        "inverted":True,
        "repeat_y":1
    },
    {
        "type":"Ground",
        "xpos": 49*128,
        "ypos": 650,
        "repeat_x": 21
    },
    {
        "type":"Wall",
        "xpos": 60*128,
        "ypos": 522,
        "ground":False,
        "inverted":False,
        "repeat_y":5
    },
    {
        "type":"FinalBox",
        "xpos":59*128,
        "ypos":522
    }

]

level_1_visuals = [
    {
        "type":"DirtBlock",
        "xpos": -128,
        "ypos": 650,
        "inverted": True,
        "curve": True,
        "repeat_y": 1,
        "repeat_x": 1
    },
    {
        "type":"DirtBlock",
        "xpos": -(5*128),
        "ypos": 650,
        "inverted": False,
        "curve": False,
        "repeat_y": 6,
        "repeat_x": 4
    },
    {
        "type": "Sign", 
        "xpos": 0,
        "ypos": 522,
        "text":"Inicio",
        "text_pos": [20, 20]   
    },
    {
        "type": "TombStone",
        "xpos": 2*128,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 2*128 +40,
        "ypos": 522
    },
    {
        "type":"Tree",
        "xpos": 5*128,
        "ypos":  522
    },
    {
        "type": "Bush",
        "xpos": 7*128,
        "ypos": 522
    },
    {
        "type": "ArrowSign",
        "xpos": 4*128,
        "ypos": 522,
        "inverted":False
    },
    {
        "type": "TextLine",
        "xpos": 11*128 + 50, 
        "ypos": 400,
        "text":" Mission Objective:",
        "color": [214, 63,49]
    },
    {
        "type": "TextLine",
        "xpos": 11*128, 
        "ypos": 425,
        "text":"Cross the cemetery and extract",
        "color": [255, 255, 255]
    },
    {
        "type": "TextLine",
        "xpos": 11*128+50, 
        "ypos": 450,
        "text":"the virus sample",
        "color": [255, 255,255]
    },
    {
        "type": "TextLine",
        "xpos": 11*128, 
        "ypos": 475,
        "text":"for the development of the cure.",
        "color": [255, 255,255]
    },
    {
        "type": "TombStone",
        "xpos": 15*128+64,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 16*128,
        "ypos": 522
    },
    {
        "type": "Skeleton",
        "xpos": 16*128-30,
        "ypos": 522,
        "inverted": False,
    },
    {
        "type":"DirtBlock",
        "xpos": 128*20,
        "ypos": 650,
        "inverted": False,
        "curve": True,
        "repeat_y": 1,
        "repeat_x": 1
    },
    {
        "type":"Tree",
        "xpos": 128*16,
        "ypos":  522
    },
    {
        "type": "Bush",
        "xpos": 128*19+28,
        "ypos": 522
    },
    {
        "type":"DirtBlock",
        "xpos": 128*21,
        "ypos": 650,
        "inverted": False,
        "curve": False,
        "repeat_y": 1,
        "repeat_x": 3
    },
    {
        "type": "TextLine",
        "xpos": 3*128, 
        "ypos": 400,
        "text":"How to play:",
        "color": [214, 63,49]
    },
    {
        "type": "TextLine",
        "xpos": 3*128, 
        "ypos": 425,
        "text":"SPACE or UP: Jump",
        "color": [255, 255,255]
    },
    {
        "type": "TextLine",
        "xpos": 3*128, 
        "ypos": 450,
        "text":"A-D or LEFT-RIGHT: Walk",
        "color": [255, 255,255]
    },
    {
        "type": "TextLine",
        "xpos": 3*128, 
        "ypos": 475,
        "text":"LeftCtrl: Attack",
        "color": [255, 255,255]
    },
    {
        "type": "TextLine",
        "xpos": 3*128, 
        "ypos": 500,
        "text":"S or Down: Fast Attack (running)",
        "color": [255, 255,255]
    },
    {
        "type": "ArrowSign",
        "xpos": 24*128,
        "ypos": 394,
        "inverted":False
    },
    {
        "type":"DirtBlock",
        "xpos": 128*24,
        "ypos": 650,
        "inverted": True,
        "curve": True,
        "repeat_y": 1,
        "repeat_x": 1
    },
    {
        "type": 'Bone',
        "xpos": 2*128,
        "ypos": 522
    },
    {
        "type": 'Bone',
        "xpos": 7*128,
        "ypos": 550
    },
    {
        "type": 'Bone',
        "xpos": 18*128,
        "ypos": 530
    },
    {
        "type": 'Bone',
        "xpos": 21*128,
        "ypos": 394
    },
    {
        "type": "Bush",
        "xpos": 128*26,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 29*128,
        "ypos": 522
    },
    {
        "type": 'Bone',
        "xpos": 27*128,
        "ypos": 650
    },
    {
        "type":"Tree",
        "xpos": 31*128,
        "ypos":  522
    },
    {
        "type": "Bush",
        "xpos": 128*35,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 36*128,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 36*128+60,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 37*128,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 37*128+60,
        "ypos": 522
    },
    {
        "type": "ArrowSign",
        "xpos": 41*128,
        "ypos": 522,
        "inverted":False
    },
    {
        "type":"Tree",
        "xpos": 39*128,
        "ypos":  522
    },
    {
        "type":"DirtBlock",
        "xpos": 43*128,
        "ypos": 650,
        "inverted": False,
        "curve": True,
        "repeat_y": 1,
        "repeat_x": 1
    },
    {
        "type":"DirtBlock",
        "xpos": 45*128,
        "ypos": 522,
        "inverted": False,
        "curve": True,
        "repeat_y": 1,
        "repeat_x": 1
    },
    {
        "type":"DirtBlock",
        "xpos": 44*128,
        "ypos": 650,
        "inverted": False,
        "curve": False,
        "repeat_y": 1,
        "repeat_x": 4
    },
    {
        "type":"DirtBlock",
        "xpos": 46*128,
        "ypos": 522,
        "inverted": False,
        "curve": False,
        "repeat_y": 1,
        "repeat_x": 2
    },
    {
        "type":"DirtBlock",
        "xpos": 48*128,
        "ypos": 650,
        "inverted": True,
        "curve": True,
        "repeat_y": 1,
        "repeat_x": 1
    },
    {
        "type":"DirtBlock",
        "xpos": 61*128,
        "ypos": 522,
        "inverted": False,
        "curve": False,
        "repeat_y": 5,
        "repeat_x": 4
    },
    {
        "type": "Bush",
        "xpos": 44*128,
        "ypos": 394
    },
    {
        "type":"Tree",
        "xpos": 46*128,
        "ypos":  267
    },
    {
        "type": 'Bone',
        "xpos": 42*128,
        "ypos": 580
    },
    {
        "type": 'Bone',
        "xpos": 45*128,
        "ypos": 394
    },
    {
        "type": 'Bone',
        "xpos": 34*128,
        "ypos": 522
    },
    {
        "type": 'Bone',
        "xpos": 30*128,
        "ypos": 500
    },
    {
        "type": 'Bone',
        "xpos": 39*128,
        "ypos": 600
    },
    {
        "type": 'Bone',
        "xpos": 47*128,
        "ypos": 522
    },
    {
        "type":"Tree",
        "xpos": 53*128,
        "ypos":  522
    },
    {
        "type":"Tree",
        "xpos": 60*128,
        "ypos":  522
    },
    {
        "type": "Bush",
        "xpos": 52*128,
        "ypos": 522
    },
    {
        "type": "ArrowSign",
        "xpos": 51*128,
        "ypos": 522,
        "inverted":False
    },
    {
        "type": "Bush",
        "xpos": 49*128,
        "ypos": 522
    },
    {
        "type": "Bush",
        "xpos": 58*128,
        "ypos": 522
    },
    {
        "type": "TombStone",
        "xpos": 56*128,
        "ypos": 522
    },
]