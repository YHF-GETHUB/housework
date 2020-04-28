# difflib模块作为python的标准库模块，无需安装，作用是比对文本之间的差异，且支持输出可读性比较强的html格式。


# !coding=utf-8
# 2018-9-19
import sys
import difflib


# 读取配置文件函数
def read_file(file_name):
    try:
        file_handle = open(file_name, 'r')
        text = file_handle.read().splitlines()  # 读取后以行进行分割
        file_handle.close()
        return text
    except IOError as error:
        print
        'Read file Error: {0}'.format(error)
        sys.exit()


# 比较两个文件并输出html格式的结果
def compare_file(file1_name, file2_name):
    if file1_name == "" or file2_name == "":
        print
        '文件路径不能为空：file1_name的路径为：{0}, file2_name的路径为：{1} .'.format(file1_name, file2_name)
        sys.exit()
    text1_lines = read_file(file1_name)
    text2_lines = read_file(file2_name)
    diff = difflib.HtmlDiff()  # 创建htmldiff 对象
    result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
    #  将结果保存到result.html文件中并打开
    try:
        with open('result.html', 'w') as result_file:  # 同 f = open('result.html', 'w') 打开或创建一个result.html文件
            result_file.write(result)  # 同 f.write(result)
    except IOError as error:
        print
        '写入html文件错误：{0}'.format(error)


if __name__ == "__main__":
    compare_file(r'D:\1.txt', r'D:\2.txt')  # 传入两文件的路径