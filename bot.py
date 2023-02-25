import datetime
import re
import telebot
import config
import ephem


def main():
    bot = telebot.TeleBot(config.BOT_TOKEN)

    @bot.message_handler(commands=['wordcount', 'wc'])
    def word_count(msg):
        args = telebot.util.extract_arguments(msg.text)
        if args:
            res = args.strip().split()
            for each in res:
                if not each.isalpha():
                    bot.send_message(msg.chat.id,
                                     f'Input some WORDS, not numbers')
                    break
            bot.send_message(msg.chat.id, f'{len(res)} words')
        else:
            bot.send_message(msg.chat.id, 'Input some words after command')

    @bot.message_handler(commands=['full_moon', 'next_full_moon', 'moon'])
    def next_full_moon(msg):
        args = telebot.util.extract_arguments(msg.text)
        next_moon = f'Next full moon based on today will be on '+\
                    str(
                        ephem.next_full_moon(
                            datetime.datetime.today()
                        )
                    )
        if args:
            res = args.strip().split()[0]
            if re.match(r'(0?[1-9]|[12][0-9]|3[01])[\-]'
                        r'(0?[1-9]|1[012])[\-]([12][0-9]+)', res):
                try:
                    res = datetime.datetime.strptime(res, '%d-%m-%Y')
                    next_moon = f'Next full moon based on {res} will be on ' +\
                                str(
                                    ephem.next_full_moon(
                                        res
                                    )
                                )
                except (ValueError, KeyError) as e:
                    print(e)
                    next_moon += "\nPlease input ONLY " \
                                 "date using format dd-mm-yyyy"
            else:
                next_moon += "\nPlease input date using format dd-mm-yyyy"
        bot.send_message(msg.chat.id, next_moon)

    @bot.message_handler(commands=['start', 'help'])
    def info_message(msg):
        bot.send_message(msg.chat.id,
                         f'Available commands are: '
                         f'\n/wordcount /wc counting words put '
                         f'after the command'
                         f'\n/next_full_moon /next_moon /moon'
                         f' - put a date dd-mm-yyyy after the comand to'
                         f' see the next full moon date')

    try:
        bot.infinity_polling(allowed_updates=['chat_member',
                                              'my_chat_member',
                                              'message'])
    except KeyboardInterrupt:
        bot.stop_polling()


if __name__ == '__main__':
    main()