# Python 学习记录

从基础语法开始，配合小脚本练习 Python。先读 [学习文档](学习文档.md)，再运行对应文件，并修改输入观察结果。

## 学习顺序

| 顺序 | 文件 | 内容 | 需要输入 |
| --- | --- | --- | --- |
| 1 | [hello_world.py](hello_world.py) | 第一个程序 | 无 |
| 2 | [constant_variable.py](constant_variable.py) | 字面量、变量、类型、字符串与输入 | 姓名、年龄 |
| 3 | [day_test.py](day_test.py) | 机器人充电小练习 | 名称、整数电量，各占一行 |
| 4 | [operator.py](operator.py) | 算术运算 | 无 |
| 5 | [if_else.py](if_else.py) | 正负判断与四则运算 | 整数、两个数、运算符，各占一行 |
| 6 | [while_for.py](while_for.py) | while、for、range 与累加 | 无 |
| 7 | [list.py](list.py) | 列表索引、切片与常用方法 | 无 |
| 8 | [str.py](str.py) | 字符串索引、切片与常用方法 | 无 |

笔记按相同主题组织，另补充了列表解包、列表推导式、输入校验和复习题。笔记中标为补充的示例不一定已写入练习脚本。

建议每次完成一个主题：先预测输出，再运行对应脚本，最后修改一个输入或边界条件并解释变化。完成笔记第 13 节后，可用 [练习参考答案](练习参考答案.md) 自查。

## 环境与运行

需要 **Python 3.10+**（`if_else.py` 使用 `match`），不需要第三方库。在终端中进入本仓库目录后运行：

Windows PowerShell：

```powershell
python --version
python hello_world.py
python constant_variable.py
```

若系统使用 Python 启动器，也可将 `python` 换成 `py -3`，并确认该解释器的版本至少为 3.10。

Ubuntu / Linux：

```bash
python3 --version
python3 hello_world.py
python3 constant_variable.py
```

若已激活虚拟环境，可使用该环境的 `python`。运行其他练习时，将命令中的文件名替换为表格里的文件名。

看到 `name:` 和 `age:` 时分别输入内容，再按 Enter；`day_test.py` 没有提示文字，会依次等待两行输入。

运行 `if_else.py` 的一次交互示例：

```text
num=-3
-3是负数
num1=10
num2=4
operator=/
10.0/4.0=2.5
```

带 `=` 的行末是手动输入的内容。输入运算符时只输入 `+`、`-`、`*` 或 `/`，不用加引号。此脚本将除数为零和未知运算符统一输出为 `!!!`；笔记第 8 节给出了区分提示的写法。需要数字的位置输入非数字文本会报 `ValueError`，当前练习尚未处理输入异常；可参考笔记第 12 节的输入校验示例。

## 文件命名注意

当前保留原练习文件名。`operator.py` 与 Python 标准库模块 `operator` 同名，在本目录执行 `import operator` 或导入依赖它的库时，可能加载到练习脚本，出现额外输出或 `ImportError`。以后扩展项目时，建议将其改名为 `operators_demo.py`，并同步修改笔记链接。

## 参考资料

- [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/index.html)
- [控制流：条件、循环与模式匹配](https://docs.python.org/zh-cn/3/tutorial/controlflow.html)
- [数据结构：列表等容器](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)
