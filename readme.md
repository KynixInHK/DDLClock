# DDL闹钟项目

项目概述：https://docs.propranolol.cn/docs/ddl_clock.html

## DDL闹钟项目后端

以下是本文件夹中部分文件的概述

1. settings.json和profiles.json两个文件，分别用来存储用户信息和配置信息。“用户信息”是用户在使用APP时产生的，当然你也可以提前给个默认值。“配置信息”是APP自带的，必须出厂时设定好，非必要不修改。目前能想到的“用户信息”包括：token、用户可以调节的参数等，“配置信息”包括：接入的应用ID等
2. 建议每个文件尽量定义函数和类，方便import使用，因为入口是哪个文件还不好说，不要在`if __name__ == "__main__":`下面写太多东西。根据我贫瘠的经验，涉及到跨文件的数据，可能需要一个专门的values.py文件，用字典的方式存放内容
3. 尽可能在成品中把任何参数都放到外部，不要简单地把参数贴到代码里面
4. 提交git的时候一定注意.gitignore文件，不要作死把用户数据、token、应用程序ID这种东西提交上去开源了（比如两个json文件）