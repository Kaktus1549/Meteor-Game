#importy

from play import *
from random import randint


#promene

lets_go_back = 0
new_skin = 0
which_raketa = 1
cz_on = 0
eng_on = 1
sp_on = 0
wanna_cz = 0
wanna_eng = 1
wanna_sp = 0
no_more_lang = 0
change_lang = 0
back_to_lobby_2 = 0
set_box_yes = 0
in_lobby = 0
lobby = 0
tut_part = 0
tut_box_clicked = 0
play_button_pressed = 0
restart_box_cration = 1
nahoda = 0
player_failed = 0
i = 1
meteor_shape = 1
meteorss = []
down_border = play.new_box(x = 0, y = -300, height = 5, width = 800, transparency = 100)
#postava

raketa_1 = play.new_image("Postavicka/Player/up.png", x = 0, y = -250)
raketa_1.hide()
raketa_2 = play.new_image("Postavicka/Player2/up.png", x = 0, y = -250)
raketa_2.hide()
raketa_3 = play.new_image("Postavicka/Player3/up.png", x = 0, y = -250)
raketa_3.hide()

#pozadi + boxy
play.set_backdrop("Red")
Welcome_text = play.new_text(words="Welcome to the Meteors!")
Welcome_box = play.new_box(height= 80, width= 180, transparency= 50, color= "yellow", x = 0, y = -70)
Welcome_play = play.new_text(words="Continue", x= 0, y= -70)

meteor_box = play.new_box(width = 280, height = 100, x = 0, y = 110, transparency = 20, color = "white")
sett_box = play.new_box(width = 280, height = 100, x = 0, y = 0, transparency = 20, color = "white")
tut_box = play.new_box(width = 280, height = 100, x = 0, y = -110, transparency = 20, color = "white")
meteor_text = play.new_text("Start game", x = 0, y = 110)
sett_text = play.new_text("Settings", x = 0, y = 0)
tut_text = play.new_text("Tutorial", x = 0, y = -110)
next_button = play.new_box(x = 220, y = -250, height=80, width= 180, transparency= 20, color= "White")
next_txt = play.new_text(x = 220 , y = -250, words= "Next")
tut_image_cz = play.new_image("Tutorial/Cz/Player.png", x = 0, y = 50)
tut_image_cz.hide()
tut_image_2_cz = play.new_image("Tutorial/Cz/meteory.png", x = 0 , y = 30)
tut_image_2_cz.hide()
tut_image_3_cz = play.new_image("Tutorial/Cz/konec.png", x = 0, y = 30)
tut_image_3_cz.hide()
tut_back_to_lobby_button = play.new_box(x = 220, y = -260, height= 70, width= 240, color= "White", transparency= 20)
tut_back_to_lobby_txt = play.new_text(words="Back to lobby", x = 220, y= -260)
restart_box = play.new_box(x = 190, y = -70, height= 70, width= 260, color = "White", transparency= 10)
restart_tex = play.new_text(x = 190, y = -70, words= "Play again")
back_to_lobby_box = play.new_box(x = -190, y = -70, height= 70, width= 260, color = "White", transparency= 10)
back_to_lobby_text = play.new_text(x  = -190, y = -70, words= "Back to lobby")
clear_box = play.new_box(width= 900, height= 800, transparency= 0)
GAME_OVER_LOL = play.new_text("Game Over!", x= 0, y= 0, color= "White")
skin = play.new_box(width = 280, height = 100, x = 0, y = 110, transparency = 20, color = "white")
language = play.new_box(width = 280, height = 100, x = 0, y = 0, transparency = 20, color = "white")
idk_box = play.new_box(width = 280, height = 100, x = 0, y = -110, transparency = 20, color = "white")
skin_text = play.new_text("Skins", x = 0, y = 110)
language_text = play.new_text("Language", x = 0, y = 0)
idk_text = play.new_text("???", x = 0, y = -110)
back_to_lobby_box_2 = play.new_box(x = 200, y =-240, height= 70, width= 260, color = "White", transparency= 10)
back_to_lobby_text_2 = play.new_text(x  = 200, y = -240, words= "Back to lobby")
eng = play.new_box(width = 280, height = 100, x = 0, y = 110, transparency = 50, color = "white")
cz = play.new_box(width = 280, height = 100, x = 0, y = 0, transparency = 20, color = "white")
sp = play.new_box(width = 280, height = 100, x = 0, y = -110, transparency = 20, color = "white")
eng_text = play.new_text("English", x = 0, y = 110)
cz_text = play.new_text("Čeština", x = 0, y = 0)
sp_text = play.new_text("En español", x = 0, y = -110)
back_to_lobby_box_3 = play.new_box(x = 200, y =-240, height= 70, width= 300, color = "White", transparency= 10)
back_to_lobby_text_3 = play.new_text(x  = 200, y = -240, words= "Back to settings")
tut_image_eng = play.new_image("Tutorial/Eng/Player.png", x = 0, y = 50)
tut_image_eng.hide()
tut_image_2_eng = play.new_image("Tutorial/Eng/Meteors.png", x = 0 , y = 30)
tut_image_2_eng.hide()
tut_image_3_eng = play.new_image("Tutorial/Eng/Play_again.png", x = 0, y = 30)
tut_image_3_eng.hide()
tut_image_sp = play.new_image("Tutorial/SP/player.png", x = 0, y = 50)
tut_image_sp.hide()
tut_image_2_sp = play.new_image("Tutorial/SP/meteors.png", x = 0 , y = 30)
tut_image_2_sp.hide()
tut_image_3_sp = play.new_image("Tutorial/SP/play_again.png", x = 0, y = 30)
tut_image_3_sp.hide()
back_from_skin_box = play.new_box(x = 200, y =-240, height= 70, width= 300, color = "White", transparency= 10)
back_from_skin = play.new_text(x  = 200, y = -240, words= "Back to settings")
choose_your_skin = play.new_text(words= "Select your new skin!", x = 0 , y = 270, color= "white")
first_skin = play.new_image("Postavicka/choosing/up.png", x = 00, y= 0, transparency= 50)
second_skin = play.new_image("Postavicka/choosing/up2.png", y = 0, x = -190, transparency= 20)
third_skin = play.new_image("Postavicka/choosing/up3.png", y = 0, x = 190, transparency= 20)

first_skin.hide()
second_skin.hide()
third_skin.hide()
choose_your_skin.hide()
back_from_skin.hide()
back_from_skin_box.hide()
GAME_OVER_LOL.hide()
clear_box.hide()
back_to_lobby_box.hide()
back_to_lobby_text.hide()
restart_box.hide()
restart_tex.hide()
tut_back_to_lobby_button.hide()
tut_back_to_lobby_txt.hide()
next_txt.hide()
next_button.hide()
meteor_box.hide()
meteor_text.hide()
tut_box.hide()
tut_text.hide()
sett_text.hide()
sett_box.hide()
language.hide()
language_text.hide()
skin.hide()
skin_text.hide()
idk_box.hide()
idk_text.hide()
back_to_lobby_box_2.hide()
back_to_lobby_text_2.hide()
eng.hide()
eng_text.hide()
cz.hide()
cz_text.hide()
sp.hide()
sp_text.hide()
back_to_lobby_box_3.hide()
back_to_lobby_text_3.hide()

#uplny zacatek
@Welcome_box.when_clicked
def click_box():
    global Welcome_text
    global Welcome_box
    global Welcome_play
    global meteor_box
    global meteor_text
    global tut_box
    global tut_text
    global sett_box
    global sett_text
    global tut_part
    global next_button
    global next_txt
    global GAME_OVER_LOL

    play.set_backdrop("Black")
    Welcome_text.remove()
    Welcome_box.remove()
    Welcome_play.remove()
    meteor_box.show()
    meteor_text.show()
    tut_box.show()
    tut_text.show()
    sett_text.show()
    sett_box.show()

@meteor_box.when_clicked
def meteor_box_click():
    global play_button_pressed

    play_button_pressed = 1

@tut_box.when_clicked
def tut_box_click():
    global tut_part
    global tut_box_clicked
    
    tut_box_clicked = 1
    tut_part = 1

@next_button.when_clicked
def abc():
    global tut_part

    tut_part = tut_part + 1

@tut_back_to_lobby_button.when_clicked
def tutu_clck():
    global tut_part
    tut_part = 0

@restart_box.when_clicked
def res_box_click():
    global restart_box_cration
    restart_box_cration = 0  

@back_to_lobby_box.when_clicked
def back_to_obby():
    global lobby
    lobby = 1

@sett_box.when_clicked
def set_boxik():
    global set_box_yes
    set_box_yes = 1

@back_to_lobby_box_2.when_clicked
def ahhh_yes():
    global back_to_lobby_2
    back_to_lobby_2 = 1

@language.when_clicked
def lang_click():
    global change_lang
    change_lang = 1

@back_to_lobby_box_3.when_clicked
def back_lobby_3():
    global no_more_lang
    no_more_lang = 1

@cz.when_clicked
def cz_click():
    global wanna_eng
    global wanna_cz
    global wanna_sp
    wanna_eng = 0
    wanna_sp = 0
    wanna_cz = 1

@eng.when_clicked
def eng_click():
    global wanna_eng
    global wanna_cz
    global wanna_sp
    wanna_eng = 1
    wanna_sp = 0
    wanna_cz = 0
@sp.when_clicked
def sp_clickk():
    global wanna_eng
    global wanna_cz
    global wanna_sp
    wanna_eng = 0
    wanna_sp = 1
    wanna_cz = 0

@skin.when_clicked
def change_skin():
    global new_skin
    new_skin = 1

@back_from_skin_box.when_clicked
def yeah():
    global lets_go_back
    if lets_go_back == 0:
        lets_go_back = 1

@first_skin.when_clicked
def first_click():
    global which_raketa
    first_skin.transparency = 50
    second_skin.transparency = 20
    third_skin.transparency = 20
    which_raketa = 1

@second_skin.when_clicked
def sec_click():
    global which_raketa
    first_skin.transparency = 20
    second_skin.transparency = 50
    third_skin.transparency = 20
    which_raketa = 2

@third_skin.when_clicked
def thirdt_click():
    global which_raketa
    first_skin.transparency = 20
    second_skin.transparency = 20
    third_skin.transparency = 50
    which_raketa = 3

@play.repeat_forever
def hi():
    global i
    global f
    global nahoda
    global player_failed
    global restart_box_cration
    global restart_box
    global restart_text
    global raketa
    global tut_part
    global tut_image
    global tut_image_2
    global next_button
    global restart_box
    global restart_tex
    global back_to_lobby_box
    global back_to_lobby_text
    global lobby
    global in_lobby
    global play_button_pressed
    global back_to_lobby_2
    global set_box_yes
    global no_more_lang
    global change_lang
    global wanna_cz
    global wanna_eng
    global wanna_sp
    global cz_on
    global eng_on
    global sp_on
    global new_skin
    global lets_go_back

    if tut_box_clicked == 1:

        meteor_box.hide()
        meteor_text.hide()
        tut_box.hide()
        tut_text.hide()
        sett_text.hide()
        sett_box.hide()
        

        if cz_on == 1:
            next_txt.show()
            next_button.show()
            if tut_part == 0:
                tut_image_3_cz.hide()
                tut_back_to_lobby_button.hide()
                tut_back_to_lobby_txt.hide()
                meteor_box.show()
                meteor_text.show()
                tut_box.show()
                tut_text.show()
                sett_text.show()
                sett_box.show()
                tut_part = 0
                next_txt.hide()
                next_button.hide() 
                
            if tut_part == 1:
                tut_image_cz.show()
            
            if tut_part ==2:
                tut_image_cz.hide()
                tut_image_2_cz.show()
            if tut_part == 3:
                tut_image_2_cz.hide()
                tut_image_3_cz.show()
                next_txt.hide()
                next_button.hide() 
                tut_back_to_lobby_button.show()
                tut_back_to_lobby_txt.show()
        if eng_on == 1:
            next_txt.show()
            next_button.show()
            if tut_part == 0:
                tut_image_3_eng.hide()
                tut_back_to_lobby_button.hide()
                tut_back_to_lobby_txt.hide()
                meteor_box.show()
                meteor_text.show()
                tut_box.show()
                tut_text.show()
                sett_text.show()
                sett_box.show()
                tut_part = 0
                next_txt.hide()
                next_button.hide() 
                
            if tut_part == 1:
                tut_image_eng.show()
            
            if tut_part ==2:
                tut_image_eng.hide()
                tut_image_2_eng.show()
            if tut_part == 3:
                tut_image_2_eng.hide()
                tut_image_3_eng.show()
                next_txt.hide()
                next_button.hide() 
                tut_back_to_lobby_button.show()
                tut_back_to_lobby_txt.show()
        if sp_on == 1:
            next_txt.show()
            next_button.show()
            if tut_part == 0:
                tut_image_3_sp.hide()
                tut_back_to_lobby_button.hide()
                tut_back_to_lobby_txt.hide()
                meteor_box.show()
                meteor_text.show()
                tut_box.show()
                tut_text.show()
                sett_text.show()
                sett_box.show()
                tut_part = 0
                next_txt.hide()
                next_button.hide() 
                
            if tut_part == 1:
                tut_image_sp.show()
            
            if tut_part ==2:
                tut_image_sp.hide()
                tut_image_2_sp.show()
            if tut_part == 3:
                tut_image_2_sp.hide()
                tut_image_3_sp.show()
                next_txt.hide()
                next_button.hide() 
                tut_back_to_lobby_button.show()
                tut_back_to_lobby_txt.show()
        
        
    
    
    
    
    if play_button_pressed == 1:
        
        meteor_box.hide()
        meteor_text.hide()
        tut_box.hide()
        tut_text.hide()
        sett_text.hide()
        sett_box.hide()
        if which_raketa == 1:
            raketa_1.show()
        if which_raketa == 2:
            raketa_2.show()
        if which_raketa == 3:
            raketa_3.show()
        if player_failed == 0:
            nahoda = randint(1, 100)
        if player_failed == 0:    
            if which_raketa == 1:
                if play.key_is_pressed("a") and not play.key_is_pressed("d") and not raketa_1.x == -400:
                    raketa_1.image = ("Postavicka/Player/left.png")
                    raketa_1.x = raketa_1.x - 5
                if play.key_is_pressed("d") and not play.key_is_pressed("a") and not raketa_1.x == 400:
                    raketa_1.image = ("Postavicka/Player/right.png")
                    raketa_1.x = raketa_1.x + 5
                if  not play.key_is_pressed("a") and not play.key_is_pressed("d"):
                    raketa_1.image = ("Postavicka/Player/up.png")
            if which_raketa == 2:
                if play.key_is_pressed("a") and not play.key_is_pressed("d") and not raketa_2.x == -400:
                    raketa_2.image = ("Postavicka/Player2/left.png")
                    raketa_2.x = raketa_2.x - 5
                if play.key_is_pressed("d") and not play.key_is_pressed("a") and not raketa_2.x == 400:
                    raketa_2.image = ("Postavicka/Player2/right.png")
                    raketa_2.x = raketa_2.x + 5
                if  not play.key_is_pressed("a") and not play.key_is_pressed("d"):
                    raketa_2.image = ("Postavicka/Player2/up.png")
            if which_raketa == 3:
                if play.key_is_pressed("a") and not play.key_is_pressed("d") and not raketa_3.x == -400:
                    raketa_3.image = ("Postavicka/Player3/left.png")
                    raketa_3.x = raketa_3.x - 5
                if play.key_is_pressed("d") and not play.key_is_pressed("a") and not raketa_3.x == 400:
                    raketa_3.image = ("Postavicka/Player3/right.png")
                    raketa_3.x = raketa_3.x + 5
                if  not play.key_is_pressed("a") and not play.key_is_pressed("d"):
                    raketa_3.image = ("Postavicka/Player3/up.png")

        
        if i == 1 and nahoda == 2 or nahoda == 5 or nahoda == 10 and player_failed == 0:
            

            meteor_shape = randint(1, 3)
            if meteor_shape == 1:
                meteor = play.new_image("Meteory_druhy/1.png", x = randint (-389, 389), y = 300)
            elif meteor_shape == 2:
                meteor = play.new_image("Meteory_druhy/2.png", x = randint (-389, 389), y = 300)
            elif meteor_shape == 3:
                meteor = play.new_image("Meteory_druhy/3.png", x = randint (-389, 389), y = 300)
            meteorss.append(meteor)
        
        
            
        f = 0
        if player_failed == 0:
            for meteor in meteorss:
                meteor.y = meteor.y - 6
            for meteor in meteorss:
                if meteor.y == -350:
                    meteor.remove()
                if which_raketa == 1:
                    if raketa_1.is_touching(meteor):
                        player_failed = 1 
                if which_raketa == 2:
                    if raketa_2.is_touching(meteor):
                        player_failed = 1    
                if which_raketa == 3:
                    if raketa_3.is_touching(meteor):
                        player_failed = 1      
                
                f = f + 1
        if player_failed == 1:
            GAME_OVER_LOL.show()
            back_to_lobby_text.show()
            back_to_lobby_box.show()
            restart_box.show()
            restart_tex.show()
            if restart_box_cration == 0:
                for meteor in meteorss:
                    if raketa_1.is_touching(meteor):
                        meteor.y = -350
                    if meteor.is_touching(clear_box):
                        meteor.y = -350
                raketa_1.x = 0
                raketa_1.y = -250
                raketa_2.x = 0
                raketa_2.y = -250
                raketa_3.x = 0
                raketa_3.y = -250
                back_to_lobby_text.hide()
                back_to_lobby_box.hide()
                restart_box.hide()
                restart_tex.hide()
                GAME_OVER_LOL.hide()
                raketa_1.image = ("Postavicka/up.png")
                player_failed = 0
                restart_box_cration = 1
        if lobby == 1:
            back_to_lobby_text.hide()
            back_to_lobby_box.hide()
            restart_box.hide()
            restart_tex.hide()
            GAME_OVER_LOL.hide()
            raketa_1.hide()
            raketa_2.hide()
            raketa_3.hide()
            lobby = 0
            play_button_pressed = 0
            player_failed = 0
            for meteor in meteorss:
                if raketa_1.is_touching(meteor):
                    meteor.y = -350
                if meteor.is_touching(clear_box):
                    meteor.y = -350
            meteor_box.show()
            meteor_text.show()
            tut_box.show()
            tut_text.show()
            sett_text.show()
            sett_box.show()
            for meteor in meteorss:
                meteor.y = meteor.y - 6
            for meteor in meteorss:
                if meteor.y == -350:
                    meteor.remove()
            raketa_1.image = ("Postavicka/Player/up.png")
            raketa_1.x = 0
            raketa_1.y = -250
   
    if set_box_yes == 1:
        meteor_box.hide()
        meteor_text.hide()
        tut_box.hide()
        tut_text.hide()
        sett_text.hide()
        sett_box.hide()
        language.show()
        language_text.show()
        skin.show()
        skin_text.show()
        idk_box.show()
        idk_text.show()
        back_to_lobby_box_2.show()
        back_to_lobby_text_2.show()
    if back_to_lobby_2 ==1:
        language.hide()
        language_text.hide()
        skin.hide()
        skin_text.hide()
        idk_box.hide()
        idk_text.hide()
        back_to_lobby_box_2.hide()
        back_to_lobby_text_2.hide()
        meteor_box.show()
        meteor_text.show()
        tut_box.show()
        tut_text.show()
        sett_text.show()
        sett_box.show()
        back_to_lobby_2 = 0
        set_box_yes = 0
    if change_lang == 1:
        language.hide()
        language_text.hide()
        skin.hide()
        skin_text.hide()
        idk_box.hide()
        idk_text.hide()
        back_to_lobby_box_2.hide()
        back_to_lobby_text_2.hide()
        cz.show()
        cz_text.show()
        eng.show()
        eng_text.show()
        sp.show()
        sp_text.show()
        back_to_lobby_box_3.show()
        back_to_lobby_text_3.show()
    if no_more_lang == 1:
        meteor_box.hide()
        meteor_text.hide()
        tut_box.hide()
        tut_text.hide()
        sett_text.hide()
        sett_box.hide()
        language.show()
        language_text.show()
        skin.show()
        skin_text.show()
        idk_box.show()
        idk_text.show()
        back_to_lobby_box_2.show()
        back_to_lobby_text_2.show()
        eng.hide()
        eng_text.hide()
        cz.hide()
        cz_text.hide()
        sp.hide()
        sp_text.hide()
        back_to_lobby_box_3.hide()
        back_to_lobby_text_3.hide()
        no_more_lang = 0
        change_lang = 0
    if wanna_cz == 1:
        wanna_eng = 0
        wanna_sp = 0
        eng.transparency = 20
        sp.transparency = 20
        cz.transparency = 50
        wanna_cz = 0
        back_to_lobby_text_3.words = "Zpět do nastavení"
        back_to_lobby_box_3.width = 300
        back_to_lobby_text_2.words = "Zpět do lobby"
        back_to_lobby_box_2.width = 280
        skin_text.words = "Skiny"
        language_text.words = "Jazyk"
        meteor_text.words = "Začít hru"
        meteor_box.width = 280
        next_txt.words = "Další"
        back_to_lobby_text.words = "Zpět do lobby"
        back_to_lobby_box.width = 280
        sett_text.words = "Nastavení"
        sett_box.width = 280
        tut_back_to_lobby_txt.words = "Zpět do lobby"
        tut_back_to_lobby_button.width = 280
        restart_tex.words = "Hrát znovu"
        GAME_OVER_LOL.words = "Hra skončila"
        cz_on = 1
        back_from_skin.words = "Zpět do nastavení"
        back_from_skin_box.width = 300
        choose_your_skin.words = "Vyberte svůj skin!"
    if wanna_eng == 1:
        wanna_cz = 0
        wanna_sp = 0
        eng.transparency = 50
        sp.transparency = 20
        cz.transparency = 20
        wanna_eng = 0
        back_to_lobby_text_3.words = "Back to settings"
        back_to_lobby_box_3.width = 280
        back_to_lobby_text_2.words = "Back to lobby"
        back_to_lobby_box_2.width = 280
        skin_text.words = "Skins"
        language_text.words = "Language"
        meteor_text.words = "Start game"
        meteor_box.width = 280
        next_txt.words = "Next"
        back_to_lobby_text.words = "Back to lobby"
        back_to_lobby_box.width = 280
        sett_text.words = "Settings"
        sett_box.width = 280
        tut_back_to_lobby_txt.words = "Back to lobby!"
        tut_back_to_lobby_button.width = 280
        restart_tex.words = "Play again!"
        GAME_OVER_LOL.words = "Game over!"
        eng_on = 1
        back_from_skin.words = "Back to settings"
        back_from_skin_box.width = 280
        choose_your_skin.words = "Choose your skin!"
    if wanna_sp == 1:
        wanna_eng = 0
        wanna_sp = 0
        eng.transparency = 20
        sp.transparency = 50
        cz.transparency = 20
        wanna_sp = 0
        back_to_lobby_text_3.words = "Volver a la configuración"
        back_to_lobby_box_3.width = 410
        back_to_lobby_text_2.words = "Volver al vestíbulo"
        back_to_lobby_box_2.width = 320
        skin_text.words = "Looks"
        language_text.words = "Idioma"
        meteor_text.words = "Iniciar el juego"
        meteor_box.width = 320
        next_txt.words = "Siguiente"
        back_to_lobby_text.words = "Volver al vestíbulo"
        back_to_lobby_box.width = 320
        sett_text.words = "Configuración"
        sett_box.width = 320
        tut_back_to_lobby_txt.words = "Volver al vestíbulo"
        tut_back_to_lobby_button.width = 320
        restart_tex.words = "Volver a jugar"
        GAME_OVER_LOL.words = "Fin del juego"
        sp_on = 1
        back_from_skin.words = "Volver a la configuración"
        back_from_skin_box.width = 410
        choose_your_skin.words = "Elige tu look!"
    if sp_on == 1:
        eng_on = 0
        cz_on = 0
    if cz_on == 1:
        eng_on = 0
        sp_on = 0
    if eng_on == 1:
        sp_on = 0
        cz_on = 0

    if new_skin == 1:
        skin.hide()
        skin_text.hide()
        language.hide()
        language_text.hide()
        idk_box.hide()
        idk_text.hide()
        back_to_lobby_box_2.hide()
        back_to_lobby_text_2.hide()
        back_from_skin_box.show()
        back_from_skin.show()
        choose_your_skin.show()
        first_skin.show()
        second_skin.show()
        third_skin.show()


    if lets_go_back == 1:
        skin.show()
        skin_text.show()
        language.show()
        language_text.show()
        idk_box.show()
        idk_text.show()
        back_to_lobby_box_2.show()
        back_to_lobby_text_2.show()
        back_from_skin_box.hide()
        back_from_skin.hide()
        lets_go_back = 0
        new_skin = 0
        choose_your_skin.hide()
        first_skin.hide()
        second_skin.hide()
        third_skin.hide()

play.start_program()