
## captcha-solver

很久不写python了，之前写的验证码破解服务，放上来，利用模板匹配破解一些简单的验证码，机器学习破解复杂验证码的部分或许以后大概再研究吧。

```bash
# env anaconda3
run:python app.py
```

web:http://localhost:8885


### 预测接口

本地：POST http://localhost:8885/predict

body:

```
{
    "type":<type>
    "img_base64":<img_base64>
}

```

return

```
{
    "predict":<predict>
    "result":"ok"
}

```

### 示例


