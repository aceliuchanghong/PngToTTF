import fontforge, os, psMat
"""
进入到C:\Program Files (x86)\FontForgeBuilds,其实就是他得到安装目录
双击fontforge-console.bat
输入ffpython to_ttf.py
"""

def main():
    # 定义参数
    img_list = list()

    # 获取文件列表
    for file in os.listdir(img_dir):
        if os.path.splitext(file)[1].lower() in '.svg':
            img_list.append(file)
    print('当前总图片数量： %d' % len(img_list))

    # 循环处理图片
    # 创建字体
    font = fontforge.font()
    font.encoding = 'UnicodeFull'
    font.version = '1.0'
    font.weight = 'Regular'
    if font_name:
        font.fontname = font_name
        font.familyname = f'{font_name}-family'
        font.fullname = f'{font_name}-fullname'
    else:
        font.fontname = 'test'
    for img_path in img_list:
        # 获取unicode
        codestr = os.path.splitext(img_path)[0]
        code = ord(codestr)

        # 创建字符
        glyph = font.createChar(code, "uni" + codestr)
        glyph.importOutlines(os.path.join(img_dir, img_path))

        # 位移调整
        base_matrix = psMat.translate(0, 0)
        glyph.transform(base_matrix)

        # 写入ttf
    font.generate(output)

    print('全部处理结束,svg文件若要删除自行处理')


if __name__ == "__main__":
    img_dir = r'C:\Users\lawrence\PycharmProjects\PngToTTF\pico'  # 上一步png转换至svg存放的路径
    output = r'C:\Users\lawrence\PycharmProjects\PngToTTF\test.ttf'  # test.ttf
    font_name = 'test'
    main()
