import pickle
import array
import telebot
from telebot import types
import atexit
import time
import signal
import datetime as dt

def keyboardInterruptHandler(signal, frame):
    exit_handler
    exit(0)


signal.signal(signal.SIGINT, keyboardInterruptHandler)

def exit_handler():
    pickle_out = open("dict.pickle","wb")
    pickle.dump(dic3, pickle_out)
    pickle_out.close()
    print('pickle out')

atexit.register(exit_handler)
try:
    bot = telebot.TeleBot("1101622297:AAFpEMajq2h9pcgm3Ti77AhXMFCwQFJwDk0")

    X=6
    Y=7
    LargeWhiteSquare = u'\U00002B1C'
    RedCircle = u'\U0001F534'
    BlueCircle = u'\U0001F535'
    BlackCircle= u'\U000026AB'

    class MESSAGE:
        def __init__(self):
            ch1='sac'
            ch2='sacsa'
            turn=0
            flag=False
            id1=0
            id2=0
            Time=dt.datetime.now()
    #arr= array.array('i',[5,5,5,5,5,5,5])
    map = [[False for x in range(Y)] for y in range(X)]
    dic ={}
    dic1={}
    dic2={}
    dic3={}
    print('pickle loaded')
    pickle_in = open("dict.pickle","rb")
    dic3 = pickle.load(pickle_in)
    pickle_in.close()
    #dic_ch1={}
    #dic_ch2={}
    #dic_turn={}
    #dic_flag={}
    def makeKeyboard(callm):
        #print(callm)
        markup = types.InlineKeyboardMarkup(row_width=7)
        for i in range(X):
            key=str(i)
            markup.add(types.InlineKeyboardButton(text=dic1[callm][key+'0'],
                                                  callback_data=key+'0'),
                       types.InlineKeyboardButton(text=dic1[callm][key+'1'],
                                                  callback_data=key+'1'),
                       types.InlineKeyboardButton(text=dic1[callm][key+'2'],
                                                  callback_data=key+'2'),
                       types.InlineKeyboardButton(text=dic1[callm][key+'3'],
                                                  callback_data=key+'3'),
                       types.InlineKeyboardButton(text=dic1[callm][key+'4'],
                                                  callback_data=key+'4'),
                       types.InlineKeyboardButton(text=dic1[callm][key+'5'],
                                                  callback_data=key+'5'),
                       types.InlineKeyboardButton(text=dic1[callm][key+'6'],
                                                  callback_data=key+'6'),)
        markup.add(types.InlineKeyboardButton(text='end the game',
                                                  callback_data='end'))
        #print('be tahesham ke resid')
        return markup

    def makeKeyboard1():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='start',
                                                  callback_data='nothing'))
        return markup

    #@bot.message_handler(commands=['play'])
    #def handle_command_adminwindow(message):
    #    smessage = bot.send_message(chat_id=message.chat.id,
    #                     text="play dooz:first 4 pieces consecutively in a (row or column or diagonal) wins the game",
    #                     reply_markup=makeKeyboard1(),
    #                     parse_mode='HTML')
    #    msg=MESSAGE()
    #    if message.from_user.username!=None:
    #        msg.ch1='@'+message.from_user.username
    #    else :
    #        msg.ch1=message.from_user.first_name
    #    msg.id1=message.from_user.id
    #    dic2[smessage.message_id]=msg


    def all_right(x,y):
        if x<X and y<Y and x>=0 and y>=0:
            return True
        else:
            return False

    def winer(x,y,dirx,diry,callm):
        for i in range(4):
            s=str(x+dirx*i)+str(y+diry*i)
            dic1[callm][s]=BlackCircle

    def check(x,y,callm):
        s1=str(x)+str(y)
        num=0
        for i in range(4):
            s=str(x)+str(y+i)
            if all_right(x,y+i) and dic1[callm][s]==dic1[callm][s1]:
                num=num+1
        if num==4 and dic1[callm][s1]!=LargeWhiteSquare:
            winer(x,y,0,1,callm)
            return True

        #print(num)
        num=0
        for i in range(4):
            s=str(x+i)+str(y)
            if all_right(x+i,y) and dic1[callm][s]==dic1[callm][s1]:
                num=num+1
        if num==4 and dic1[callm][s1]!=LargeWhiteSquare:
            winer(x,y,1,0,callm)
            return True
        #print(num)
        num=0
        for i in range(4):
            s=str(x+i)+str(y-i)
            if all_right(x+i,y-i) and dic1[callm][s]==dic1[callm][s1]:
                num=num+1
        if num==4 and dic1[callm][s1]!=LargeWhiteSquare:
            winer(x,y,1,-1,callm)
            return True
        #print(num)
        num=0
        for i in range(4):
            s=str(x+i)+str(y+i)
            if all_right(x+i,y+i) and dic1[callm][s]==dic1[callm][s1]:
                num=num+1
        if num==4 and dic1[callm][s1]!=LargeWhiteSquare:
            winer(x,y,1,1,callm)
            return True

        #print(num)
        return False

    def check1(callm):
        for x in range(X):
            for y in range(Y):
                if check(x,y,callm):
                    return True
        return False

    @bot.inline_handler(lambda query: query.query=='' )
    def query_text(inline_query):
        try:
            #print('here')
            r1= types.InlineQueryResultArticle(id='1', title='play connectfour game', input_message_content= types.InputTextMessageContent('play connectfour:first 4 pieces consecutively in a (row or column or diagonal) wins the game'),reply_markup=makeKeyboard1())
           # r = types.InlineQueryResultGame(id='1',game_short_name='connectfour')
            bot.answer_inline_query(inline_query.id, [r1])
        except Exception as e:
            print('exception happends')

    @bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
    def test_chosen(chosen_inline_result):
        msg=MESSAGE()
        if chosen_inline_result.from_user.username!=None:
            msg.ch1='@'+chosen_inline_result.from_user.username
        else :
            msg.ch1=chosen_inline_result.from_user.first_name
        msg.id1=chosen_inline_result.from_user.id
        dic2[chosen_inline_result.inline_message_id]=msg


    @bot.callback_query_handler(func=lambda call: True)
    def handle_query(call):
        try:
            ch1='sac'
            ch2='sacsa'
            turn=0
            flag=False
            try:
                msg=dic2[call.inline_message_id]
                ch1=msg.ch1
                id1=msg.id1
                ch2=msg.ch2
                id2=msg.id2
                turn=msg.turn
                flag=msg.flag
                #ch1=dic_ch1[call.inline_message_id]
                #ch2=dic_ch2[call.inline_message_id]
                #turn=dic_turn[call.inline_message_id]
                #flag=dic_flag[call.inline_message_id]
            except:
                print('nashod')
            #print(id1)
            if flag==True:
                return
            s=(call.data)
            if s=='end' and ((turn==0 and call.from_user.id==id2) or (turn==1 and call.from_user.id==id1)):
                #print('im in end')
                a=dic2[call.inline_message_id].Time
                b=dt.datetime.now()
                c=(b-a).total_seconds()
                #print(c)
                if c<60:
                    bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='if your opponent doesnt respond for'+str(60-c)+'seconds you can press it again and end the game.')
                else:
                    del dic[call.inline_message_id]
                    del dic1[call.inline_message_id]
                    del dic2[call.inline_message_id]
                    bot.edit_message_text(text='Game ended.',
                                          inline_message_id=call.inline_message_id,
                                          parse_mode='HTML')
                    return
            elif s=='end':
                bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='you cant press this button')
            elif s=='nothing':
                #print('here')
                stringList = {}
                #print(message.chat.id)
                for x in range(X):
                    for y in range(Y):
                        s=str(x)+str(y)
                        stringList[s]=LargeWhiteSquare
                dic1[call.inline_message_id]=stringList
                #print(dic1[call.inline_message_id]['00'])
                if call.from_user.username!=None:
                    ch2='@'+call.from_user.username
                else :
                    ch2=call.from_user.first_name
                id2=call.from_user.id
                #print(call.inline_message_id)
                #dic_ch2[call.inline_message_id]=ch2
                #dic_flag[call.inline_message_id]=flag
                #dic_turn[call.inline_message_id]=turn
                arr= array.array('i',[5,5,5,5,5,5,5])
                dic[call.inline_message_id]=arr
                #print('here')
                if ch1==None:
                    ch1='no username'
                if ch2==None:
                    ch2='no username'
                if id1!=id2:
                    print((ch1,ch2))
                    sd1=str(id1)+str(id2)
                    sd2=str(id2)+str(id1)
                    if sd1 in dic3:
                        ok=0
                    else:
                        dic3[sd1]=0
                        dic3[sd2]=0

                    #print('here ghablesh')
                    bot.edit_message_text(text=ch1+" turn: "+BlueCircle,
                                          inline_message_id=call.inline_message_id,
                                          reply_markup=makeKeyboard(call.inline_message_id),
                                          parse_mode='HTML')

                    #print('here ghablesh')
                else:
                    bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='wait for some one to join')
                #print('here agin!')
                dic2[call.inline_message_id].ch1=ch1
                dic2[call.inline_message_id].ch2=ch2
                dic2[call.inline_message_id].turn=turn
                dic2[call.inline_message_id].flag=flag
                dic2[call.inline_message_id].id1=id1
                dic2[call.inline_message_id].id2=id2
                #print()
                dic2[call.inline_message_id].Time=dt.datetime.now()
            elif (turn==0 and call.from_user.id==id1) or (turn==1 and call.from_user.id==id2):
                if ch1==None:
                    ch1='no username'
                if ch2==None:
                    ch2='no username'
                #print(s)
                x = int(s[0])
                y = int(s[1])
                if dic[call.inline_message_id][y]>=0:
                    turn=(turn+1)%2
                    dic2[call.inline_message_id].turn=turn
                else:
                    bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='its full')
                    return


                if turn == 0:
                    dic2[call.inline_message_id].Time=dt.datetime.now()
                    if dic[call.inline_message_id][y]>=0:
                        s1=str(dic[call.inline_message_id][y])+str(y)
                        dic[call.inline_message_id][y]=dic[call.inline_message_id][y]-1
                        dic1[call.inline_message_id][s1]=RedCircle
                    flag = check1(call.inline_message_id)

                    dic2[call.inline_message_id].flag=flag
                    txt=ch1+" turn: "+BlueCircle
                    if flag==True:
                        sd1=str(id1)+str(id2)
                        sd2=str(id2)+str(id1)
                        dic3[sd2]=dic3[sd2]+1
                        txt=ch2+" win "+RedCircle+'\n'+ch1+':'+str(dic3[sd1])+'\n'+ch2+':'+str(dic3[sd2])
                    bot.edit_message_text(
                                    text=txt,
                                    inline_message_id=call.inline_message_id,
                                    reply_markup=makeKeyboard(call.inline_message_id),
                                    parse_mode='HTML')

                    bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=False,
                                  text='Next')
                else:
                    dic2[call.inline_message_id].Time=dt.datetime.now()
                    if dic[call.inline_message_id][y]>=0:
                        s1=str(dic[call.inline_message_id][y])+str(y)
                        dic[call.inline_message_id][y]=dic[call.inline_message_id][y]-1
                        dic1[call.inline_message_id][s1]=BlueCircle
                    flag = check1(call.inline_message_id)

                    dic2[call.inline_message_id].flag=flag
                    txt=ch2+" turn: "+RedCircle
                    if flag==True:
                        sd1=str(id1)+str(id2)
                        sd2=str(id2)+str(id1)
                        dic3[sd1]=dic3[sd1]+1
                        txt=ch1+" win "+BlueCircle+'\n'+ch1+':'+str(dic3[sd1])+'\n'+ch2+':'+str(dic3[sd2])
                    bot.edit_message_text(
                                    text=txt,
                                    inline_message_id=call.inline_message_id,
                                    reply_markup=makeKeyboard(call.inline_message_id),
                                    parse_mode='HTML')

                    bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=False,
                                  text='Next')
            else:
                bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='not your turn')
            #print(dic2[call.inline_message_id].Time)
            if flag==True:
                del dic[call.inline_message_id]
                del dic1[call.inline_message_id]
                del dic2[call.inline_message_id]
            #dic_ch1[call.inline_message_id]=ch1
            #dic_ch2[call.inline_message_id]=ch2
            #dic_turn[call.inline_message_id]=turn
            #dic_flag[call.inline_message_id]=flag
        except:
            bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text='your not in the game')
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=0)
        except:
            time.sleep(1)
            print('pickle out')
            pickle_out = open("dict.pickle","wb")
            pickle.dump(dic3, pickle_out)
            pickle_out.close()
except:
    print('pickle out')
    pickle_out = open("dict.pickle","wb")
    pickle.dump(dic3, pickle_out)
    pickle_out.close()
