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

    def is_going_back(self, update):
        text = update.message.text
        update.message.reply_text("主題：國家\n選擇：\n1.國旗猜國名\n2.國歌猜國名\n3.國家有趣介紹影片")
        return text.lower() == '返回'

#picture
    def is_going_to_picture1(self, update):
        text = update.message.text
        return text.lower() == '國旗猜國名'
    def is_going_to_picture2(self, update):
        text = update.message.text
        return text.lower() == '丹麥'
    def is_going_to_picture3(self, update):
        text = update.message.text
        return text.lower() == '挪威'
    def is_going_to_picture4(self, update):
        text = update.message.text
        return text.lower() == '瑞典'
    def is_going_to_picture5(self, update):
        text = update.message.text
        return text.lower() == '冰島'
    def is_going_to_picture6(self, update):
        text = update.message.text
        return text.lower() == '芬蘭'


#audio
    def is_going_to_audio1(self, update):
        text = update.message.text
        return text.lower() == '國歌猜國名'
    def is_going_to_audio2(self, update):
        text = update.message.text
        return text.lower() == '以色列'
    def is_going_to_audio3(self, update):
        text = update.message.text
        return text.lower() == '俄羅斯'
    def is_going_to_audio4(self, update):
        text = update.message.text
        return text.lower() == '泰國'
    def is_going_to_audio5(self, update):
        text = update.message.text
        return text.lower() == '美國'


#background
    def is_going_to_background1(self, update):
        text = update.message.text
        return text.lower() == '國家有趣介紹影片'

#final
    def is_going_to_final(self, update):
        text = update.message.text
        return text.lower() == 'go to final'

#===============================================



#ie picture
    def on_enter_picture1(self, update):
        update.message.reply_text("第1關:猜猜看，這是哪一國？")
        update.message.reply_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/141px-Flag_of_Denmark.svg.png')


    def on_exit_picture1(self, update):
        print('Leaving picture1')

    def on_enter_picture2(self, update):
        update.message.reply_text("答對了！\n第2關:猜猜看，這是哪一國？")
        update.message.reply_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/144px-Flag_of_Norway.svg.png')

    def on_exit_picture2(self, update):
        print('Leaving picture2')

    def on_enter_picture3(self, update):
        update.message.reply_text("答對了！\n第3關:猜猜看，這是哪一國？")
        update.message.reply_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Sweden.svg/155px-Flag_of_Sweden.svg.png')

    def on_exit_picture3(self, update):
        print('Leaving picture3')

    def on_enter_picture4(self, update):
        update.message.reply_text("答對了！\n第4關:猜猜看，這是哪一國？")
        update.message.reply_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Iceland.svg/144px-Flag_of_Iceland.svg.png')

    def on_exit_picture4(self, update):
        print('Leaving picture4')

    def on_enter_picture5(self, update):
        update.message.reply_text("答對了！\n第5關:猜猜看，這是哪一國？")
        update.message.reply_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/156px-Flag_of_Finland.svg.png')

    def on_exit_picture5(self, update):
        print('Leaving picture5')

    def on_enter_picture6(self, update):
        update.message.reply_text("Win！")
        update.message.reply_photo(photo='')

    def on_exit_picture6(self, update):
        print('Leaving picture6')

#ie audio
    def on_enter_audio1(self, update):
        update.message.reply_text("第1關：聽聽看，這是什麼國家的國歌？（可能需稍等幾秒）")
        update.message.reply_audio(audio=open('audio/1.mp3','rb'))

    def on_exit_audio1(self, update):
        print('Leaving audio1')

    def on_enter_audio2(self, update):
        update.message.reply_text("答對了！\n第2關：聽聽看，這是什麼國家的國歌？（可能需稍等幾秒）")
        update.message.reply_audio(audio=open('audio/2.mp3','rb'))

    def on_exit_audio2(self, update):
        print('Leaving audio2')

    def on_enter_audio3(self, update):
        update.message.reply_text("答對了！\n第3關：聽聽看，這是什麼國家的國歌？（可能需稍等幾秒）")
        update.message.reply_audio(audio=open('audio/3.mp3','rb'))

    def on_exit_audio3(self, update):
        print('Leaving audio3')

    def on_enter_audio4(self, update):
        update.message.reply_text("答對了！\n第4關：聽聽看，這是什麼國家的國歌？（可能需稍等幾秒）")
        update.message.reply_audio(audio=open('audio/4.mp3','rb'))

    def on_exit_audio4(self, update):
        print('Leaving audio3')

    def on_enter_audio5(self, update):
        update.message.reply_text("Win!")

    def on_exit_audio5(self, update):
        print('Leaving audio3')


#ie background
    def on_enter_background1(self, update):
        button_list = [
        InlineKeyboardButton("youtube",callback_data='1',url='https://www.youtube.com/watch?v=y41eIfwQYtQ'),
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        update.message.reply_text("三色條紋國旗的有趣歷史", reply_markup=reply_markup)


    def on_exit_background1(self, update):
        print('Leaving background1')




