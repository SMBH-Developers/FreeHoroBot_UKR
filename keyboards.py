from aiogram import types


class Markups:
    start_mrkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_mrkup.add(types.KeyboardButton(text='✨Отримати безкоштовний гороскоп'))
    start_mrkup.add(types.KeyboardButton(text='📜Освітнє меню'))

    study_mrkup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    study_btns_titles = ['✨Що таке астрологія?', '✨Гороскоп - що це?',
                         '✨Як зявився перший гороскоп?', '✨Астро-рада на день',
                         '✨Що вивчають в астрології?', '✨Що таке 12 будинків в астрології?',
                         '✨Який будинок відповідає за роботу?', '✨Який будинок відповідає за сімю?',
                         '🙏Отримати безкоштовний гороскоп']

    study_mrkup.add(types.KeyboardButton('✨Що таке астрологія?'), types.KeyboardButton('✨Гороскоп - що це?'))
    study_mrkup.add(types.KeyboardButton('✨Як зявився перший гороскоп?'), types.KeyboardButton('✨Астро-рада на день'))
    study_mrkup.add(types.KeyboardButton('✨Що вивчають в астрології?'), types.KeyboardButton('✨Що таке 12 будинків в астрології?'))
    study_mrkup.add(types.KeyboardButton('✨Який будинок відповідає за роботу?'), types.KeyboardButton('✨Який будинок відповідає за сімю?'))
    study_mrkup.add(types.KeyboardButton('🙏Отримати безкоштовний гороскоп'))

    mrkup_for_every_study_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrkup_for_every_study_btn.add(types.KeyboardButton('✨Отримати безкоштовний гороскоп на рік'))
    mrkup_for_every_study_btn.add(types.KeyboardButton('👈Назад'))

    to_menu_mrkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    to_menu_mrkup.add(types.KeyboardButton('📜Освітнє меню'))

    kb_if_how_to_get_know_zodiac = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_if_how_to_get_know_zodiac.add(types.KeyboardButton(text='✨Отримати безкоштовний гороскоп на 2024 рік'))
    kb_if_how_to_get_know_zodiac.add(types.KeyboardButton(text='👈Назад'))

    admin_mrkup = types.InlineKeyboardMarkup()
    admin_mrkup.add(types.InlineKeyboardButton(text='Пользователей всего', callback_data='Admin_Users_Total'))
    admin_mrkup.add(types.InlineKeyboardButton(text='Пользователей за сегодня', callback_data='Admin_Users_For_TODAY'))
    admin_mrkup.add(types.InlineKeyboardButton(text='Ввели дату за сегодня', callback_data='Admin_Dates_For_TODAY'))
    admin_mrkup.add(types.InlineKeyboardButton(text='Зашли после рассылки 17ого марта 19:15', callback_data='Admin_17_march_sending'))
    admin_mrkup.add(types.InlineKeyboardButton(text='Рассылка', callback_data='Admin_Send_Messages'))  # Рассылка по любым
    admin_mrkup.add(types.InlineKeyboardButton(text='Рассылка тем, кто еще не перешёл', callback_data='Admin_Special_Send_Msgs'))  # Раcсылка только по тем, кто не перешёл на наш аккаунт
    admin_mrkup.add(types.InlineKeyboardButton(text='Перешедших по реф ссылкам', callback_data='Admin_Referal_Users'))
    back_admin_mrkup = types.InlineKeyboardMarkup()
    back_admin_mrkup.add(types.InlineKeyboardButton(text='⬅️ В меню админа', callback_data='Admin_BACK'))

    @staticmethod
    def generate_send_msgs_step(sending_type: str) -> types.InlineKeyboardMarkup:
        send_messages_step_mrkup = types.InlineKeyboardMarkup()
        send_messages_step_mrkup.add(types.InlineKeyboardButton(text='Первая ступень', callback_data=f'Sending?Step=0&type={sending_type}'),
                                     types.InlineKeyboardButton(text='Вторая ступень', callback_data=f'Sending?Step=1&type={sending_type}'))
        send_messages_step_mrkup.add(types.InlineKeyboardButton(text='Третья ступень', callback_data=f'Sending?Step=2&type={sending_type}'),
                                     types.InlineKeyboardButton(text='Четвёртая ступень', callback_data=f'Sending?Step=3&type={sending_type}'))
        send_messages_step_mrkup.add(types.InlineKeyboardButton(text='Отправить всем', callback_data=f'Sending?Step=ALL&type={sending_type}'))
        send_messages_step_mrkup.add(types.InlineKeyboardButton(text='⬅️ В меню админа', callback_data='Admin_BACK'))
        return send_messages_step_mrkup

    back_to_steps = types.InlineKeyboardMarkup()
    back_to_steps.add(types.InlineKeyboardButton(text='⬅️ Назад', callback_data='Admin_Send_Messages'))

    cancel_sending = types.InlineKeyboardMarkup()
    cancel_sending.add(types.InlineKeyboardButton(text='Відміна!', callback_data='Cancel_Getting_Msg_For_Sending'))

    to_our_tg_mrkup = types.InlineKeyboardMarkup()
    to_our_tg_mrkup.add(types.InlineKeyboardButton(text='ОТРИМАТИ ГОРОСКОП', url=f'https://t.me/Ezoteric_Soul'))


    @staticmethod
    def generate_delete_msg_mrkup(arg=None):
        mrkup_to_del_msg = types.InlineKeyboardMarkup()
        mrkup_to_del_msg.add(types.InlineKeyboardButton('Закрити', callback_data=f'delete_msg{arg if arg else ""}'))
        return mrkup_to_del_msg

    mrkup_referal_program = types.InlineKeyboardMarkup()
    mrkup_referal_program.add(types.InlineKeyboardButton(text='✨Перевірити виконання умов', callback_data='ref_program?check_reqs'))
    mrkup_referal_program.add(types.InlineKeyboardButton(text='✨Переглянути відгуки', callback_data='ref_program?reviews'))
    mrkup_referal_program.add(types.InlineKeyboardButton(text='✨Як правильно запросити друзів?', callback_data='ref_program?guide'))
