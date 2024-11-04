# 自动下载微信公众号图片并自动去除水印



* 安装依赖

  ```shell
  pip install -r requirement.txt
  ```

* 修改配置文件config.json

  ```json
  url = '公众号文章链接'
  
  ROOT_PATH = r'C:\article\'  # 保存的路径
  ```

* 运行
    ```shell
    python main.py
    ```
运行后会生成一个时间戳的文件夹，里面按照图片出现的顺序命名，processed- 这个前缀的为去掉水印后的图片。
![效果图](./image/img.png)

### 欢迎关注公众号

原文链接：


  

  
