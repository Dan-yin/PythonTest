try :
    raise(KeyboardInterrupt)
except KeyboardInterrupt:
    print('this is a test')
finally:
    print('this is a final result')