from transitions.extensions import GraphMachine
from telegram import InlineKeyboardButton,InlineKeyboardMarkup

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

 
#勝利校區=========== up ================== 
    def is_going_to_sheng(self, update):
        text = update.message.text
        return text.lower() == '下'

    def sheng_back_to_initial(self, update):
        text = update.message.text
        return text.lower() == '上'


    def is_going_to_sheng(self, update):
        text = update.message.text
        return text.lower() == '下'

#勝利校區=========== down ================== 
    def is_going_back_sheng(self, update):
        text = update.message.text
        return text.lower() == '上'




#成功校區=========== up ================== 
    def is_going_to_cheng(self, update):
        text = update.message.text
        return text.lower() == '上'

    def cheng_back_to_initial(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_to_cheng1(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_cheng2(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_cheng3(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_cheng4(self, update):
        text = update.message.text
        return text.lower() == '上'
    def is_going_to_cheng5(self, update):
        text = update.message.text
        return text.lower() == '上'
    def is_going_to_cheng6(self, update):
        text = update.message.text
        return text.lower() == '上'
    def is_going_to_cheng7(self, update):
        text = update.message.text
        return text.lower() == '上'

#成功校區=========== down ================== 
    def is_going_back_cheng(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_cheng1(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_cheng2(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_cheng3(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_cheng4(self, update):
        text = update.message.text
        return text.lower() == '下'
    def is_going_back_cheng5(self, update):
        text = update.message.text
        return text.lower() == '下'
    def is_going_back_cheng6(self, update):
        text = update.message.text
        return text.lower() == '下'



#光復校區=========== up ================== 
    def is_going_to_koan(self, update):
        text = update.message.text
        return text.lower() == '左'

    def koan_back_to_initial(self, update):
        text = update.message.text
        return text.lower() == '右'


    def is_going_to_koan1(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_koan2(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_music(self, update):
        text = update.message.text
        return text.lower() == '想'


    def is_going_to_koan3(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_koan4(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_koan5(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_koan6(self, update):
        text = update.message.text
        return text.lower() == '上'

#光復校區=========== down ================== 
    def is_going_back_koan(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_koan1(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_koan2(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_koan3(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_koan4(self, update):
        text = update.message.text
        return text.lower() == '下'

    def is_going_back_koan5(self, update):
        text = update.message.text
        return text.lower() == '下'


#自強校區=========== up ================== 
    def is_going_to_zi(self, update):
        text = update.message.text
        return text.lower() == '右'

    def zi_back_to_initial(self, update):
        text = update.message.text
        return text.lower() == '左'



    def is_going_to_zi1(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_zi2(self, update):
        text = update.message.text
        return text.lower() == '上'

    def is_going_to_zi3(self, update):
        text = update.message.text
        return text.lower() == '上'

#自強校區=========== down ================== 
    def is_going_back_zi(self, update):
        text = update.message.text
        return text.lower() == '下'


    def is_going_back_zi1(self, update):
        text = update.message.text
        return text.lower() == '下'
    def is_going_back_zi2(self, update):
        text = update.message.text
        return text.lower() == '下'



#===============================================

    def on_enter_initial(self, update):
        text = update.message.text
        update.message.reply_text("原點")
        update.message.reply_photo(photo=open('img/initial.jpg', 'rb'))

#勝利校區 
    def on_enter_sheng(self, update):
        text = update.message.text
        update.message.reply_text("進入勝利校區")
        update.message.reply_photo(photo=open('img/sheng.jpg', 'rb'))

    def on_enter_dorm(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("住宿服務組",callback_data='1',url='http://housing.osa.ncku.edu.tw/bin/home.php?Lang=zh-tw')
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/drom.jpg', 'rb'))
        update.message.reply_text("學生宿舍 ", reply_markup=reply_markup)

#成功校區
    def on_enter_cheng(self, update):
        text = update.message.text
        update.message.reply_text("進入成功校區")
        update.message.reply_photo(photo=open('img/cheng.jpg', 'rb'))

    def is_going_to_cheng1(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：博物館",callback_data='1',url='http://museum.ncku.edu.tw/bin/home.php'),
            InlineKeyboardButton("右邊：工科系館",callback_data='1',url='http://www.es.ncku.edu.tw/esncku/zh/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng1.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_cheng2(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：物理系館",callback_data='1',url='http://www.phys.ncku.edu.tw/2012/en/'),
            InlineKeyboardButton("右邊：資訊系館",callback_data='1',url='http://www.csie.ncku.edu.tw/ncku_csie/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng2.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_cheng3(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：化學系館",callback_data='1',url='http://web.che.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：資源系館",callback_data='1',url='http://www.mp.ncku.edu.tw/bin/home.php'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng3.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_cheng4(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：測量系館",callback_data='1',url='http://www.geomatics.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：材料系館",callback_data='1',url='http://www.mse.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng4.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_cheng5(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("右邊：土木系館",callback_data='1',url='http://www.civil.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng5.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_cheng6(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：總圖書館",callback_data='1',url='http://www.lib.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：環工系館",callback_data='1',url='http://www.ev.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng6.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_cheng7(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：生科系館",callback_data='1',url='http://www.bio.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：水利系館",callback_data='1',url='http://www.mse.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/cheng7.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)


#光復校區
    def on_enter_koan(self, update):
        text = update.message.text
        update.message.reply_text("進入光復校區")
        update.message.reply_photo(photo=open('img/koan.jpg', 'rb'))
        return text.lower() == '左'

    def on_enter_koan1(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：球場",callback_data='1',url='http://pe.acad.ncku.edu.tw/bin/home.php?Lang=zh-tw'),
            InlineKeyboardButton("右邊：中正堂",callback_data='1',url='http://cet.acad.ncku.edu.tw/ste/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/koan1.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_koan2(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：學生活動中心",callback_data='1',url='https://www.youtube.com/watch?v=rZ-6lh8YJig'),
            InlineKeyboardButton("右邊：管理學院",callback_data='1',url='http://www.management.ncku.edu.tw/main.php'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/koan2.jpg', 'rb'))
        update.message.reply_text("想聽聽成大國樂舍的表演嘛~？")
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_music(self, update):
        update.message.reply_text("傳送音樂中...")
        update.message.reply_audio(audio=open('audio/2016.mp3','rb'))
        self.go_back(update)

    def on_enter_koan3(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：唯農大樓",callback_data='1',url='http://www.ives.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：雲平大樓",callback_data='1',url='http://web.ncku.edu.tw/files/11-1000-166.php?Lang=zh-tw'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/koan3.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_koan4(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：工設系館",callback_data='1',url='http://www.ide.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：歷史系館",callback_data='1',url='http://www.his.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/koan4.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_koan5(self, update):
        text = update.message.text
        update.message.reply_photo(photo=open('img/koan5.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_koan6(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：都計系館",callback_data='1',url='http://www.up.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：修齊大樓",callback_data='1',url='http://www.flld.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/koan6.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)


#自強校區
    def on_enter_zi(self, update):
        text = update.message.text
        update.message.reply_text("進入自強校區")
        update.message.reply_photo(photo=open('img/zi.jpg', 'rb'))

    def on_enter_zi1(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：電機系館",callback_data='1',url='http://www.ee.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：系統系館",callback_data='1',url='http://w3.sname.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/zi1.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_zi2(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("左邊：化工系館",callback_data='1',url='http://web.che.ncku.edu.tw/'),
            InlineKeyboardButton("右邊：機械系館",callback_data='1',url='http://www.me.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_photo(photo=open('img/zi2.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)

    def on_enter_zi3(self, update):
        text = update.message.text
        button_list = [
            InlineKeyboardButton("自強操場",callback_data='1',url='http://www.up.ncku.edu.tw/'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        update.message.reply_photo(photo=open('img/zi3.jpg', 'rb'))
        update.message.reply_text("附近建築：", reply_markup=reply_markup)




