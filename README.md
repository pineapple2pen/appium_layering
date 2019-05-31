# appium_layering

  项目是基于appium进行移动端自动化测试，由于没有ios设备，所以目前是只在win上面测试过，可以运行。

***
### 环境配置
- appium
- java
- android(adb aapt等工具)
- nodeJs
- python(appium)

***
### 项目结构

- common
  - adb_tools.py
    adb工具箱，封装了部分adb命令
  - apk_tool.py
    apk解析工具，主要依赖使用aapt工具。
  - config.py
    核心，整个框架最重要的一个类，所以信息均注册在这个类下
  - html_test_runner.py
    unittest报告生成类，网上开源，本人进行了简单汉化
  - singleton.py
    类装饰器，通过闭包，将类变为单例模式
  - time_tools.py
    时间工具类
- page
  - page.py
    page类
- server
  - appium_server.py
    appium服务启动关闭类
  - driver_server.py
    封装了页面操作方法的一个driver类
- test_runner
  - runner.py
    用例执行类
- page_config
  - ****.json
    页面配置
- operator_config
  - ****.json
    页面操作配置
- test_case
  - ****.json
    用例
***

### 页面配置
exp:
```json
{
  "id": "startPage",
  "name": "启动页",
  "elements": [
    {
      "id": "skip",
      "name": "跳过",
      "android": "com.mymoney:id/splash_skip_tv",
      "ios": ""
    },
    {
      "id": "welcome_pic",
      "name": "启动页图片",
      "android": "com.mymoney:id/splash_skip_tv",
      "ios": ""
    }
  ]
}
```
说明：

| key名 | 含义 | 类型 | 是否可为空|
| :--: | :--: | :--: | :--: |
|id|页面唯一标示id|字符串|否|
|name|页面名称|字符串|是|
|elements|页面元素集合|集合|否|
|elements-id|页面元素唯一标示id|字符串|是|
|elements-name|页面元素名称|字符串|否|
|elements-android|安卓定位|字符串|是|
|elements-ios|ios定位|字符串|否|

***

### 操作配置
exp:
```json
[
  {
    "id": "click_skip",
    "name": "点击跳过按钮",
    "page": "startPage",
    "operator": [
      {
        "order": 1,
        "func": "click_exist",
        "element_id": "skip",
        "other_param_dict": {},
        "other_param_list": [],
        "saveReturn": false,
        "return": null
      }
    ]
  }
]
```
说明：

| key名 | 含义 | 类型 | 是否可为空|
| :--: | :--: | :--: | :--: |
|id|页面操作标示id|字符串|否|
|name|页面操作名称|字符串|是|
|page|所属页面|字符串|是|
|operator|页面操作步骤|集合|否|
|order|操作顺序|整数|是|
|func|执行函数名称|字符串|否|
|element_id|执行元素定位|字符串|是|
|other_param_dict|函数执行字典参数|字典|是|
|other_param_list|函数执行集合参数|集合|是|
|saveReturn|执行函数后是否保存|布尔|否|
|return|保存赋值key名|字符串|是|

***

### 用例配置
exp:
```json
[
  {
    "id": "startPageWaitTime",
    "name": "启动页面停留时间",
    "run": true,
    "execute": [
      {
        "execute_id": "startPage-wait_page_gone",
        "page": "startPage",
        "operator": "wait_page_gone",
        "save_return": true,
        "save_name": "startPage-wait_page_gone"
      }
    ],
    "check_type": "func-0",
    "check_ope": [],
    "check_param": [
      {
        "check_type": "compare",
        "check_val": "startPage-wait_page_gone",
        "check_func": "gt",
        "param": 2.0,
        "other_param": ""
      }
    ]
  }
]
```

说明：

| key名 | 含义 | 类型 | 是否可为空|
| :--: | :--: | :--: | :--: |
|id|用例id|字符串|否|
|name|用例名称|字符串|是|
|run|是否执行|布尔|否|
|execute|执行步骤|集合|否|
|execute_id|执行id|字符串|否|
|page|执行页面|字符串|否|
|operator|执行的操作id(操作步骤id)|字符串|否|
|save_return|是否保存该执行步骤返回|布尔|否|
|save_name|返回值变量名|字符串|是|
|check_type|检查函数|字符串|是|
|check_ope|检查操作，内部和execute相同|集合|是|
|check_param|检查参数|集合|否|
|check_param-check_type|检查类型|字符串|是|
|check_param-check_val|save_name中保存的变量|字符串|否|
|check_param-check_func|函数名称（gt、gte、lt、lte、eq等）|字符串|否|
|param|检查对比参数|-|是|
|other_param|检查其他参数|-|否|
