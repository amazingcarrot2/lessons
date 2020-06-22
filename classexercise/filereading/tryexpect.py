try:
    # 可能引发异常的代码
    open('data.txt')
except:
    # 异常发生后处理的代码
    print('err')
else:
    # 未发生异常时执行的代码
    print('open success')
finally:
    # 结束异常处理前的代码（不管是否异常都会在最后运行）
    print('done')
