### env

```
git clone https://github.com/chiaoooo/PngToTTF
mkdir svg_separate
mkdir final_font
```

### 转换Font

```
npm install
```

### PNG ---> SVG
- 修改 input 为自己的 png 文件夹
- svg 结束在 svg_separate
```
node potrace.js
```

### SVG ---> SVG

這個步驟為了讓 svg 中的 fill-rule="evenodd" 不被下一個步驟的 svgicons2svgfont 忽略。
- 处于pytorch虚拟conda环境 先 pip install picosvg
- M3 Pro 處理 5,345 字大約需要 148 秒
- 處理過的 SVG 會存在 pico 資料夾
- fillrule 的比較：
```
node run_pico.js
```

| NoneZero                                      | EvenOdd                                       |
| --------------------------------------------- | --------------------------------------------- |
|  ![img.png](img%2Fimg.png)| ![img_1.png](img%2Fimg_1.png) |

如果不做這個步驟直接打包，顯示會長這樣：

| 曲                                            | 曙                             | 曾                                            |
| --------------------------------------------- |-------------------------------| --------------------------------------------- |
| ![img_2.png](img%2Fimg_2.png) | ![img_3.png](img%2Fimg_3.png) | ![img_4.png](img%2Fimg_4.png) |

## 字体生成
安装 FontForge 进入安装目录

双击fontforge-console.bat

修改to_ttf.py并且复制文件到对应安装目录

```shell
ffpython to_ttf.py
```

### 完成 !
