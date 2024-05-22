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
| ![](https://hackmd.io/_uploads/HySD7ASfa.png) | ![](https://hackmd.io/_uploads/rJU_mCSG6.png) |

如果不做這個步驟直接打包，在 fontforge 顯示會長這樣：
![](https://hackmd.io/_uploads/HJwYN0rG6.png)

放大圖：

| 曲                                            | 曙                                            | 曾                                            |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| ![](https://hackmd.io/_uploads/S1GL40HMp.png) | ![](https://hackmd.io/_uploads/ByWUBABfT.png) | ![](https://hackmd.io/_uploads/H16kBRrfa.png) |

### SVG ---> SVG (打包成一個 SVG 檔)
- 执行没报错,但是没法生成
這個步驟跟 https://chiaoooo.github.io/font-svg-viewer/ 不同的地方是不採取替換再打包的方法，而是直接打包現有的 svg 檔，節省空間及時間 ( 31026 kb 縮小至 9252 kb / 12 小時縮短至 2 分鐘 )。
- 完成以後會在 final_font 裡面看到 fontpico.svg，將它丟入 FontForge 內並完成後續設定。

```
node readfile.js
```

### SVG ---> TTF

安装FontForge 并在FontForge目录下创建一个SVG目录 并把生成好的svg放进去

進入 FontForge 以後可以看到字不會有黑一塊一塊的，就代表成功了!
![](https://hackmd.io/_uploads/BJkrfeLGp.png)

- 點選 Element ---> Font info，在這邊可以修改字體名稱
  ![](https://hackmd.io/_uploads/SkC_aRHGp.png)

- 點選左邊那排的 OS/2 ---> Charsets ---> MS Code Pages 取消 Default 的打勾 ---> 選取 950 ---> ok！
  ![](https://hackmd.io/_uploads/SygB0CHGa.png)

- 點選 File ---> Generate Fonts 輸出成 ttf 檔（跳出訊息都選 yes / generate）
  ![](https://hackmd.io/_uploads/rJMZJJLGp.png)

### 完成 !
