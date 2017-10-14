try:
    pass

except:
    pass

finally:
    pass


try:
    pass
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


# 오류 일부러 발생시키기
try:
    raise NotImplementedError
except NotImplementedError as e:
    print(e)
