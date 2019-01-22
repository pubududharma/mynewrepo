"""
This greets the world and prints today's datetime
"""
import datetime

if __name__ == '__main__':
    print(f'\n{"Hello World":*^50}')
    print('\nToday is', end=' ')
    print(datetime.datetime.now().strftime('%B %d, %Y'))
    print('\nHave a nice day!')
